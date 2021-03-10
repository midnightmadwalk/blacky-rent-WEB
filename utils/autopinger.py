import aiohttp
import socket 

def host():
    host_id = "https://"+socket.getfqdn()
    return host_id
    
async def ping():
    aio_session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
    async with aio_session.get(host()) as response:
       print("✅ online!")
    await aio_session.close()
print("started...")

