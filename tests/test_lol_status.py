
import pytest


@pytest.mark.asyncio
async def test_get_shard_data(session):
    obj = await session.get_shard_data()
    print(obj)
