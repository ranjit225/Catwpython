from Allrepo.properties import Envirnomentsetup,path2
from Loginfunction.Login import Logincatw
import unittest

from utilfunction.utilclass import functionutil


class Invalidcred(Envirnomentsetup):
    def test_invalidcred(self):
     print("******************This is the test case for*******************", __name__, "*************************")
     driver = self.driver
     login=Logincatw(driver)
     ss_path= "/Invalidcredi/"
     ss=functionutil(driver)
     try:
      if login.Invalidcred()==True:
         print("Application is not logged as the cred are invalid")
      else:
        print("case is failed")
        ss.ScreenShot(ss_path + "home.png")
      if login.Continyebutton()==True:
         print("clicked on continue button")
      else:
         print("falied in clicming on continue")
         ss.ScreenShot(ss_path + "home.png")
      if login.validatetext() == True:
         print("Text is verified sucesfully")
      else:
         print("unable to verify teh TEXT")
         ss.ScreenShot(ss_path + "home.png")
     except Exception as EXC:
        print("there is a exception",EXC)
        ss.ScreenShot(ss_path + "home1.png")

if __name__=="__main__":
    unittest.main()