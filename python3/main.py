import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from json_strings import *

schema = {
    "type": "object",
    "required": ["name", "winPercent"],
    "properties": {
        "name": {"type": "string"},
        "winPercent": {"type": ["number", "null"]},
    },
}


def introduce(player):
    if player["winPercent"] is not None:
        print("{:s} wins {:f}% of the time."
              .format(
                  player["name"],
                  player["winPercent"]))
    else:
        print("{:s} is a new player."
              .format(player["name"]))


try:
    player = json.loads(good_json)

    try:
        validate(player, schema)
        introduce(player)

    except ValidationError as validation_error:
        print("Invalid player", validation_error)

except json.decoder.JSONDecodeError as decode_error:
    print("JSON parse error", decode_error)


# This was easy.
# Formatted using PEP8.
# Python was created by Guido van Rossum and first released in 1991.
# The language designer wanted something easy to read.
# It's multi-paradigm. Garbage collected.
# It can generate optimized code so the second execution of any file is faster.
# You can do this manually like so: `python -m compileall .`
# Python has been described as a protocol-oriented language. http://masnun.rocks/2017/04/15/interfaces-in-python-protocols-and-abcs/
# One thing I remember being odd about Python is that classes' instance methods
# need to be written as accepting that instance as the first parameter of each method,
# though they are not called this way. https://realpython.com/instance-class-and-static-methods-demystified/
# Lots of things are written in Python. https://en.wikipedia.org/wiki/List_of_Python_software
#   You've probably heard of Ansible, Dropbox, Mercurial, Eve Online (uses Stackless Python),
#   Django, Reddit (originally written in common lisp), YouTube.
# Then there's TensorFlow. https://www.tensorflow.org/get_started/get_started_for_beginners
# Because of TensorFlow, how easy it is to use Python, and the fact that very big companies will scout you
# I cannot recommend any language more.
