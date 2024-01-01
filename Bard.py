from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID": "ENTER YOUR KEY",
    "__Secure-1PSIDTS": "ENTER YOUR KEY",
    "__Secure-1PSIDCC": "ENTER YOUR KEY",

}

bard = BardCookies(cookie_dict = cookie_dict)

while True:
    Query = input("Enter Your Query:")
    Reply = bard.get_answer(Query)['content']
    print(Reply)
