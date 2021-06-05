from downloader import download_raw_story
from text_processor import process_raw_text

if __name__ == "__main__":

    while True:
        e = input("Enter number:\n")
        raw_text = download_raw_story(int(e))
        process_raw_text(raw_text)