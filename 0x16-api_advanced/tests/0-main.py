#!/usr/bin/python3
"""Main script to get the number of Reddit subreddit subscribers."""
import sys
from reddit_subscribers import number_of_subscribers

def main():
    if len(sys.argv) != 2:
        print("Usage: main.py <subreddit>")
        sys.exit(1)

    subreddit = sys.argv[1]
    subscribers = number_of_subscribers(subreddit)
    print(f"Subreddit '{subreddit}' has {subscribers} subscribers.")

if __name__ == "__main__":
    main()

