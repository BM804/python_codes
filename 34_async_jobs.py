"""Run asynchronous jobs with a shared concurrency limit."""
import asyncio

async def job(number: int, semaphore: asyncio.Semaphore):
    async with semaphore:
        print(f"Job {number} started")
        await asyncio.sleep(0.1)
        return f"Job {number} finished"

async def main():
    limit = asyncio.Semaphore(2)
    results = await asyncio.gather(*(job(number, limit) for number in range(6)))
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
