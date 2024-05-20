"""Using async and await functions.

Will run task function in series since there are no blocking tasks.
"""

import time

TASK_SECONDS = 3


def task(task_id, task_seconds):
    print(f"{task_id} running")

    for i in range(3):
        time.sleep(task_seconds)
        print(f"task {task_id}: {i}")

    print(f"{task_id} done")
    return ""


def running():
    # for i in range(3):
    # await asyncio.create_task(task(i, TASK_SECONDS))

    task(1, TASK_SECONDS)
    task(2, TASK_SECONDS)
    task(3, TASK_SECONDS)

    print("DONE ALL")


if __name__ == "__main__":
    p = time.perf_counter()
    running()
    duration = time.perf_counter() - p
    print(f"Finished in {duration:0.2f} seconds")
