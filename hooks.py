#pytest_runtest_makereport

import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):

    outcome = yield

    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        driver=item.funcargs.get("driver")
        if driver:
            driver.save_screenshot("save_screenshot.png")

def test_login(driver):
    driver.get("http://localhost:8080")

    assert driver.title == "Invalid Title"