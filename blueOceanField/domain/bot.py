from datetime import datetime
from typing import Iterable, Optional
from injector import inject
import river
import river.time_series
import rx
import rx.operators as op

from blueOceanField.domain.feature import FeatureProcess
from blueOceanField.domain.market import IExchange, Ohlcv, Symbol


class Bot:
    @inject
    def __init__(self, exchange: IExchange, pipeline: rx.Observable):
        self._model = river.time_series.SNARIMAX(1, 0, 0)
        self._exchange = exchange
        self.pipeline = pipeline

    def run(
        self,
        symbol: Symbol,
        from_: Optional[datetime] = None,
        to: Optional[datetime] = None,
    ):
        self._exchange.pull_stream(symbol, from_, to).pipe(
            op.map(lambda x: x.to_dict()),
            op.buffer_with_count(2, 1),
            op.map(
                lambda x: (
                    prev_input := {
                        key: value for key, value in x[0].items() if key != "close"
                    },
                    ans := x[1]["close"],
                    input := {
                        key: value for key, value in x[1].items() if key != "close"
                    },
                    x[1],
                )
            ),
        ).subscribe(
            on_next=lambda x: self.__update(x),
            on_error=lambda e: print(e),
        )

    def __update(self, x):
        self._model.learn_one(x[1], x[0])
        pred = self._model.forecast(1, xs=[x[2]])
        print(pred)
