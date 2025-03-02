import asyncio
from typing import Any, AsyncGenerator

import rx
from rx.scheduler.eventloop import AsyncIOScheduler


async def observable_to_async_generator(observable: rx.Observable) -> AsyncGenerator[Any, None]:
    queue = asyncio.Queue()

    def on_next(value):
        queue.put_nowait(value)

    def on_error(error):
        queue.put_nowait(error)

    def on_completed():
        queue.put_nowait(None)

    async def subscribe():
        observable.subscribe(
            on_next=on_next,
            on_error=on_error,
            on_completed=on_completed,
            scheduler=AsyncIOScheduler(asyncio.get_event_loop())
        )

    asyncio.create_task(subscribe())

    while True:
        item = await queue.get()
        if item is None:
            break
        elif isinstance(item, Exception):
            raise item
        yield item
