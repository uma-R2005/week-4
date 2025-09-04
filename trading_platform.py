import asyncio
import threading

async def market_data_feed(updates):
    for i in range(updates):
        await asyncio.sleep(1)
        print(f"Market price update {i}")

def trading_algo():
    print("Running trading algorithm...")

async def trading_platform():
    updates = int(input("Enter number of market updates to simulate: "))
    task = asyncio.create_task(market_data_feed(updates))
    t = threading.Thread(target=trading_algo)
    t.start()
    await task
    t.join()

asyncio.run(trading_platform())
