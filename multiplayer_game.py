import asyncio
import threading

async def player_updates(player_id, steps):
    for i in range(steps):
        await asyncio.sleep(1)
        print(f"Player {player_id} moved at step {i}")

def game_physics():
    print("Physics engine calculating collisions...")

async def game():
    players = int(input("Enter number of players: "))
    steps = int(input("Enter number of moves: "))
    tasks = [player_updates(i+1, steps) for i in range(players)]
    await asyncio.gather(*tasks)

    t = threading.Thread(target=game_physics)
    t.start()
    t.join()

asyncio.run(game())
