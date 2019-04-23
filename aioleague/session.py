
from typing import Optional, Union

import aiohttp
from dacite import from_dict

from .models import (
    ChampionInfo,
    CurrentGameInfo,
    FeaturedGames,
    MatchDTO,
    MatchlistDTO,
    MatchReferenceDTO,
    MatchTimelineDTO,
    ShardStatus,
    SummonerDTO,
)


class AIOLeague:
    regions = ["NA1", "RU", "KR", "PBE1", "BR1", "OC1", "JP1", "EUN1", "EUW1", "TR1", "LA1", "LA2"]

    def __init__(self, api_key: str, region: str = "NA1", aiohttp_client: Optional[aiohttp.ClientSession] = None):
        self.region = region
        if aiohttp_client is None:
            self._client = aiohttp.ClientSession(raise_for_status=True)
        else:
            self._client = aiohttp_client

        self._client._default_headers.update({
            'X-Riot-Token': api_key
        })

    async def close(self):
        await self._client.close()

    @property
    def region(self) -> str:
        return self._region

    @region.setter
    def region(self, value: str) -> None:
        if value not in self.regions:
            raise ValueError('Invalid Region')
        self._region = value

    @property
    def endpoint(self) -> str:
        return f"https://{self.region}.api.riotgames.com"

    async def get_all_champion_masteries(self, summoner_id: str):
        raise NotImplementedError

    async def get_champion_mastery(self, summoner_id: str, champion_id: str):
        raise NotImplementedError

    async def get_total_mastery_score(self, summoner_id: str):
        raise NotImplementedError

    async def get_champion_rotation(self) -> ChampionInfo:
        async with self._client.get(f"{self.endpoint}/lol/platform/v3/champion-rotations") as r:
            result = await r.json()
        return from_dict(data_class=ChampionInfo, data=result)

    async def get_challenger_leagues(self, queue: str):
        raise NotImplementedError

    async def get_league_entries_by_summoner(self, summoner_id: str):
        raise NotImplementedError

    async def get_league_entries(self, queue: str, tier: str, division: str):
        raise NotImplementedError

    async def get_grandmaster_league(self, queue: str):
        raise NotImplementedError

    async def get_league_by_id(self, league_id: str):
        raise NotImplementedError

    async def get_master_league(self, queue: str):
        raise NotImplementedError

    async def get_shard_data(self) -> ShardStatus:
        async with self._client.get(f"{self.endpoint}/lol/status/v3/shard-data") as r:
            result = await r.json()
        return from_dict(data_class=ShardStatus, data=result)

    async def get_match(self, match: Union[MatchReferenceDTO, int]) -> MatchDTO:
        if isinstance(match, MatchReferenceDTO):
            match_id = match.gameId
        elif isinstance(match, int):
            match_id = match
        else:
            raise ValueError(f'Invalid match type: {type(match)}')
        async with self._client.get(f"{self.endpoint}/lol/match/v4/matches/{match_id}") as r:
            result = await r.json()
        return from_dict(data_class=MatchDTO, data=result)

    async def get_matchlist(
        self,
        account_id: str,
        champion: int = None,
        queue: int = None,
        season: int = None,
        end_time: int = None,
        begin_time: int = None,
        end_index: int = None,
        begin_index: int = None
    ) -> MatchlistDTO:
        params = {}
        if champion is not None:
            params['champion'] = champion
        if queue is not None:
            params['queue'] = queue
        if season is not None:
            params['season'] = season
        if end_time is not None:
            params['endTime'] = end_time
        if begin_time is not None:
            params['beginTime'] = begin_time
        if end_index is not None:
            params['endIndex'] = end_index
        if begin_index is not None:
            params['beginIndex'] = begin_index

        async with self._client.get(f"{self.endpoint}/lol/match/v4/matchlists/by-account/{account_id}", params=params) as r:
            result = await r.json()
        return from_dict(data_class=MatchlistDTO, data=result)

    async def get_match_timeline(self, match_id: str) -> MatchTimelineDTO:
        async with self._client.get(f"{self.endpoint}/lol/match/v4/timelines/by-match/{match_id}") as r:
            result = await r.json()
        return from_dict(data_class=MatchTimelineDTO, data=result)

    async def get_match_by_tournament(self, tournament_code: str, match_id: Optional[str] = None):
        pass

    async def get_current_game(self, summoner_id: str) -> CurrentGameInfo:
        async with self._client.get(f"{self.endpoint}/lol/spectator/v4/active-games/by-summoner/{summoner_id}") as r:
            result = await r.json()
        return from_dict(data_class=CurrentGameInfo, data=result)

    async def get_featured_games(self) -> FeaturedGames:
        async with self._client.get(f"{self.endpoint}/lol/spectator/v4/featured-games") as r:
            result = await r.json()
        return from_dict(data_class=FeaturedGames, data=result)

    async def get_summoner_by_account_id(self, account_id: str) -> SummonerDTO:
        async with self._client.get(f"{self.endpoint}/lol/summoner/v4/summoners/by-account/{account_id}") as r:
            result = await r.json()
        return from_dict(data_class=SummonerDTO, data=result)

    async def get_summoner_by_name(self, name: str) -> SummonerDTO:
        async with self._client.get(f"{self.endpoint}/lol/summoner/v4/summoners/by-name/{name}") as r:
            result = await r.json()
        return from_dict(data_class=SummonerDTO, data=result)

    async def get_summoner_by_puuid(self, puuid: str) -> SummonerDTO:
        async with self._client.get(f"{self.endpoint}/lol/summoner/v4/summoners/by-puuid/{puuid}") as r:
            result = await r.json()
        return from_dict(data_class=SummonerDTO, data=result)

    async def get_summoner_by_summoner_id(self, summoner_id: str) -> SummonerDTO:
        async with self._client.get(f"{self.endpoint}/lol/summoner/v4/summoners/{summoner_id}") as r:
            result = await r.json()
        return from_dict(data_class=SummonerDTO, data=result)
