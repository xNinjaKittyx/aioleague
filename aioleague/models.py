
from dataclasses import dataclass
from typing import List


@dataclass
class Translation:
    locale: str
    content: str
    updated_at: str


@dataclass
class Message:
    severity: str
    author: str
    created_at: str
    translations: List[Translation]
    updated_at: str
    content: str
    id: str


@dataclass
class Incident:
    id: int
    active: bool
    created_at: str
    updates: List[Message]


@dataclass
class Service:
    status: str
    incidents: List[Incident]
    name: str
    slug: str


@dataclass
class ShardStatus:
    name: str
    region_tag: str
    hostname: str
    services: List[Service]
    slug: str
    locales: List[str]


@dataclass
class SummonerDTO:
    profileIconId: int
    name: str
    puuid: str
    summonerLevel: int
    revisionDate: int
    id: str
    accountId: str
