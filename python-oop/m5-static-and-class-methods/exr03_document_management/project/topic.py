class Topic:
    def __init__(self, id, topic, storage_folder) -> None:
        self.id = int(id)
        self.topic = str(topic)
        self.storage_folder = str(storage_folder)

    def edit(self, new_topic, new_storage_folder) -> None:
        self.topic = new_topic
        self.storage_folder = new_storage_folder

    def __repr__(self) -> str:
        return f'Topic {self.id}: {self.topic} in {self.storage_folder}'
        