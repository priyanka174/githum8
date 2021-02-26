from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Libraries import Readdata

def startbrowser():
    global driver
    if((Readdata.data1('info', "Browser"))=='Chrome'):

        path="C:/Users/User/PycharmProjects/giyhubpr/Drivers/chromedriver.exe"
        driver=Chrome(executable_path=path)
    elif((Readdata.data1('info', "Browser")) == 'Firefox'):
        path = "C:/Users/User/PycharmProjects/giyhubpr/Drivers/geckodriver-v0.26.0-win64 (1)/geckodriver.exe"
        driver =Firefox(executable_path=path)
    else:
        path = "C:/Users/User/PycharmProjects/giyhubpr/Drivers/chromedriver.exe"
        driver=Chrome(executable_path=path)

    driver.get(Readdata.data1('info', 'Application_url'))
    driver.maximize_window()
    return driver

def closebrowser():
    driver.close()