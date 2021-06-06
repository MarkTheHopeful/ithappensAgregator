from database_manager import DatabaseManager
from text_processor import process_raw_text
from utils import convert_datetime_to_timestamp, convert_html_to_plaintext
from story import Story, init_from_tuple
from downloader import download_raw_story


def download_story(story_id: int):
    raw_text = download_raw_story(story_id)
    headline, datetime_text, tags_pairs, story_text, likes_cnt = process_raw_text(raw_text)

    timestamp = convert_datetime_to_timestamp(datetime_text)
    story_text = convert_html_to_plaintext(story_text)

    result_story = Story(story_id, headline, timestamp, tags_pairs, story_text, likes_cnt)
    return result_story


class StoryManager:
    storage = None

    def __init__(self, db_manager: DatabaseManager):
        self.storage = db_manager

    def get_story(self, story_id):
        story = None
        story_data = self.storage.get_story(story_id)
        if not story_data:
            story = download_story(story_id)
            self.storage.insert_story(story.get_tuple())
        else:
            story = init_from_tuple(*story_data)

        return story
