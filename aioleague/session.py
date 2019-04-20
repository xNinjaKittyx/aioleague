
from typing import Optional, Set

import aiohttp
from dacite import from_dict

from .models import (
    Translation,
    Message,
    Incident,
    Service,
    ShardStatus,
    SummonerDTO
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
        pass

    async def get_champion_mastery(self, summoner_id: str, champion_id: str):
        pass

    async def get_total_mastery_score(self, summoner_id: str):
        pass

    async def get_champion_rotation(self):
        pass

    async def get_challenger_leagues(self, queue: str):
        pass

    async def get_league_entries_by_summoner(self, summoner_id: str):
        pass

    async def get_league_entries(self, queue: str, tier: str, division: str):
        pass

    async def get_grandmaster_league(self, queue: str):
        pass

    async def get_league_by_id(self, league_id: str):
        pass

    async def get_master_league(self, queue: str):
        pass

    async def get_shard_data(self) -> ShardStatus:
        async with self._client.get(f"{self.endpoint}/lol/status/v3/shard-data") as r:
            result = await r.json()
        return from_dict(data_class=ShardStatus, data=result)

    async def get_match(self, match_id: str):
        pass

    async def get_matchlist(
        self,
        account_id: str,
        champion: Set[int] = None,
        queue: Set[int] = None,
        season: Set[int] = None,
        end_time: int = None,
        begin_time: int = None,
        end_index: int = None,
        begin_index: int = None
    ):
        pass

    async def get_match_timeliine(self, match_id: str):
        pass

    async def get_match_by_tournament(self, tournament_code: str, match_id: Optional[str] = None):
        pass

    async def get_current_game(self, summoner_id: str):
        pass

    async def get_featured_games(self):
        pass

    async def get_summoner_by_account_id(self, account_id: str):
        async with self._client.get(f"{self.endpoint}/lol/summoner/v4/summoners/by-account/{account_id}") as r:
            result = await r.json()
        return from_dict(data_class=SummonerDTO, data=result)

    async def get_summoner_by_name(self, name: str):
        async with self._client.get(f"{self.endpoint}/lol/summoner/v4/summoners/by-name/{name}") as r:
            result = await r.json()
        return from_dict(data_class=SummonerDTO, data=result)

    async def get_summoner_by_puuid(self, puuid: str):
        async with self._client.get(f"{self.endpoint}/lol/summoner/v4/summoners/by-puuid/{puuid}") as r:
            result = await r.json()
        return from_dict(data_class=SummonerDTO, data=result)

    async def get_summoner_by_summoner_id(self, summoner_id: str):
        async with self._client.get(f"{self.endpoint}/lol/summoner/v4/summoners/{summoner_id}") as r:
            result = await r.json()
        return from_dict(data_class=SummonerDTO, data=result)
