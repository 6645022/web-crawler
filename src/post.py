from metadata import Metadata
from date import Date


class Post:
    author = Metadata()
    title = Metadata()
    date = Date()

    def __init__(self, author, title, content, date):
        self.author = author
        self.title = title
        self.content = content
        self.date = date

    @property
    def content(self):
        return self.content

    @content.setter
    def content(self, value):
        self._content = value.strip().rstrip()

    def get_post(self):
        post = dict()
        post['author'] = self.author
        post['title'] = self.title
        post['content'] = self.content
        post['date'] = self.date
        return post
