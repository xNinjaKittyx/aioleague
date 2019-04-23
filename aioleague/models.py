
from dataclasses import dataclass
from typing import Dict, List, Optional


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


@dataclass
class FeaturedGameInfo:
    gameId: int
    gameStartTime: int
    platformId: str
    gameMode: str
    mapId: int
    gameType: str
    bannedChampions: List[BannedChampion]
    observers: Observer
    participants: List[Participant]
    gameLength: int
    gameQueueConfigId: int


@dataclass
class FeaturedGames:
    clientRefreshInterval: int
    gameList: List[FeaturedGameInfo]


@dataclass
class MasteryDTO:
    masteryId: int
    rank: int


@dataclass
class ParticipantTimelineDTO:
    lane: str
    participantId: int
    csDiffPerMinDeltas: Optional[Dict[str, float]]
    goldPerMinDeltas: Optional[Dict[str, float]]
    xpDiffPerMinDeltas: Optional[Dict[str, float]]
    creepsPerMinDeltas: Optional[Dict[str, float]]
    xpPerMinDeltas: Optional[Dict[str, float]]
    role: str
    damageTakenDiffPerMinDeltas: Optional[Dict[str, float]]
    damageTakenPerMinDeltas: Optional[Dict[str, float]]


@dataclass
class RuneDTO:
    runId: int
    rank: int

@dataclass
class ParticipantStatsDTO:
    firstBloodAssist: bool
    visionScore: int
    magicDamageDealtToChampions: int
    damageDealtToObjectives: int
    totalTimeCrowdControlDealt: int
    longestTimeSpentLiving: int
    perk1Var1: int
    perk1Var3: int
    perk1Var2: int
    tripleKills: int
    perk3Var3: int
    nodeNeutralizeAssist: Optional[int]
    perk3Var2: int
    playerScore9: int
    playerScore8: int
    kills: int
    playerScore1: int
    playerScore0: int
    playerScore3: int
    playerScore2: int
    playerScore5: int
    playerScore4: int
    playerScore7: int
    playerScore6: int
    perk5Var1: int
    perk5Var3: int
    perk5Var2: int
    totalScoreRank: int
    neutralMinionsKilled: int
    damageDealtToTurrets: int
    physicalDamageDealtToChampions: int
    nodeCapture: Optional[int]
    largestMultiKill: int
    perk2Var2: int
    perk2Var3: int
    totalUnitsHealed: int
    perk2Var1: int
    perk4Var1: int
    perk4Var2: int
    perk4Var3: int
    wardsKilled: int
    largestCriticalStrike: int
    largestKillingSpree: int
    quadraKills: int
    teamObjective: Optional[int]
    magicDamageDealt: int
    item2: int
    item3: int
    item0: int
    neutralMinionsKilledTeamJungle: int
    item6: int
    item4: int
    item5: int
    perk1: int
    perk0: int
    perk3: int
    perk2: int
    perk5: int
    perk4: int
    perk3Var1: int
    damageSelfMitigated: int
    magicalDamageTaken: int
    firstInhibitorKill: bool
    trueDamageTaken: int
    nodeNeutralize: Optional[int]
    assists: int
    combatPlayerScore: int
    perkPrimaryStyle: int
    goldSpent: int
    trueDamageDealt: int
    participantId: int
    totalDamageTaken: int
    physicalDamageDealt: int
    sightWardsBoughtInGame: int
    totalDamageDealtToChampions: int
    physicalDamageTaken: int
    totalPlayerScore: int
    win: bool
    objectivePlayerScore: int
    totalDamageDealt: int
    item1: int
    neutralMinionsKilledEnemyJungle: int
    deaths: int
    wardsPlaced: int
    perkSubStyle: int
    turretKills: int
    firstBloodKill: bool
    trueDamageDealtToChampions: int
    goldEarned: int
    killingSprees: int
    unrealKills: int
    altarsCaptured: Optional[int]
    firstTowerAssist: bool
    firstTowerKill: bool
    champLevel: int
    doubleKills: int
    nodeCaptureAssist: Optional[int]
    inhibitorKills: int
    firstInhibitorAssist: bool
    perk0Var1: int
    perk0Var2: int
    perk0Var3: int
    visionWardsBoughtInGame: int
    altarsNeutralized: Optional[int]
    pentaKills: int
    totalHeal: int
    totalMinionsKilled: int
    timeCCingOthers: int


