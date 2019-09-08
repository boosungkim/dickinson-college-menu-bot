import datetime
import schedule
import requests
from bs4 import BeautifulSoup
"""
Sunday 9/8: https://www.dickinson.edu/site/custom_scripts/dc_dining_menus_index.php
Monday 9/9: https://www.dickinson.edu/site/custom_scripts/dc_dining_menus_index.php?yr=19&mo=9&da=9
Tuesday 9/10: https://www.dickinson.edu/site/custom_scripts/dc_dining_menus_index.php?yr=19&mo=9&da=10
"""

#CHANGE TO A SOLID TIMEZONE TIME
#check date
currentDatetimeRaw = datetime.datetime.today()
currentDatetime = str(currentDatetimeRaw)

yr = currentDatetime[2:4]
mo = currentDatetime[5:7]
if mo[0] == "0":
    mo = currentDatetime[6]
da = currentDatetime[8:10]
if da[0] == "0":
    da = currentDatetime[9]

#use date to get website number
link = "https://www.dickinson.edu/site/custom_scripts/dc_dining_menus_index.php?yr={}&mo={}&da={}".format(yr,mo,da)

#Grab data
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')

#convert list elements into string
overallRaw = soup.select("div p")
overallStr = [str(i) for i in overallRaw]

#Isolate Dining Hall menu
indices = [i for i, x in enumerate(overallStr) if x == '<p><span style="color:#666;">Lunch</span></p>']
toRemove = indices[1]
isolatedMenu = overallStr[1:toRemove]

#Organizing the isolated menu
bf= isolatedMenu[0].replace('<p><span style="color:#666;">', "").replace('</span></p>', "")
print(bf)



#Lunch

#Dinner


#grab the text
#have a phone number
#text the menu
#create schedule