import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:

        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
        async with session.get(pokemon_url) as resp:
            pokemon = await resp.json()
            print(pokemon['name'])

async def main2():
    session = aiohttp.ClientSession()
    pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
    resp = await session.get(pokemon_url)
    pokemon = await resp.json()
    print(pokemon['name'])
    print("resp:", resp)
    print("session:", session)
    resp.close()
    print("resp:", resp)
    await session.close()
    print("session:", session)

asyncio.run(main2())

print("end")
