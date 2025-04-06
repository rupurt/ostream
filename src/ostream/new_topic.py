class NewTopic:
    name: str
    partitions: int

    def __init__(self, name: str, partitions: int):
        self.name = name
        self.partitions = partitions