@dataclass
class ParticipantDTO:
    stats: ParticipantStatsDTO
    participantId: int
    runes: Optional[List[RuneDTO]]
    timeline: ParticipantTimelineDTO
    teamId: int
    spell2Id: int
    masteries: Optional[List[MasteryDTO]]
    highestAchievedSeasonTier: Optional[str]
    spell1Id: int
    championId: int


@dataclass
class TeamBansDTO:
    pickTurn: int
    championId: int


@dataclass
class TeamStatsDTO:
    firstDragon: bool
    firstInhibitor: bool
    bans: List[TeamBansDTO]
    baronKills: int
    firstRiftHerald: bool
    firstBaron: bool
    riftHeraldKills: int
    firstBlood: bool
    teamId: int
    firstTower: bool
    vilemawKills: int
    inhibitorKills: int
    towerKills: int
    dominionVictoryScore: int
    win: str
    dragonKills: int


@dataclass
class PlayerDTO:
    currentPlatformId: str
    summonerName: str
    matchHistoryUri: str
    platformId: str
    currentAccountId: str
    profileIcon: int
    summonerId: str
    accountId: str


@dataclass
class ParticipantIdentityDTO:
    player: PlayerDTO
    participantId: int


@dataclass
class MatchDTO:
    seasonId: int
    queueId: int
    gameId: int
    participantIdentities: List[ParticipantIdentityDTO]
    gameVersion: str
    platformId: str
    gameMode: str
    mapId: int
    gameType: str
    teams: List[TeamStatsDTO]
    participants: List[ParticipantDTO]
    gameDuration: int
    gameCreation: int


@dataclass
class MatchReferenceDTO:
    lane: str
    gameId: int
    champion: int
    platformId: str
    season: int
    queue: int
    role: str
    timestamp: int


@dataclass
class MatchlistDTO:
    matches: List[MatchReferenceDTO]
    totalGames: int
    startIndex: int
    endIndex: int


@dataclass
class MatchPositionDTO:
    x: int
    y: int


@dataclass
class MatchEventDTO:
    eventType: Optional[str]
    towerType: Optional[str]
    teamId: Optional[int]
    ascendedType: Optional[str]
    killerId: Optional[int]
    levelUpType: Optional[str]
    pointCaptured: Optional[str]
    assistingParticipantIds: Optional[List[int]]
    wardType: Optional[str]
    monsterType: Optional[str]
    type: str
    skillSlot: Optional[int]
    victimId: Optional[int]
    timestamp: int
    afterId: Optional[int]
    monsterSubType: Optional[str]
    laneType: Optional[str]
    itemId: Optional[int]
    participantId: Optional[int]
    buildingType: Optional[str]
    creatorId: Optional[int]
    position: Optional[MatchPositionDTO]
    beforeId: Optional[int]


@dataclass
class MatchParticipantFrameDTO:
    totalGold: int
    teamScore: Optional[int]
    participantId: int
    level: int
    currentGold: int
    minionsKilled: int
    dominionScore: Optional[int]
    position: Optional[MatchPositionDTO]
    xp: int
    jungleMinionsKilled: int


@dataclass
class MatchFrameDTO:
    timestamp: int
    participantFrames: Dict[str, MatchParticipantFrameDTO]
    events: List[MatchEventDTO]


@dataclass
class MatchTimelineDTO:
    frames: List[MatchFrameDTO]
    frameInterval: int


@dataclass
class ChampionInfo:
    freeChampionIdsForNewPlayers: List[int]
    freeChampionIds: List[int]
    maxNewPlayerLevel: int
