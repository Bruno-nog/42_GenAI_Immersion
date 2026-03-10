import sys


def greeting(name: str) -> None:
    """
    receives a name and prints a greeting
    """
    print(f"Hello {name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("need an argument")
        sys.exit(1)
    greeting(sys.argv[1])