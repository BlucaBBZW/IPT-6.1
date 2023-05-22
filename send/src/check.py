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
            Body = "Today another 5000 people died :("
            main(Body)

        if (apisetup.checki_deathbyalcohol):
            Body = "Today another 5000 people died :("
            main(Body)

        if (apisetup.checki_deathsbysmoking):
            Body = "Today another 5000 people died :("
            main(Body)

        if (apisetup.checki_deathsbyhiv):
           Body = "Today another 5000 people died :("
           main(Body)

        if (apisetup.checki_deathsbycancer):
            Body = "Today another 5000 people died :("
            main(Body)

        if (apisetup.checki_deathsofmothers):
            Body = "Today another 5000 people died :("
            main(Body)

        if (apisetup.checki_deathsofchildren):
            Body = "Today another 5000 people died :("
            main(Body)


        time.sleep(300)  # 5 Minuten warten
