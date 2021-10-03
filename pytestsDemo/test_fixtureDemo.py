import pytest

@pytest.mark.usefixtures("setup")  # the fixture will be applied to all the methods in the class
class TestExample:

    def test_fixtureDemo1(self):  # we use 'setup' as an argument, so that it is linked to the fixture
        print("This will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):  # we use 'setup' as an argument, so that it is linked to the fixture
        print("This will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):  # we use 'setup' as an argument, so that it is linked to the fixture
        print("This will execute steps in fixtureDemo3 method")