# Created by @data_quest_

# Weather App (in python)
# ⚠ Input Instructions:

# 1. Just Enter Your City Name in the right format.
# 2. The city name doesnt need to be very specific. But you can add more infos like state or country name. Its like a google search. 

# This code returns the latest weather data so the the result might change time over time. 
# all times are according to the timezone of servers.
#using OPENWEATHERMAP API


"   *･ﾟﾟ･*:.｡..｡.:*ﾟ:*:✼✿　　"


from urllib.request import urlopen
from urllib.parse import quote
import json


import datetime

cityname=quote(input()) or "New+York"
try:
    data=urlopen(f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&units=metric&appid=af50bbd7309f973b6a2318253e78ad20") # open weather map api
except:
    print("Please Enter A valid city Name!")
    exit()


data=json.loads(data.read()) 

def center(s):
    """ 
    For data presentation.
    """
    g=" "*((15-len(s))//2)
    s=g+s+g
    print(s.center(26))


def temp(flt):
    """
    for temparatures presentation.
    """
    flt=float(flt)
    return str(flt)[:str(flt).find(".")+2]


# city name
center("City Name")
center(data["name"])

print()

center("Country")
center(data["sys"]["country"])

print()

center("Long | Lat")
center(f'{data["coord"]["lon"]} | {data["coord"]["lat"]}')

print()

center("Weather Description")
center(data["weather"][0]["description"].title())

print()

center("Temperature")
center(f"{temp(data['main']['temp'])}°C")

center(f"{temp(data['main']['temp_min'])}°C | {temp(data['main']['temp_max'])}°C")

print()

center("Feels like")
center(f'{temp(data["main"]["feels_like"])}°C') 

print()

center("Humidity")
center (str(data["main"]["humidity"]) +"%")

print()
timesta=datetime.datetime.fromtimestamp

center("Sunrise | Sunset")
center(f" {str(timesta(data['sys']['sunrise']))[-9:]} | {str(timesta(data['sys']['sunset']))[-9:]}")

print()


center(" Local")
center(" Date | Time")
center(f" {str(timesta(data['dt']))[:10]} | {str(timesta(data['dt']))[-10:]}")

print()

center("@data_quest_")

       
'''
>>OUTPUT<<
Bangalore
        City Name         
        Bengaluru         

         Country          
            IN            

        Long | Lat        
       77.6 | 12.98       

   Weather Description    
        Clear Sky         

       Temperature        
          30.0°C          
     26.0°C | 31.6°C      

        Feels like        
          28.6°C          

         Humidity         
           32%            

     Sunrise | Sunset     
    07:37:55 |  20:01:49  

           Local          
        Date | Time       
  2020-04-13 | 3 22:59:35 

       @data_quest_  
 '''
