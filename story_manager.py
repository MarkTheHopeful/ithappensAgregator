from text_processor import process_raw_text
from utils import convert_datetime_to_timestamp, convert_html_to_plaintext
from story import Story
from downloader import download_raw_story


def download_story(story_id: int):
    raw_text = download_raw_story(story_id)
    headline, datetime_text, tags_pairs, story_text, likes_cnt = process_raw_text(raw_text)

    timestamp = convert_datetime_to_timestamp(datetime_text)
    story_text = convert_html_to_plaintext(story_text)

    result_story = Story(story_id, headline, timestamp, tags_pairs, story_text, likes_cnt)
    return result_story


class StoryManager:
    storage = dict()  # TODO: replace with db

    def __init__(self):
        storage = dict()

    def get_story(self, story_id):
        story = None
        if story_id not in self.storage.keys():
            story = download_story(story_id)
            self.storage[story_id] = story
        else:
            story = self.storage[story_id]
        return story
