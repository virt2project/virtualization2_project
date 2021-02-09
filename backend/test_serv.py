import asyncio
import websockets
import json
import math


async def save_to_db(data):
    pass

async def backend_service(websocket, path):
	initial = await websocket.recv()

	data = json.loads(initial)
	print(data)
	#await save_to_db
	await asyncio.sleep(1/60)

						

    #await websocket.send(json.dumps(data))



start_server = websockets.serve(backend_service, "localhost", 8001)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
