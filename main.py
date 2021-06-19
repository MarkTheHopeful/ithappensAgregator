from story_manager import StoryManager
from database_manager import DatabaseManager
from custom_exceptions import StoryNotFoundException


def download_stories_to_lim(man: StoryManager, lim: int):
    for i in range(1, lim + 1):
        try:
            story_temp = sm.get_story(i)
        except StoryNotFoundException as e:
            print(e)
            break
        except ConnectionError:
            print("Connection failed. There may be no internet connection.")
            break
        print(f"Story {i} downloaded.")


if __name__ == "__main__":
    dm = DatabaseManager()
    # dm.drop_table()
    # dm.create_table()
    sm = StoryManager(dm)

    while True:
        e = input("Enter number:\n")
        if e == "quit":
            print("Exiting...")
            break
        if e == "download":
            lim_s = input("Enter the limit:\n")
            try:
                lim = int(lim_s)
            except ValueError:
                print("Not a story number entered")
                continue
            download_stories_to_lim(sm, lim)
            continue

        try:
            story_id = int(e)
        except ValueError:
            print("Not a story number entered")
            continue

        try:
            story = sm.get_story(story_id)
        except StoryNotFoundException as e:
            print(e)
            continue
        except ConnectionError:  # TODO: Doesn't work sometimes.
            print("Connection failed. There may be no internet connection.")
            continue
        print(story.story_text)
