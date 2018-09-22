"""
Holds the params after the string to translate
"""

from lang.core.parser.helpers import get_text_between_string_tags


class Param:
    sort = None
    item = None
    type = None
    content = None

    def __init__(self, sort=None, item=None):
        self.sort = sort
        self.item = item

        item_type = "text"
        should_split = True

        not_found = -1

        if item.find("comment") != not_found:
            item_type = "comment"
        elif item.find("note") != not_found:
            item_type = "note"
        elif item.find("textdomain") != not_found:
            item_type = "textdomain"
        else:
            should_split = False

        item_content = item

        if should_split:
            parts = item.split("=")
            item_content = parts[1]

        item_content = get_text_between_string_tags(item_content)[0]

        self.type = item_type
        self.content = item_content

    def __repr__(self):
        return self.content
