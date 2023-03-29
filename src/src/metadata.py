from metadataEnum import MetadataEnum


class Metadata:
    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        if self._name in MetadataEnum.__members__:
            value = ''
        self._name = value

    def __get__(self, instance, owner):
        return self._name
