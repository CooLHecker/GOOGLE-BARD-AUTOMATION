from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID": "ewg1uqHfFfMjn9SOSe2M8jUtmiNcq3KRHJY-G1_xR5ubzMOXcXHTQkWAphG6BBaRUCOkjA.",
    "__Secure-1PSIDTS": "sidts-CjIBPVxjSsi7btT_NE61WeWKLnoh28NdjS-MiQ3_p0stH9Vqts5wX3WhA77kWU1cK40SfhAA",
    "__Secure-1PSIDCC": "ABTWhQF8euGiOAOkwH0RpWK7msO0oYZdbrMApKi-o2j9Puf_mtq-9X2DUSNqslPkyZNc7s21ow",

}

bard = BardCookies(cookie_dict = cookie_dict)

while True:
    Query = input("Enter Your Query:")
    Reply = bard.get_answer(Query)['content']
    print(Reply)