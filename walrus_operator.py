# 3.8 feature
# called walrus because apparently := looks like walrus eyes with tusks
import re

VALUE_BEFORE_COLON_RE = re.compile("(.*?):.*")


def print_if_match(text: str):
    match = VALUE_BEFORE_COLON_RE.match(text)
    if match:
        print(match.group(1))
    else:
        print("no match")


def print_if_match_with_walrus(text: str):
    if match := VALUE_BEFORE_COLON_RE.match(text):
        print(match.group(1))
    else:
        print("no match")


if __name__ == '__main__':
    print_if_match_with_walrus("blarg")
    print_if_match_with_walrus("foo:bar")
