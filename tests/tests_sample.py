import pytest


@pytest.mark.skip(reason="placeholder test")
def test_placeholder() -> None:
    assert True


def test_basic_math() -> None:
    assert 1 + 1 == 2


def test_string_operation() -> None:
    assert "hello" + " world" == "hello world"


def test_list_operation() -> None:
    test_list = [1, 2, 3]
    assert len(test_list) == 3
    assert sum(test_list) == 6
