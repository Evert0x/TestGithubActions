from tests.context import TestGithub

def test_success():
    assert TestGithub.sum(1, 2) == 3

def test_fail():
    assert TestGithub.sum(1, 2) == 4