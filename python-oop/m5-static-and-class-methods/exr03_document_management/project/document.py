from exr03_document_management.project.category import Category
from exr03_document_management.project.topic import Topic


class Document:
    def __init__(self, id, category_id, topic_id, file_name) -> None:
        self.id = int(id)
        self.category_id = int(category_id)
        self.topic_id = int(topic_id)
        self.file_name = str(file_name)
        self.tags = list()

    @classmethod
    def from_instances(cls, id, category: Category, topic: Topic, file_name):
        return cls(id, category.id, topic.id, file_name)

    def add_tag(self, tag_content) -> None:
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content) -> None:
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, file_name) -> None:
        self.file_name = file_name

    def __repr__(self) -> str:
        return f'Document {self.id}: {self.file_name}; category {self.category_id}, ' \
            f'topic {self.topic_id}, tags: {", ".join([tag for tag in self.tags])}'
