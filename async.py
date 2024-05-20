"""Using async and await functions.

Will run task function in series since there are no blocking tasks.
"""

import asyncio
import time

TASK_SECONDS = 3


async def task(task_id, task_seconds):
    print(f"{task_id} running")

    for i in range(3):
        await asyncio.sleep(task_seconds)
        print(f"task {task_id}: {i}")

    print(f"{task_id} done")
    return ""


async def running():
    # for i in range(3):
    # await asyncio.create_task(task(i, TASK_SECONDS))

    x = asyncio.create_task(task(1, TASK_SECONDS))
    y = asyncio.create_task(task(2, TASK_SECONDS))
    z = asyncio.create_task(task(3, TASK_SECONDS))

    # For actual benefit of asyncio to work, you need to use await.
    # If await isn't used then the tasks are run in series.
    await x
    await y
    await z

    print("DONE ALL")


if __name__ == "__main__":
    p = time.perf_counter()
    asyncio.run(running())
    duration = time.perf_counter() - p
    print(f"Finished in {duration:0.2f} seconds")
