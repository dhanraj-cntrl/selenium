#
#
#
# #async- while waiting for one program it allows to perform another
#
# import pytest
# from playwright.async_api import Page, expect
#
#
# @pytest.mark.asyncio
# async def test_url(page:Page):
#     await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     await expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
# @pytest.mark.asyncio
# async def test_apititle(page:Page):
#     await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     await expect(page).to_have_title("OrangeHR")
#     print(page.title())
#     print(page.url)
#
# # Task 1 → API call → waiting 3 seconds
# # Task 2 → database query → waiting 2 seconds
# # Task 3 → process data
# #
# # With async programming, while Task 1 is waiting,
# #the program can work on Task 2 or Task 3.
# #Asynchronous execution allows multiple tasks to make progress concurrently.
# #When one task is waiting for an I/O operation to complete,
# #the program can use that waiting time to execute other available tasks
# #instead of blocking the entire program
#
# #Task 1 (3Second)
#
#
# #Task 2 (2Second)
#
#
# #Task 3 (1 Second)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
