from playwright.sync_api import Page, expect


def test_url(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(page.url)

def test_title(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_title("OrangeHRM")
    print(page.title())


#read data from excel
#write data into excel
#ddt using openpyxl


