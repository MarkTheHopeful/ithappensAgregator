import requests
from custom_exceptions import StoryNotFoundException

DOWNLOAD_LINK_PREFIX = "https://ithappens.me/story/"


def download_raw_story(story_id: int):
    link = DOWNLOAD_LINK_PREFIX + str(story_id)

    resp = requests.get(link)
    print(resp.raw)  # TODO: Find a way to see the downloaded size
    # sz = int(resp.headers['content-length'])
    # print(f"Size of the story number {story_id}: {sz} bytes.")

    if resp.status_code == 200:
        return resp.text
    elif resp.status_code == 404:
        raise StoryNotFoundException(story_id)
    else:
        print(resp.status_code)
        print(resp.text)
        raise RuntimeError(f"Unexpected status code: {resp.status_code}")
