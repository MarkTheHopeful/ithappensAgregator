import re

base_story_re = re.compile(r"<h1 itemprop=\"headline\">.*<div class='rating'>\d+</div>", re.M | re.S)
headline_re = re.compile(r"(<h1 itemprop=\"headline\">)(.*)(</h1>)", re.M | re.S)
datetime_re = re.compile(r"(datetime=')(.*)(' itemprop='datePublished')", re.M | re.S)
date_published_re = re.compile(r"('datePublished'>)(.*)(</time>)", re.M | re.S)
tags_re = re.compile(r"(<li><a href=\"/tag/(\w+)\" itemprop=\"about\">(\w+)</a></li>)+", re.M | re.S | re.U)
text_re = re.compile(r"(<div class='text' itemprop='articleBody'>\n)(.*)(</div>.<!-- noindex -->)", re.M | re.S)
likes_re = re.compile(r"(<div class='rating'>)(\d+)(</div>)", re.M | re.S)


def process_raw_text(raw_page_text: str):
    processing_page_text = base_story_re.search(raw_page_text)[0]

    headline_text = headline_re.search(processing_page_text).group(2)

    datetime_text = datetime_re.search(processing_page_text).group(2)

    date_published_text = date_published_re.search(processing_page_text).group(2)

    tags_raw_strings = tags_re.findall(processing_page_text)
    tags_pairs = [[tag_string[1], tag_string[2]] for tag_string in tags_raw_strings]

    story_text = text_re.search(processing_page_text).group(2)

    likes_cnt = int(likes_re.search(processing_page_text).group(2))

    return [headline_text, datetime_text, date_published_text, tags_pairs, story_text, likes_cnt]
