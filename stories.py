"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

medieval = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

modern = Story(
    ["city", "famous_building", "clothing_item", "number"],
    """This summer, I went to {city}, and had a blast visiting the {famous_building}!  I just wish it wasn't {number} degrees when I went; I had to wear a {clothing_item} the entire time...."""
)

futuristic = Story(
    ["celestial_body", "tiny_insects", "number", "adjective", "person", 'breakfast_food'],
    """On the distant planet of {celestial_body}, there lived a
       group of large, {adjective} {tiny_insects}. We were at war with them for {number} days.  We were just lucky to have had {person} on our side.  Without them, the human race would have become the {breakfast_food} of the galaxy!"""
)


stories_dict = {
    0: 'Medieval',
    1: 'Modern',
    2: 'Futuristic',
    # 'Medieval': medieval,
    # 'Modern': modern,
    # 'Futuristic': futuristic,
}
stories = [medieval, modern, futuristic]