import asyncio

from .new_topic import NewTopic
from .obstorage import Obstorage


class Broker:
    obstorage: Obstorage

    def __init__(self, obstorage: Obstorage):
        self.obstorage = obstorage

    def start(self):
        pass

    def close(self):
        pass

    async def create_topic(self, new_topic: NewTopic):
        pass

    async def get_topic(self):
        pass

    async def list_topics(self):
        pass
