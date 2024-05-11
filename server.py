
import websockets
import asyncio

clients = []
accounts = {}

async def handler(socket):
    if socket not in clients:
        clients.append(socket)
        name = await socket.recv()
        accounts[socket.remote_address[0]] = name
        print("Connesso nuovo client: " + accounts[socket.remote_address[0]] + " con ip " + socket.remote_address[0])

    async for message in socket:
        websockets.broadcast(clients, accounts[socket.remote_address[0]] + ": " + message)

async def main():
    print("Server in ascolto sulla porta 3033 ... ")
    async with websockets.serve(handler, "0.0.0.0", 3033):
        await asyncio.Future()  # loop infinito

asyncio.run(main())