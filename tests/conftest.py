import asyncio

import httpx
import pytest

pytest_plugins = ["tests.fixtures"]


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def client():
    async with httpx.AsyncClient() as client:
        yield client
