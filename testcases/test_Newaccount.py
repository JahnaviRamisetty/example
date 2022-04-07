import time

import pytest
from selenium import webdriver
from pageobjects.loginpage import newaccount
from utilities.readproperties import Readconfig

class Test_Login:
    baseURL = Readconfig.getApplicationurl()

    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
       # self.na = newaccount(self.driver)
        self.na = newaccount(self.driver)
        self.na.setCreateAccount()
        time.sleep(2)
        self.na.setfirstname("abc")
        time.sleep(2)
        self.na.setsurname("xyz")
        time.sleep(2)
        self.na.setmobilenumber("987654321")
        time.sleep(3)
        self.na.setnewpassword("aaaa")
        time.sleep(2)
        self.na.setday("10")
        self.na.setmonth("july")
        self.na.setyear("1999")
        self.na.setGender("Female")
        self.na.setsignintxt()
        self.driver.save_screenshot(".\\screenshots\\" + "facebook.png")







