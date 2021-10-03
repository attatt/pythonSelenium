# all pytest file names should start with "test_" or end with "_test"
# all pytest method names should start "test"

# all code should be wrapped in method
import pytest



def test_firstProgram(setup):  # we use 'setup' as an argument, so that it is linked to the fixture
    print("Hello")

@pytest.mark.smoke
def test_secondCreditCardProgram():
    print("Sup")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])
    print(crossBrowser[1])
