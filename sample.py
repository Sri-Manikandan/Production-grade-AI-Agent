# import asyncio

# async def task():
#     await asyncio.sleep(4)
#     print("Done")

# async def hi():
#     await asyncio.sleep(2)
#     print("Hi")

# async def main():
#     await asyncio.gather(task(),hi())

# asyncio.run(main())
import asyncio

async def download(name, seconds):
    print(f"Start {name}")
    await asyncio.sleep(seconds)
    print(f"End {name}")

async def main():
    await asyncio.gather(
        download("A", 2),
        download("B", 1),
        download("C", 3)
    )

asyncio.run(main())
