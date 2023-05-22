import pymongo

import os




username = ""

password = ""

myclient = pymongo.MongoClient(f'mongodb+srv://{username}:{password}')

mydb = myclient[""] #db name

col_sub = mydb["subscribers"] # collection name



class Database:

        @staticmethod

        def add_email_address(email_address:str): # Fügt eine Addresse hinzu

                 try:

                         email_address = email_address.lower()

                        insert = {"address": email_address, "awards": {"first": 0, "second": 0, "third": 0}, "isSubscribed": True}

                        if not email_address in Database.get_email_address(): # Wenn die Addresse nicht exestriert

                        col_sub.insert_one(insert) # fügt hinzu

                         else:

                            print(f'Email already exists: {email_address})')

                except Exception as error:

                         print("Error: " + str(error))

                         # TODO Log
