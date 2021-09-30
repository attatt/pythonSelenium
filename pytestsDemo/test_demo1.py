# all pytest file names should start with "test_" or end with "_test"
# all pytest method names should start "test"

# all code should be wrapped in method
import pytest


def test_firstProgram():
    print("Hello")

@pytest.mark.smoke
def test_secondCreditCardProgram():
    print("Sup")