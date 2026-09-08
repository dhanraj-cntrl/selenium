import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @pytest.fixture(params=["Chrome","Edge"])
# def setup(request):
#     browser=request.param
#     if browser=="Chrome":
#         driver=webdriver.Chrome()
#     elif browser=="Edge":
#         driver=webdriver.Edge()
#     driver.maximize_window()
#     yield driver
#     driver.quit()

@pytest.fixture  #scope=function/class/module/session/package
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login(setup):
    setup.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    setup.find_element(By.NAME,"username").send_keys("Admin")
    setup.find_element(By.NAME,"password").send_keys("admin123")
    setup.find_element(By.XPATH,"//button[@type='submit']").click()
    print(setup.title)

@pytest.mark.skip
@pytest.mark.parametrize("user_name,pass_word",[
    ("admin","admin123"),
    ("Admin","admin123")
])
def test_parametrize_login(setup,user_name,pass_word):
    setup.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    setup.find_element(By.NAME,"username").send_keys(user_name)
    setup.find_element(By.NAME,"password").send_keys(pass_word)
    setup.find_element(By.XPATH,"//button[@type='submit']").click()
    assert setup.title == "OrangeHRM"

@pytest.mark.skip(reason="under development")
def test_logout(setup):
    setup.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    setup.find_element(By.NAME,"username").send_keys("admin")
    setup.find_element(By.NAME,"password").send_keys("admin123")
    setup.find_element(By.XPATH,"//button[@type='submit']").click()
    wait=WebDriverWait(setup,10)
    wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='oxd-icon orangehrm-upgrade-icon']")))
    setup.save_screenshot("test_logout.png")

#@pytest.mark.skip
#@pytest.mark.skip(reason='development')
#@pytest.mark.skipif(browser=='Firefox')














