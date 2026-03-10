import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Need an argument")
        sys.exit(1)
    print(sys.argv[1])
    