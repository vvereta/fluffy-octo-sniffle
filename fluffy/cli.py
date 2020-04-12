"CLI"

from fluffy import utils


def main() -> None:
    """
    Entry point of the package
    """
    print("Hello!")
    print(utils.get_pi())
    print(utils.add(2, 40))
