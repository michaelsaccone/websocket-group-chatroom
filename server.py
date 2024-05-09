
import websockets
import asyncio

async def handler(socket):
    async for message in socket:
        print("ricevuto " + str(message))

async def main():
    print("Server in ascolto sulla porta 3033 ... ")
    async with websockets.serve(handler, "localhost", 3033):
        await asyncio.Future()  # loop infinito

asyncio.run(main())