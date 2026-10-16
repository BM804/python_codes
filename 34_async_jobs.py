"""Distinct Python example #34."""
import asyncio
async def job(i,limit):
 async with limit:await asyncio.sleep(.1);return f"job {i} done"
async def main():print(await asyncio.gather(*(job(i,asyncio.Semaphore(2)) for i in range(6))))
asyncio.run(main())
