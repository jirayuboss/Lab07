import code
import unittest

class TestCode(unittest.TestCase):
    def test_login_correct(self):
        self.assertEqual(code.login('pigboss1','094585648'), 'Login Success.')

    def test_login_incorrect_username(self):
        self.assertEqual(code.login('pigboss','094585648'), 'Incorrect Username.')

    def test_login_incorrect_password(self):
        self.assertEqual(code.login('pigboss1','09458'), 'Incorrect Password.')

    def test_login_incorrect_usernameandpassword(self):
        self.assertEqual(code.login('pigboss', '094585'), 'Incorrect Username and Password.')

if __name__ == '__main__':
    unittest.main()