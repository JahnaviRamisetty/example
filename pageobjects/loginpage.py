import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class newaccount:

    createaccounttxt="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"
    firstnametxt="//*[@id='u_f_b_jr']"
    surnametxt="//*[@id='u_f_d_+o']"
    mobilenumbertxt="//*[@id='u_f_g_3S']"
    newpasswordtxt="//*[@id='password_step_input']"
    daytxt="//*[@id='day']"
    monthtxt="//*[@id='month']"
    yeartxt="//*[@id='year']"
    femaletxt="u_1j_2_Vn"
    maletxt="u_1j_3_/8"
    signintxt="//*[@id='u_f_s_Hh']"

    def __int__(self,driver):
        self.driver=driver

    def setCreateAccount(self):
        self.driver.find_element(By.CLASS_NAME,self.createaccounttxt).click()

    def setfirstname(self,firstname):
        self.driver.find_element(By.XPATH,self.firstnametxt).clear()
        self.driver.find_element(By.XPATH,self.firstnametxt).send_keys(firstname)
    def setsurname(self,surname):
        self.driver.find_element(By.XPATH,self.surnametxt).clear()
        self.driver.find_element(By.XPATH,self.surnametxt).send_keys(surname)
    def setmobilenumber(self,mobilenumber):
        self.driver.find_element(By.XPATH,self.mobilenumbertxt).clear()
        self.driver.find_element(By.XPATH,self.mobilenumbertxt).send_keys(mobilenumber)

    def setnewpassword(self,newpassword):
         self.driver.find_element(By.XPATH,self.newpasswordtxt).clear()
         self.driver.find_element(By.XPATH,self.newpasswordtxt).send_keys(newpassword)

    def setday(self,day):
        drp= Select(self.driver.find_element(By.XPATH,self.daytxt))
        drp.select_by_visible_text(day)



    def setmonth(self,month):
        drp1=Select(self.driver.find_element(By.XPATH,self.monthtxt))
        drp1.select_by_visible_text(month)

    def setyear(self,year):
        drp2=Select(self.driver.find_element(By.XPATH,self.yeartxt))
        drp2.select_by_visible_text(year)

    def setGender(self, gender):
            if gender == 'Male':
                self.driver.find_element(By.ID, self.maletxt).click()
            elif gender == 'Female':
                self.driver.find_element(By.ID, self.femaletxt).click()
            else:
                self.driver.find_element(By.ID, self.maletxt).click()

    def setsignintxt(self):
        self.driver.find_element(By.XPATH,self.signintxt)




