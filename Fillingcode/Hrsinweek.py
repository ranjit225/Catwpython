import time

from selenium import webdriver

from Allrepo import Locaters

totalhours=float(45.0)
class validatinghrs:
    def __init__(self,driver):
        self.driver= driver
    def totalhrs(self):
        loggedhours=self.driver.find_element_by_xpath(Locaters.Logged_HRS).text
        if float(loggedhours)==totalhours:
            print("total hours are matching which is :",loggedhours)
            return True
        else:
            print("hours are not matching which is :",loggedhours)
            return False

    def standradhours(self):
            loggedhours = self.driver.find_element_by_xpath(Locaters.Logged_HRS).text
            Standardhours= self.driver.find_element_by_xpath(Locaters.Standard_HRS).text
            if loggedhours>=Standardhours:
                print("hours logged in a week"+ loggedhours +":which is greater then standar hours:"+ Standardhours +" ")
                return True
            else:
                print("hours logged in a week"+ Standardhours +":which is greater then standar hours:"+ loggedhours)
                print("hours needs to be add more will be:", Standardhours-loggedhours)
                return False








