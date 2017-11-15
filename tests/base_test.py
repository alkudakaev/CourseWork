import pytest
from selenium import webdriver
import core.config


#  запускаем
@pytest.fixture(scope='class')
def setup(request):
    core.config.browser = webdriver.Chrome('E:\\University\ITMO\CourseWork\chromedriver.exe')

    def teardown():
        core.config.browser.quit()

    request.addfinalizer(teardown)

@pytest.mark.usefixtures('setup')
class BaseTest(object):
    pass