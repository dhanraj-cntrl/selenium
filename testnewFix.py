import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def setup():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
@pytest.mark.sanity
def test_homepage(setup):
    setup.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(setup.title)
    setup.save_screenshot("Homepage.png")

@pytest.mark.smoke
@pytest.mark.parametrize("username,password",
                         [
                             ("admin123","123"),
                             ("Admin123","admin12333"),
                             ("Admin","admin123")
                         ])
def test_login(setup,username,password):
    setup.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    setup.find_element(By.NAME,"username").send_keys(username)
    setup.find_element(By.NAME,"password").send_keys(password)
    setup.find_element(By.XPATH,"//button[@type='submit']").click()
    print(setup.title)
    # assert setup.title == "OrangeHRM"

