from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, Optional
from injector import inject
import river
import river.time_series
import rx
import rx.internal
import rx.operators as op
import rx.operators
import rx.scheduler

from blueOceanField.domain.feature import FeatureProcess
from blueOceanField.domain.market import IExchange, Ohlcv, Symbol


# NOTE: 予測対象は選択可能にしたほうがいい気がするが、設計上Ohlcvのどれかしか選べないため選択可能にするメリットがあるか微妙
TARGET_LABEL = "close"


@dataclass(frozen=True)
class BotLearnDataset:
    input: dict
    target: float

@dataclass(frozen=True)
class BotPredicateDataset:
    input: dict

class Bot:
    @inject
    def __init__(self, exchange: IExchange):
        self._is_running = False
        self._model = river.time_series.SNARIMAX(1, 0, 0)
        self._exchange = exchange
        self._pipeline = rx.empty()

        self._on_model_updated_subject = rx.subject.Subject()
        self._on_predicated_subject = rx.subject.Subject()

    @property
    def is_running(self) -> bool:
        return self._is_running

    @property
    def on_model_updated_as_observable(self) -> rx.Observable:
        return self._on_model_updated_subject

    @property
    def on_predicated_as_observable(self) -> rx.Observable:
        return self._on_predicated_subject

    def run(
        self,
        symbol: Symbol,
        from_: Optional[datetime] = None,
        to: Optional[datetime] = None,
    ) -> None:
        def learn_and_predicate(inputs: Iterable[dict]) -> None:
            self._model_update(inputs)
            self._predicate(dict(inputs[1]))

        self._exchange.pull_stream(symbol, from_, to).pipe(
            op.map(lambda x: x.to_dict()),
            op.do_action(lambda x: print(x)),
            op.flat_map(lambda x: self._pipeline.pipe(op.start_with(x))),
            op.buffer_with_count(2, 1),
        ).subscribe(
            on_next=lambda x: learn_and_predicate(x)
        )

    def _model_update(self, input: Iterable[dict]) -> None:
        prev = input[0]
        prev.pop(TARGET_LABEL)
        target = input[1][TARGET_LABEL]
        dataset = BotLearnDataset(prev, target)
        self._model.learn_one(dataset.target, dataset.input)
        self._on_model_updated_subject.on_next(None)

    def _predicate(self, x: dict):
        pred = self._model.forecast(1, xs=[x])
        self._on_predicated_subject.on_next(pred[0])
