import time
import apisetup
import send
from send import gmail_send_message
from send import main

def check():
    while True:

        if (apisetup.checki_deathstoday):
            Body = "Today another 5000 people died :("
            main(Body)

        if (apisetup.checki_deaththisyear):
            Body = "This year another 10000 people died :("
            main(Body)

        if (apisetup.checki_deathbyalcohol):
            Body = "50 people died to alcohol :("
            main(Body)

        if (apisetup.checki_deathsbysmoking):
            Body = "100 people died to smoking  :("
            main(Body)

        if (apisetup.checki_deathsbyhiv):
           Body = "20 people died to HIV :("
           main(Body)

        if (apisetup.checki_deathsbycancer):
            Body = "30 people died to cancer :("
            main(Body)

        if (apisetup.checki_deathsofmothers):
            Body = "20 mothers died :("
            main(Body)

        if (apisetup.checki_deathsofchildren):
            Body = "10 childrens died :("
            main(Body)


        time.sleep(300)  # 5 Minuten warten

check()
