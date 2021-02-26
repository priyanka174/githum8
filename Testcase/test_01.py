from selenium.webdriver import Chrome
from Base import Base_01
from Libraries import Readdata
from Pages import pages1
def test_data01():
    driver=Base_01.startbrowser()
    reg=pages1.pages2(driver)
    reg.username("priya")
    driver=Base_01.closebrowser()


def test_data02():
    driver=Base_01.startbrowser()
    reg=pages1.pages2(driver)
    reg.email("priya@gmail.com")
    driver=Base_01.closebrowser()