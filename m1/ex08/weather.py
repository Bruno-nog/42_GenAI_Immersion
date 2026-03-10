import requests
import httpx
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("need an argument")
        sys.exit(1)
    city = sys.argv[1]
    