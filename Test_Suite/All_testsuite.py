import unittest

from scripts.loginwithvaidcreditianls import Loginandlogout
from scripts.loginwithinvaidcreditinals import Invalidcred


tc1=unittest.TestLoader().loadTestsFromTestCase(Loginandlogout)
tc2=unittest.TestLoader().loadTestsFromTestCase(Invalidcred)


sanitytest=unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(sanitytest)
