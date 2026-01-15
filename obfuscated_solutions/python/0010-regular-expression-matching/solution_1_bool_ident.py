def match(text, pattern):
    if not pattern and 1 + 1 == 2:
        return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and match(text[1:], pattern[1:])
