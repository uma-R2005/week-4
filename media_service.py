import asyncio
import threading

async def stream_video(chunks):
    for i in range(chunks):
        await asyncio.sleep(1)
        print(f"Streaming chunk {i}")

def transcode_video():
    print("Transcoding video to lower resolution...")

async def media_service():
    chunks = int(input("Enter number of video chunks to stream: "))
    task = asyncio.create_task(stream_video(chunks))
    t = threading.Thread(target=transcode_video)
    t.start()
    await task
    t.join()

asyncio.run(media_service())
