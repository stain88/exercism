import re

def abbreviate(phrase):
    matches = re.findall(r'((?<![A-Z])[A-Z])|(?:(?:\s|-)([a-z]))', phrase)
    return ''.join(''.join(x) for x in matches).upper()
