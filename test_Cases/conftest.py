import pytest
from selenium import webdriver

@pytest.fixture(params=["Chrome","Edge"])
def setup(request):
    browser=request.param

    if browser== "Chrome":
        options=webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver=webdriver.Chrome(options=options)
    elif browser == "Edge":
        options=webdriver.EdgeOptions()
        options.add_argument("--headless")
        driver=webdriver.Edge(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

# @pytest.fixture(params=["Chrome","Edge"])
# def setup(request):
#     browser=request.param
#     if browser== "Chrome":
#         driver=webdriver.Chrome()
#     elif browser == "Edge":
#         driver=webdriver.Edge()
#     driver.maximize_window()
#     yield driver
#     driver.quit()



