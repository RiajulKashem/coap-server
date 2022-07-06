import asyncio

from aiocoap import *


async def main():
    context = await Context.create_client_context()
    payload = b"sending from local client"

    request = Message(code=POST, payload=payload, uri="coap://localhost/m")

    response = await context.request(request).response
    print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())