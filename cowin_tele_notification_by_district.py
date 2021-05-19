# code written by Mayank saini
# twitter @mayank98108
import json
import telegram
import requests
from datetime import datetime, timedelta
import time


def notify_me(message):
    token = ""  # Enter the token of your Telegram bot
    chat_id = "" # Enter the chat ID
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)

age = 46 # Enter your age
district_ids = "147"  # enter your district id
num_days = 2 # number of days to look

print_flag = 'Y'

print("Starting search for Covid vaccine slots!")

actual = datetime.today()
list_format = [actual + timedelta(days=i) for i in range(num_days)]
actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]

while True: # this loop will keep looking
    counter = 0   

    for district_id in district_ids:   
        for given_date in actual_dates:

            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(district_ids, given_date)
            print(URL)
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
            
            result = requests.get(URL, headers=header)

            if result.ok:
                response_json = result.json()
                if response_json["sessions"]:
                    if(print_flag.lower() =='y'):
                        
                        for session in response_json["sessions"]:
                            if (session["min_age_limit"] <= age and session["available_capacity"] > 0 ) :
                                notify_me('Alert!!!')
                                print("Available on: {}".format(given_date))
                                notify_me("Available on: {}".format(given_date))
                                print("Pincode: ", session["pincode"])
                                notify_me('     Pincode: ')
                                notify_me(session["pincode"])
                                print('Center Name: ' + session["name"])
                                notify_me('     Center Name: ' + session["name"])
                                print("\t Price: ", session["fee_type"])
                                notify_me('     Price: ' + session["fee_type"])
                                print("\t Availablity : ", session["available_capacity"])
                                notify_me("Available capacity:")
                                notify_me(session["available_capacity"])

                                if(session["vaccine"] != ''):
                                    print("\t Vaccine type: ", session["vaccine"])
                                    notify_me('     Vaccine type: ' + session["vaccine"])
                                print("\n")
                                notify_me('************************************')
                                counter = counter + 1
            else:
                print("No Response!")
                
    if counter == 0:
        print("No Vaccination slot available!")
    time.sleep(30) # sleep for 30 seconds
