import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(params=["Chrome","Edge"])
def setup(request):
    browser=request.param
    if browser=="Chrome":
        driver=webdriver.Chrome()
    elif browser=="Edge":
        driver=webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.skip
def test_homepage(setup):
    setup.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    setup.find_element(By.NAME,"username").send_keys("Admin")
    setup.find_element(By.NAME,"password").send_keys("admin123")
    setup.find_element(By.XPATH,"//button[@type='submit']").click()
    assert setup.title=="OrangeHRM"
    setup.save_screenshot("Homepage.png")

@pytest.mark.parametrize("user_name,pass_word",
                         [("admin12","admin123"),
                          ("Admin","admin123")
                          ])
def test_login(setup,user_name,pass_word):
    setup.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    setup.find_element(By.NAME,"username").send_keys(user_name)
    setup.find_element(By.NAME,"password").send_keys(pass_word)
    setup.find_element(By.XPATH,"//button[@type='submit']").click()
    assert setup.title=="OrangeHRM"


def test_AutomationBlogspot(setup):
    setup.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
    setup.find_element(By.XPATH,"//button[contains(text(),'New Tab')]").click()
    parent=setup.current_window_handle
    for i in setup.window_handles:
        setup.switch_to.window(i)
        if setup.title=="SDET-QA Blog":
            print(setup.title)



# @pytest.fixture(params=["Chrome","Edge"])
# def setup_headless(request):
#     browser=request.param
#     if browser=="Chrome":
#         options=webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         driver=webdriver.Chrome(options=options)
#     elif browser=="Edge":
#         options=webdriver.EdgeOptions()
#         options.add_argument("--headless")
#         driver=webdriver.Edge(options=options)
#     yield driver
#     driver.quit()




















