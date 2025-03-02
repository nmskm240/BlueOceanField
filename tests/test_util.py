import pytest
import rx
import rx.operators as op
from blueOceanField.application.util import observable_to_async_generator


@pytest.mark.asyncio
async def test_observable_normal_case():
    """✅ 正常系: 1秒ごとに値を3つ発行する"""
    observable = rx.interval(1.0).pipe(op.take(3))  # 0, 1, 2 を発行して完了

    results = []
    async for value in observable_to_async_generator(observable):
        results.append(value)

    assert results == [0, 1, 2], f"Expected [0, 1, 2], but got {results}"


@pytest.mark.asyncio
async def test_observable_error_case():
    """❌ エラー系: 途中でエラーが発生した場合"""

    def error_observable(observer, scheduler):
        observer.on_next(42)
        observer.on_error(ValueError("Test error"))

    observable = rx.create(error_observable)

    async for e in observable_to_async_generator(observable):
        if isinstance(e, Exception):
            pytest.raises(ValueError, match="Test error")

@pytest.mark.asyncio
async def test_observable_immediate_complete():
    """✅ 即時完了系: 何も発行せずに即完了"""
    observable = rx.empty()  # 何も出さずに完了する Observable

    results = []
    async for value in observable_to_async_generator(observable):
        results.append(value)

    assert results == [], f"Expected [], but got {results}"
