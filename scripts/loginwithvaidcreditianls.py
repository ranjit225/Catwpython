import time

from selenium import webdriver

from Allrepo import properties
from Allrepo.properties import Envirnomentsetup
from Fillingcode.ClickTimeentry import clickTimeEntry
from Fillingcode.Hrsinweek import validatinghrs
from Loginfunction.Login import Logincatw
from Loginfunction.Logout import Logout
import unittest

from utilfunction.utilclass import functionutil


class Loginandlogout(Envirnomentsetup):
    def test_lohinlout(self):
      print("******************This is the test case for*******************", __name__, "*************************")
      driver = self.driver
      login=Logincatw(driver)
      cte=clickTimeEntry(driver)
      hrperweek=validatinghrs(driver)
      logout=Logout(driver)
      ss_path = "/Validcred/"
      ss = functionutil(driver)
      try:
        if login.loginwithvalidcred()==True:
         print("sucessfully logged into application")
        else:
         print("login to application is failed")
         ss.ScreenShot(ss_path + "dashvoard.png")
        if cte.element_to_clicktimeentery()==True:
         print("sucessfully clicked on time entry")
        else:
         print("falied in clicking time entry link")
         ss.ScreenShot(ss_path + "dashvoard.png")
        if cte.click_continuebutton()==True:
         print("sucessfully clicked on Continue button")
        else:
         print("Failed in clicking on continue button")
         ss.ScreenShot(ss_path + "dashvoard.png")
        if hrperweek.totalhrs()==True:
         print("total hrs are validated in catw and hours are equal for a week")
        else:
         print("total hrs are not equal in a week")
         ss.ScreenShot(ss_path + "dashvoard.png")
        if hrperweek.standradhours()==True:
         print("Standard hrs is less than the logged hrs for current week")
        else:
         print("Standard hrs is greater than the logged hrs for current week")
         ss.ScreenShot(ss_path + "dashvoard.png")
        if logout.logout()==True:
         print("sucesfully logged out of the application")
        else:
         print("unable to logout of the applciation")
         ss.ScreenShot(ss_path + "dashvoard.png")
      except Exception as err:
          print("there is a exception",err)
          ss.ScreenShot(ss_path + "dashvoard1.png")


if __name__=="__main__":
    unittest.main()

























