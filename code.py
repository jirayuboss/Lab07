import sqlite3
import unittest

conn = sqlite3.connect('users.db')
c = conn.cursor()

def login(username,password):
    usrnm = (username,)
    psswrd = (password,)

    check_validation = c.execute("SELECT COUNT(*) FROM Users WHERE USERNAME = ? AND PASSWORD = ?", [(username),(password)])
    for row_validation in check_validation:
        validation = row_validation[0]
    if validation == 1:
        return 'Login Success.'
    else:

        check_usrnm = c.execute("SELECT COUNT(*) FROM Users WHERE USERNAME = ?", usrnm)
        for row_usrnm in check_usrnm:
            usrnm_validation = row_usrnm[0]
        if usrnm_validation == 1:
            return 'Incorrect Password.'
        else:

            check_psswrd = c.execute("SELECT COUNT(*) FROM Users WHERE PASSWORD = ?", psswrd)
            for row_psswrd in check_psswrd:
                psswrd_validation = row_psswrd[0]
            if psswrd_validation == 1:
                return 'Incorrect Username.'
            else:
                return 'Incorrect Username and Password.'