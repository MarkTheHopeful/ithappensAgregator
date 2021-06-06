from story_manager import StoryManager
from database_manager import DatabaseManager

if __name__ == "__main__":
    dm = DatabaseManager()
    # dm.drop_table()
    # dm.create_table()
    sm = StoryManager(dm)

    while True:
        e = input("Enter number:\n")
        story = sm.get_story(int(e))
        print(story.tags_pairs)

