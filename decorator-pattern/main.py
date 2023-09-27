import time

import random
import string


class BaseStream:
    def __init__(self, text):
        self.text = text

    def stream(self):
        for char in self.text:
            yield char
            time.sleep(1)


class StreamDecorator:
    def __init__(self, stream):
        self._stream = stream

    def stream(self):
        return self._stream.stream()


class PaddingStream(StreamDecorator):
    def stream(self):
        base_stream = super().stream()
        for char in base_stream:
            yield f" {char} "


class RandomFlipStream(StreamDecorator):
    def stream(self):
        base_stream = super().stream()
        for char in base_stream:
            if random.choice([True, False]):
                yield random.choice(string.ascii_letters)
            else:
                yield char


# Create a base stream with Sonnet 18
base = BaseStream(
    """
Shall I compare thee to a summer's day?
Thou art more lovely and more temperate:
...
So long lives this, and this gives life to thee.
"""
)


# Add padding
padded = PaddingStream(base)

# Randomly flip characters
random_flip = RandomFlipStream(padded)

# Stream out the text
for char in padded.stream():
    print(char, end="", flush=True)
