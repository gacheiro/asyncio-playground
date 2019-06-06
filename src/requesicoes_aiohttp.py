import asyncio
import aiohttp


URLS = ['http://uern.br', 'http://di.uern.br', 'http://ufersa.edu.br']


async def fetch(session, url):
    async with session.get(url) as response:
        # indo buscar a página, pode ir fazer outra coisa por enquanto
        return await response.text()

        
async def main():
    async with aiohttp.ClientSession() as session:
        pages = await asyncio.gather(*(fetch(session, url) for url in URLS))
        
        # faz alguma coisa com as páginas
        ...
        

asyncio.run(main())
