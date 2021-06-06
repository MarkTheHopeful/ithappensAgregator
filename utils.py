import ciso8601
import time


def convert_datetime_to_timestamp(datetime_string: str):
    return time.mktime(ciso8601.parse_datetime(datetime_string).timetuple())


def convert_html_to_plaintext(story_text: str):
    story_text = story_text.replace("<p>", "", -1)
    story_text = story_text.replace("</p>", "\n\n", -1)
    story_text = story_text.replace("<br/>", "\n", -1)
    story_text = story_text.strip()
    return story_text
