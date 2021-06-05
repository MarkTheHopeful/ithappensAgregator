import requests

DOWNLOAD_LINK_PREFIX = "https://ithappens.me/story/"


def download_raw_story(story_id):
    link = DOWNLOAD_LINK_PREFIX + str(story_id)

    resp = requests.get(link)
    print(resp.status_code)
    print(resp.text)


if __name__ == "__main__":

    while True:
        e = input("Enter number:\n")
        download_raw_story(e)
