from my_modern_project.main import add, hello


def test_add() -> None:
    assert add(1, 2) == 3


def test_hello() -> None:
    assert hello() == "Hello, World!"
