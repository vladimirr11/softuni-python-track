import sys, os
sys.path.insert(0, os.getcwd())

from exr03_document_management.project.category import Category
from exr03_document_management.project.topic import Topic
from exr03_document_management.project.document import Document


class Storage:
    def __init__(self) -> None:
        self.categories = list()
        self.topics = list()
        self.documents = list()
    
    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for category in self.categories:
            if category.id == category_id:
                category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_strorage_folder):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.edit(new_topic, new_strorage_folder)

    def edit_document(self, document_id, new_file_name):
        for document in self.documents:
            if document.id == document_id:  
                document.edit(new_file_name)

    def delete_category(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                self.categories.remove(category)

    def delete_topic(self, topic_id):
        for top in self.topics:
            if top.id == topic_id:
                self.topics.remove(top)

    def delete_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                self.documents.remove(doc)

    def get_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return doc

    def __repr__(self) -> str:
        for doc in self.documents:
            return doc.__repr__()


if __name__ == '__main__':
    c1 = Category(1, "work")
    t1 = Topic(1, "daily tasks", "C:\\work_documents")
    d1 = Document(1, 1, 1, "finilize project")

    d1.add_tag("urgent")
    d1.add_tag("work")

    storage = Storage()
    storage.add_category(c1)
    storage.add_topic(t1)
    storage.add_document(d1)

    print(c1)
    print(t1)
    print(storage.get_document(1))
    print(storage)
