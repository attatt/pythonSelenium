# all pytest file names should start with "test_" or end with "_test"
# all pytest method names should start "test"

# all code should be wrapped in method
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Sup", "Test failed because strings do not match"

@pytest.mark.xfail
def test_secondCreditCard():
    a = 4
    b = 6
    assert a + b == 10, "Addition result does not match(att)"