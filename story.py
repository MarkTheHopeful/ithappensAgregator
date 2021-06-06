class Story:
    story_id = 0
    headline = "Empty headline"
    timestamp = 0
    tags_pairs = []
    story_text = "Empty text"
    likes_cnt = 0

    def __init__(self, story_id, headline, timestamp, tags_pairs, story_text, likes_cnt):
        self.story_id = story_id
        self.headline = headline
        self.timestamp = timestamp
        self.tags_pairs = tags_pairs
        self.story_text = story_text
        self.likes_cnt = likes_cnt
