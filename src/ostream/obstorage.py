from typing import Optional

from pydantic import BaseModel, Field


class BucketObstorage(BaseModel):
    pass


class DiskCacheObstorage(BaseModel):
    pass


class MemoryCacheObstorage(BaseModel):
    pass


class Obstorage(BaseModel):
    bucket: BucketObstorage = Field()
    disk_cache: Optional[DiskCacheObstorage] = Field()
    memory_cache: MemoryCacheObstorage = Field()
