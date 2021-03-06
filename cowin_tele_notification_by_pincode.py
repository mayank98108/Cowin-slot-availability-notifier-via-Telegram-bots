# code written by Mayank saini
# twitter @mayank98108
import json
import telegram
import requests
from datetime import datetime, timedelta
import time


def notify_me(message):
    token = "" # Enter your telegram bot tokken
    chat_id = "" # Enter your chat id
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)

age = 46    # Enter your age
pincodes = [""]  # Enter your pincodes here, you can make a list of valid pincodes
num_days = 2 # Look for next 2 day

print_flag = 'Y'

print("Starting search for Covid vaccine slots!")

actual = datetime.today()
list_format = [actual + timedelta(days=i) for i in range(num_days)]
actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]

while True:
    counter = 0   

    for pincode in pincodes:   
        for given_date in actual_dates:

            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, given_date)
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
            
            result = requests.get(URL, headers=header)

            if result.ok:
                response_json = result.json()
                if response_json["centers"]:
                    if(print_flag.lower() =='y'):
                        for center in response_json["centers"]:
                            for session in center["sessions"]:
                                if (session["min_age_limit"] <= age and session["available_capacity"] > 0 ) :
                                    notify_me('Alert!!!')
                                    print('Pincode: ' + pincode)
                                    notify_me('Pincode: ' + pincode)
                                    print("Available on: {}".format(given_date))
                                    notify_me("Available on: {}".format(given_date))
                                    print('Pincode: ' + center["name"])
                                    notify_me('     Center Name: ' + center["name"])
                                    print("\t", center["block_name"])
                                    notify_me('     Block name: ' + center["block_name"])
                                    print("\t Price: ", center["fee_type"])
                                    notify_me('     Price: ' + center["fee_type"])
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

