from enum import Enum
import os


class MetadataEnum(Enum):
    def __str__(self):
        return str(self.value)
    sec = 1
    min = 60
    hour = 60 * 60
    hours = 60 * 60


def extract_published_time(time):
    time_list = time.split(' ')
    time = MetadataEnum[time_list[1]].value
    return int(time_list[0]) * time


def check_post_published_time(time):
    published_time_sec = extract_published_time(time)
    return True if published_time_sec < int(os.environ.get("published_time_threshold")) else False
