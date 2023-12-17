import aiohttp


async def get_body(x):
     async with aiohttp.ClientSession() as session:
        async with session.get(x) as resp:
            status_code = resp.status
            print(status_code)
            return await resp.content.read()
        

