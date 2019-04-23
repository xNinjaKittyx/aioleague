# aioleague
Asyncio Python API Bindings for League of Legends API.


Supported for Python 3.6+


# Installation

```
pip install git+https://github.com/xNinjaKittyx/aioleague.git
```

# Basic Usage

```
import asyncio
import aioleague


async def sample(api_key):
    client = aioleague.AIOLeague(api_key)
    summoner = await session.get_summoner_by_name("NinjaKitty")
    current_game = await get_current_game(self, summoner.id)

    print(current_game)


asyncio.get_event_loop.run_until_complete(sample("YOUR API KEY"))

```

# Useful Links:

Riot's Full API Documentation: https://developer.riotgames.com/api-methods/
