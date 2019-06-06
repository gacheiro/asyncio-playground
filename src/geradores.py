import asyncio


async def g():
    yield "Hello"
    await asyncio.sleep(5)
    yield "World"
    
    
async def main():
    async for w in g(): # isso aqui funciona?
        print(w)
    
    
asyncio.run(main())
