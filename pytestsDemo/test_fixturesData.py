import pytest

from .BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile222(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.critical(dataLoad[2])
        print(dataLoad[2])
