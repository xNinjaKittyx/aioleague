
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


@dataclass
class Perks:
    perkStyle: int
    perkIds: List[int]
    perkSubStyle: int

@dataclass
class GameCustomizationObject:
    category: str
    content: str


@dataclass
class CurrentGameParticipant:
    profileIconId: int
    championId: int
    summonerName: str
    gameCustomizationObjects: List[GameCustomizationObject]
    bot: bool
    perks: Perks
    spell2Id: int
    teamId: int
    spell1Id: int
    summonerId: str


@dataclass
class Observer:
    encryptionKey: str


@dataclass
class BannedChampion:
    pickTurn: int
    championId: int
    teamId: int


@dataclass
class CurrentGameInfo:
    gameId: int
    gameStartTime: int
    platformId: str
    gameMode: str
    mapId: int
    gameType: str
    bannedChampions: List[BannedChampion]
    observers: Observer
    participants: List[CurrentGameParticipant]
    gameLength: int
    gameQueueConfigId: int


@dataclass
class Participant:
    profileIconId: int
    championId: int
    summonerName: str
    bot: bool
    spell1Id: int
    teamId: int
    spell2Id: int


