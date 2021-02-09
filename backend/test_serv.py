import asyncio
import websockets

import json
import math

def calc_pos(rho, phi):
    x = rho*math.cos(math.pi*phi/180)
    y = rho*math.sin(math.pi*phi/180)

    return x, y, 0

#async def save_to_db(data):
#    pass

async def backend_service(websocket, path):
	initial = await websocket.recv()

	data = json.loads(initial)
	print(type(data))

#	b1_phi = data['b1']['phi']
#	b2_phi = data['b2']['phi']
#	b3_phi = data['b3']['phi']

#	b1_rho = data['b1']['rho']
#	b2_rho = data['b2']['rho']
#	b3_rho = data['b3']['rho']

#	while True:
#		b1x, b1y, b1z = calc_pos(b1_rho, b1_phi)
#		b2x, b2y, b2z = calc_pos(b2_rho, b2_phi)
#		b3x, b3y, b3z = calc_pos(b3_rho, b3_phi)

#		b1_phi = 0 if b1_phi >= 360 else b1_phi+2
#		b2_phi = 0 if b2_phi >= 360 else b2_phi+2
#		b3_phi = 0 if b3_phi >= 360 else b3_phi+2

#		data = {
#			"b1": {"x": b1x, "y": b1y, "z": b1z},
#			"b2": {"x": b2x, "y": b2y, "z": b2z},
#			"b3": {"x": b3x, "y": b3y, "z": b3z}
#		}

    #await websocket.send(json.dumps(data))
        # await save_to_db
    #await asyncio.sleep(1/60)

start_server = websockets.serve(backend_service, "localhost", 8001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
