import unittest


def suite():  
    return unittest.TestLoader().discover("portfolio_app.tests", pattern="*.py")