import Allfunction
from selenium import webdriver
from Allrepo import properties
from Allrepo import Locaters
class Logincatw(object):
    def __init__(self,driver):
        self.driver= driver
    def loginwithvalidcred(self):
        value=self.driver.find_element_by_xpath(Locaters.Login_page).is_displayed()
        if value==True:
         rows = Allfunction.contriws(properties.path, "Catw")
         username = Allfunction.UNPWD(properties.path, "Catw", rows, 1)
         password = Allfunction.UNPWD(properties.path, "Catw", rows, 2)
         self.driver.find_element_by_id(Locaters.User_Name).send_keys(username)
         self.driver.find_element_by_id(Locaters.Password).send_keys(password)
         self.driver.find_element_by_class_name(Locaters.Countinue_Button).click()
         return True
        else:
            print("Login page is not visible")
            return False

    def Invalidcred(self):
        try:
         value =self.driver.find_element_by_xpath(Locaters.Login_page).is_displayed()
         if value==True:
            rows=Allfunction.contriws(properties.path,"invalid")
            username = Allfunction.UNPWD(properties.path, "invalid", rows, 1)
            password = Allfunction.UNPWD(properties.path, "invalid", rows, 2)
            self.driver.find_element_by_id(Locaters.User_Name).send_keys(username)
            self.driver.find_element_by_id(Locaters.Password).send_keys(password)
            return True
         else:
            print("login page is not visible")

            return False
        except:
            print("ERROR in homepage as unable to enter creditinals!")




    def validatetext(self):
        Text = self.driver.find_element_by_id(Locaters.Text_validate).text
        print(Text)
        if Text == "Client, name, or password is not correct; log on again":
            print("unable to login since the credials are invalid")
            return True
        else:
            print("found error")
            return False

    def Continyebutton(self):
        button=self.driver.find_element_by_class_name(Locaters.Countinue_Button)
        if button.is_displayed()==True:
            button.click()
            print("sucessfully clicked on continue button")
            return True
        else:
            print("unable to click on continue button")
            return False







