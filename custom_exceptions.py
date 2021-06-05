class StoryNotFoundException(Exception):
    def __init__(self, story_id):
        super(StoryNotFoundException, self).__init__(f"There is no story with id {story_id}")
