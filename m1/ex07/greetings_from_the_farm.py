import sys
import cowsay

def greetings_from_the_farm(name: str) -> None:
    """
    receives a name and prints a greeting
    """
    cowsay.cow(f"Hello {name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("need an argument")
        sys.exit(1)
    greetings_from_the_farm(sys.argv[1])