
import aioleague
import pytest


@pytest.mark.asyncio
async def test_featured_games(session: aioleague.AIOLeague) -> None:
    obj = await session.get_featured_games()
    print(obj)


@pytest.mark.asyncio
async def test_current_game(session: aioleague.AIOLeague) -> None:
    featured_games = await session.get_featured_games()
    name = featured_games.gameList[0].participants[0].summonerName
    summoner = await session.get_summoner_by_name(name)
    current_game = await session.get_current_game(summoner.id)
    print(current_game)
