import asyncio
import threading

async def receive_messages(name, count):
    for i in range(count):
        await asyncio.sleep(1)
        print(f"{name} received message {i}")

def save_to_db(message):
    print(f"Saving '{message}' to database...")

async def chat():
    name = input("Enter chat username: ")
    msg = input("Enter a message: ")
    count = int(input("How many messages to simulate receiving? "))

    asyncio.create_task(receive_messages(name, count))
    thread = threading.Thread(target=save_to_db, args=(msg,))
    thread.start()
    await asyncio.sleep(count + 1)

asyncio.run(chat())
