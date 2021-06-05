import requests
from custom_exceptions import StoryNotFoundException

DOWNLOAD_LINK_PREFIX = "https://ithappens.me/story/"


def download_raw_story(story_id: int):
    link = DOWNLOAD_LINK_PREFIX + str(story_id)

    resp = requests.get(link)

    if resp.status_code == 200:
        return resp.text
    elif resp.status_code == 404:
        raise StoryNotFoundException(story_id)
    else:
        print(resp.status_code)
        print(resp.text)
        raise RuntimeError(f"Unexpected status code: {resp.status_code}")


if __name__ == "__main__":

    while True:
        e = input("Enter number:\n")
        print(download_raw_story(int(e)))
