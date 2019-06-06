import asyncio
from random import randint

async def chip_gratis(op):
    while True:
        print(f'Chipe da {op} grátis!')
        await asyncio.sleep(randint(1, 5))
        

async def main():
    anunciantes = asyncio.gather(
            chip_gratis('Claro'), 
            chip_gratis('Tim'), 
            chip_gratis('Vivo'))
            
    await anunciantes
            
            
asyncio.run(main())
