from story_manager import StoryManager

if __name__ == "__main__":
    sm = StoryManager()
    while True:
        e = input("Enter number:\n")
        story = sm.get_story(int(e))
        print(story.story_text)
