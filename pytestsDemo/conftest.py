import pytest


@pytest.fixture(scope="class")  # because this scope was defined, it will only run once per class
def setup():
    print("This will be executed first")
    yield   # code after this will execute after the rest of the program runs
    print("This will execute last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["attila", "cseh", "attifreestyle.com"]  # tuple

@pytest.fixture(params=[("chrome", "attila", "cseh"), ("firefox", "attila"), ("IE", "text")])
def crossBrowser(request):  # request is used because we have params for the fixture
    return request.param