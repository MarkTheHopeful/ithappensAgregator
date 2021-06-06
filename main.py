from story_manager import StoryManager
from database_manager import DatabaseManager
from custom_exceptions import StoryNotFoundException

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
        except ConnectionError:
            print("Connection failed. There may be no internet connection.")
            continue
        print(story.tags_pairs)
