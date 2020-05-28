from selenium import webdriver

from Allrepo.properties import Envirnomentsetup
from Fillingcode.ClickTimeentry import clickTimeEntry
from Fillingcode.Entrycode import Selcectdropdown
from Fillingcode.Fillinghours import fillinghrs
from Fillingcode.Hrsinweek import validatinghrs
from Loginfunction.Login import Logincatw
from Loginfunction.Logout import Logout
import unittest


class Loginandlogout(Envirnomentsetup):
    def test_lohinlout(self):
      login=Logincatw()
      cte=clickTimeEntry()
      hrperweek=validatinghrs()
      logout=Logout()
      fili=fillinghrs()
      try:
        if login.loginwithvalidcred()==True:
         print("sucessfully logged into application")
        else:
         print("login to application is failed")
        if cte.element_to_clicktimeentery()==True:
         print("sucessfully clicked on time entry")
        else:
         print("falied in clicking time entry link")
        if cte.click_continuebutton()==True:
         print("sucessfully clicked on Continue button")
        else:
         print("Failed in clicking on continue button")
        if hrperweek.totalhrs()==True:
         print("total hrs are validated in catw and hours are equal for a week")
        else:
         print("total hrs are not equal in a week")
        if hrperweek.standradhours()==True:
         print("Standard hrs is less than the logged hrs for current week")
        else:
         print("Standard hrs is greater than the logged hrs for current week")
        if fili.fillinghrss()==True:
         print("sucesfully logged out of the application")
        else:
         print("unable to logout of the applciation")
      except Exception as err:
          print("there is a exception",err)

if __name__=="__main__":
    unittest.main()



















































