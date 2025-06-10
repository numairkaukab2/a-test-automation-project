import pytest

def test_addition():
    result = 2 + 2
    assert result==4

@pytest.mark.skip(reason="Known failure, will fix later")
def test_addition2():
    result = 3+5
    assert result==7