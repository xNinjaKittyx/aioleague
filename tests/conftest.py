
import aioleague
import pytest


def pytest_addoption(parser):
    parser.addoption("--api_key", help="LoL Development API Key")


@pytest.fixture()
async def session(request):
    api_key = request.config.getoption('api_key')
    client = aioleague.AIOLeague(api_key)
    yield client
    await client.close()
