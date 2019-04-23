
import aioleague
import pytest


@pytest.mark.asyncio
async def test_summoner_by_account(session: aioleague.AIOLeague) -> None:
    obj = await session.get_summoner_by_name("NinjaKitty")
    obj = await session.get_summoner_by_account_id(obj.accountId)
    assert obj.name == "NinjaKitty"
    print(obj)


@pytest.mark.asyncio
async def test_summoner_by_name(session: aioleague.AIOLeague) -> None:
    obj = await session.get_summoner_by_name("NinjaKitty")
    assert obj.name == "NinjaKitty"
    print(obj)


@pytest.mark.asyncio
async def test_summoner_by_puuid(session: aioleague.AIOLeague) -> None:
    obj = await session.get_summoner_by_name("NinjaKitty")
    obj = await session.get_summoner_by_puuid(obj.puuid)
    assert obj.name == "NinjaKitty"
    print(obj)


@pytest.mark.asyncio
async def test_summoner_by_id(session: aioleague.AIOLeague) -> None:
    obj = await session.get_summoner_by_name("NinjaKitty")
    obj = await session.get_summoner_by_summoner_id(obj.id)
    print(obj)
