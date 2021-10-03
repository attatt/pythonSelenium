import pytest

@pytest.mark.usefixtures("dataLoad")
class TestFixtureExample:

    def test_editProfile(self, dataLoad):  # here, we must pass the fixture name to the method, because we return something from the fixture
        print(dataLoad)
        print(dataLoad[2])