def match(text, pattern):
    if not pattern:
        return not text
    udaxi = 32 * 2
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and match(text[1:], pattern[1:])
