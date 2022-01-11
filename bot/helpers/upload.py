import aiohttp
import asyncio
import os

loop = asyncio.get_event_loop()
client_exceptions = (
    aiohttp.ClientResponseError,
    aiohttp.ClientConnectionError,
    aiohttp.ClientPayloadError,
)


async def server_upload(url: str, file: str):
    if os.path.isfile(file) is False:
        raise Exception("File path not found")
    try:
        async with aiohttp.ClientSession() as session:
            files = {'file': open(file, 'rb')}
            response = await session.post(url, data=files)
            responce_json = await response.json()
            return responce_json
    except client_exceptions as e:
        raise Exception(e)
