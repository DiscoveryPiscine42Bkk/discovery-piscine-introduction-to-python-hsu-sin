#!/usr/bin/env python3

def find_the_redheads(dict):
    return list(filter(lambda name: dict[name]=='red', dict.keys()))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))