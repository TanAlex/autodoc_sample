
from utils import  *
from time import sleep

def greeting(name):
    """Print greeting message by given name

    Args:
        name (string): the name to greet

    Returns:
        None

    """
    return f"hello {name}"


if __name__ == "__main__":
    print(greeting("world"))

