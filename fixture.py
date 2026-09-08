import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_loginPage(setup):
    setup.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(setup.current_url)
    print(setup.title)

def test_login(setup):
    setup.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    setup.implicitly_wait(10)
    setup.find_element(By.NAME,"username").send_keys("Admin")
    setup.find_element(By.NAME,"password").send_keys("admin123")
    setup.find_element(By.XPATH,"//button[@type='submit']").click()
    print(setup.title)


@pytest.mark.parametrize(
    "user_name,pass_word",[
    ("admin2","admin123"),
    ("Admin","Admin123"),
    ("admin123","123pasdd"),
    ("Admin","admin123")
])

def test_parametrize_login(setup,user_name,pass_word):
    setup.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    setup.implicitly_wait(10)
    setup.find_element(By.NAME,"username").send_keys(user_name)
    setup.find_element(By.NAME,"password").send_keys(pass_word)
    setup.find_element(By.XPATH,"//button[@type='submit']").click()
    assert setup.title == "OrangeHRM"






