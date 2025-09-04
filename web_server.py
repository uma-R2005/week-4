import asyncio
import threading

async def handle_request(client_id):
    await asyncio.sleep(1)  
    print(f"Handled request from visitor {client_id}")

def cpu_heavy_task():
    total = sum(i*i for i in range(10_000))
    print("CPU task finished (encryption done)")

async def main():
    n = int(input("Enter number of website visitors: "))
    tasks = [handle_request(i+1) for i in range(n)]
    await asyncio.gather(*tasks)

    thread = threading.Thread(target=cpu_heavy_task)
    thread.start()
    thread.join()

asyncio.run(main())

