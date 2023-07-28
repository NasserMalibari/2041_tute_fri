#!/usr/bin/python3

"""
Write a Python program, tags.py which given the URL of a web page fetches it by running wget and prints the HTML tags it uses.
The tag should be converted to lower case and printed in alphabetical order with a count of how often each is used.
Don't count closing tags.
Make sure you don't print tags within HTML comments
"""

from argparse import ArgumentParser
import subprocess
import re
import collections

def main():
    parser = ArgumentParser(prog="tags.py", 
                            description="print tags of given url")
    parser.add_argument("-f", "--frequency", action="store_true", help="print by frequency instead of lexi")
    parser.add_argument("url", help="url to get tags from")

    args = parser.parse_args()

    process = subprocess.run(["wget", "-O-", "-q", args.url], capture_output = True, text=True)

    text = process.stdout.lower()

    # remove comments
    text = re.sub(r"<!--.*?>", "", text, flags=re.DOTALL)
    # get tags 
    tags = re.findall(r"</(\w+)>" , text)

    # <br/>
    # count them

    counts = collections.Counter(tags)
    # alternatively
    # for name in tags:
    #     counts[name] += 1

    # print
    if args.frequency:
        for (tag, count) in counts.most_common():
            print(f"{tag} {count}")
    else:
        for (tag, count) in sorted(counts.items()):
            print(f"{tag} {count}")

if __name__ == "__main__":
    main()