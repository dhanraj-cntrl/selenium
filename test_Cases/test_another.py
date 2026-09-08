import pytest
from selenium import webdriver


#fixture
@pytest.fixture
def setup():
    options=webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quite()

# @pytest.fixture(params=[("Chrome","Edge")])
# def setup(request):
#     browser=request.param
#     if browser=="Chrome":
#         driver=webdriver.Chrome()
#     elif browser=="Edge":
#         driver=webdriver.Edge()
#     driver.maximize_window()
#     yield driver
#     driver.quite()











