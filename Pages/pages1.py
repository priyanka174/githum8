from Libraries import Readdata

class pages2:
    def __init__(self, obj):
        global driver
        driver=obj

    def username(self, username):
        driver.find_element_by_name(Readdata.data2('info2', 'username')).send_keys("priya")

    def email(self, email):
        driver.find_element_by_name(Readdata.data2('info2', 'email')).send_keys("priya@.com")