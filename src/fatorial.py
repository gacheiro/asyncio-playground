import asyncio
from random import randint

# funciona, mas não sei se o controle é passado corretamente
# pras corrotinas

async def asyncrange(a, b):
    # um range assincrono
    for i in range(a, b):
        await asyncio.sleep(1)
        yield i
        

async def fat(n):
    f = 1
    async for i in asyncrange(1, n+1):
        print(f'Calculando o fatorial de {i}..{n}')
        f *= i        
    return f
        
        
async def main():

    future_fats = asyncio.gather(fat(5), fat(6), fat(7))
    
    f5, f6, f7 = await future_fats # espera as corrotinas terminarem
    
    print(f"fat(5) = {f5}")
    print(f"fat(6) = {f6}")
    print(f"fat(7) = {f7}")
    
    
asyncio.run(main())
