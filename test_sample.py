import pytest
from selenium import webdriver



# @pytest.fixture
# def setup():
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()


# @pytest.fixture(params=["Chrome","Edge"])
# def setup(request):
#     browser=request.param
#     if browser=="Chrome":
#         driver=webdriver.Chrome()
#     elif browser=="Edge":
#         driver=webdriver.Edge()
#     yield driver
#     driver.quit()

@pytest.fixture
def setup():
    options=webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver=webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# @pytest.mark.parametrize("username,password",[
#     ("Admin","admin123"),
#     ("WrongAdmin","wrongPass")
# ])
# def test_login_para(self,setup,username,password):
#
















