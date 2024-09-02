from typing import Generator
from screenpy import AnActor
from screenpy_requests.abilities import MakeAPIRequests

import pytest
import requests

@pytest.fixture(scope="function")
def usuario() -> Generator:
    the_actor = AnActor\
        .named("usuario")\
        .who_can(MakeAPIRequests())\

    yield the_actor
    the_actor.exit()
