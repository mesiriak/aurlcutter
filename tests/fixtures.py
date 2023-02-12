from aurlcutter import Cutter

import pytest

import random, string


@pytest.fixture
async def test_url() -> str:
    test_url = (
        "https://"
        + "".join(random.sample(string.ascii_letters + string.digits, 8))
        + ".com"
    )
    return test_url


@pytest.fixture
async def tiny_cutter() -> Cutter:
    yield Cutter().tinyurl


@pytest.fixture
async def isgd_cutter() -> Cutter:
    yield Cutter().isgd


@pytest.fixture
async def osdb_cutter() -> Cutter:
    yield Cutter().osdb


@pytest.fixture
async def dagd_cutter() -> Cutter:
    yield Cutter().dagd


@pytest.fixture
async def chilpit_cutter() -> Cutter:
    yield Cutter().chilpit
