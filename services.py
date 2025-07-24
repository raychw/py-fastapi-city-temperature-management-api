import aiohttp


async def fetch_temperature(city_name: str) -> float:
    async with aiohttp.ClientSession() as session:
        return 25.0 + hash(city_name) % 10
