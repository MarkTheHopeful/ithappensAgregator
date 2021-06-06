from downloader import download_raw_story
from text_processor import process_raw_text
from utils import convert_datetime_to_timestamp, convert_html_to_plaintext
from story import Story


def get_story(story_id: int):
    raw_text = download_raw_story(story_id)
    headline, datetime_text, tags_pairs, story_text, likes_cnt = process_raw_text(raw_text)

    timestamp = convert_datetime_to_timestamp(datetime_text)
    story_text = convert_html_to_plaintext(story_text)

    result_story = Story(story_id, headline, timestamp, tags_pairs, story_text, likes_cnt)
    return result_story


if __name__ == "__main__":

    while True:
        e = input("Enter number:\n")
        story = get_story(int(e))
        print(story.story_text)
