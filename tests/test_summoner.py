
import aioleague
import pytest


@pytest.mark.asyncio
async def test_summoner_by_account(session: aioleague.AIOLeague) -> None:
    obj = await session.get_summoner_by_account_id('vW_50hPY0c-wwjgIyChX0l24hzruWHKQYGNtBII2oh_k4g')
    assert obj.name == "NinjaKitty"
    print(obj)


@pytest.mark.asyncio
async def test_summoner_by_name(session: aioleague.AIOLeague) -> None:
    obj = await session.get_summoner_by_name("NinjaKitty")
    assert obj.name == "NinjaKitty"
    print(obj)


@pytest.mark.asyncio
async def test_summoner_by_puuid(session: aioleague.AIOLeague) -> None:
    obj = await session.get_summoner_by_puuid('5Y_BrTtFy5dzNdoLDaRqtzBuIZH3rBSWoh-Xnj7XxNfHH47VlVzTIhYXw7I9Elo5rjbsNw4rbbggog')
    assert obj.name == "NinjaKitty"
    print(obj)


@pytest.mark.asyncio
async def test_summoner_by_id(session: aioleague.AIOLeague) -> None:
    obj = await session.get_summoner_by_summoner_id('Pbxea0Yt9gdSc5mnEz6ZsFSL6r7wdTz0XsSnv3OcumPN8OQ')
    print(obj)
