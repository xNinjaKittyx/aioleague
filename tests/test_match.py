
import aioleague
import pytest


@pytest.mark.asyncio
async def test_match(session: aioleague.AIOLeague) -> None:
    summoner = await session.get_summoner_by_name("NinjaKitty")
    get_matches = await session.get_matchlist(summoner.accountId, end_index=1)
    match = await session.get_match(get_matches.matches[0].gameId)
    print(match)


@pytest.mark.asyncio
async def test_matchlist(session: aioleague.AIOLeague) -> None:
    summoner = await session.get_summoner_by_name("xlikeabossx")
    get_matches = await session.get_matchlist(summoner.accountId, end_index=1)
    print(get_matches)


@pytest.mark.asyncio
async def test_match_timeline(session: aioleague.AIOLeague) -> None:
    summoner = await session.get_summoner_by_name("ebacho")
    get_matches = await session.get_matchlist(summoner.accountId, end_index=1)
    timeline = await session.get_match_timeline(get_matches.matches[0].gameId)
    print(timeline)
