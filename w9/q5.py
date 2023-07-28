#!/usr/bin/python3

from argparse import ArgumentParser
from bs4 import BeautifulSoup
import requests
import sys
import collections

def main():
    parser = ArgumentParser(prog="tags.py", 
                            description="print tags of given url")
    parser.add_argument("-f", "--frequency", action="store_true", help="print by frequency instead of lexi")
    parser.add_argument("url", help="url to get tags from")

    args = parser.parse_args()

    resp = requests.get(args.url)

    if resp.status_code != 200:
        sys.exit(1)
    
    soup = BeautifulSoup(resp.text.lower(), 'html.parser') # html5lib

    tags = soup.find_all()
    # print(tags)
    tag_names = [tag.name for tag in tags]

    counts = collections.Counter(tag_names)

    # print
    if args.frequency:
        for (tag, count) in counts.most_common():
            print(f"{tag} {count}")
    else:
        for (tag, count) in sorted(counts.items()):
            print(f"{tag} {count}")


if __name__ == "__main__":
    main()