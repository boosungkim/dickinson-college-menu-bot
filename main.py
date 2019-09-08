import datetime
import schedule
import requests
from bs4 import BeautifulSoup
<<<<<<< HEAD
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
=======
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from configparser import ConfigParser

#CHANGE TO A SOLID TIMEZONE TIME
#CHANGE /W to WITH

#check date
def getLink():
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
    return link


def getMenu(link):
    #Grab data
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    #convert list elements into string
    overallRaw = soup.select("div p")
    overallStr = [str(i) for i in overallRaw]
    #Isolate Dining Hall menu
    indices = [i for i, x in enumerate(overallStr) if x == '<p><span style="color:#666;">Lunch</span></p>']
    toRemove = indices[1]
    isolatedRawMenu = overallRaw[1:toRemove]
    isolatedStrMenu = overallStr[1:toRemove]
    #Divide into sections
    lcStart = isolatedStrMenu.index('<p><span style="color:#666;">Lunch</span></p>')
    dnStart = isolatedStrMenu.index('<p><span style="color:#666;">Dinner</span></p>')
    
    breakfastRawList = isolatedRawMenu[0:lcStart]
    lunchRawList = isolatedRawMenu[lcStart:dnStart]
    dinnerRawList = isolatedRawMenu[dnStart:]
    #Final lists
    breakfastStrList = []
    lunchStrList = []
    dinnerStrList = []
    #Breakfast String List
    for i in breakfastRawList:
        breakfastStrList.append(str(i.get_text()))
    #Lunch String List
    for j in lunchRawList:
        lunchStrList.append(str(j.get_text()))
    #Dinner String List
    for k in dinnerRawList:
        dinnerStrList.append(str(k.get_text()))
    return [breakfastStrList, lunchStrList, dinnerStrList]


def formatMenu(stringList):
    formattedMenu = ""
    for a in stringList:
        if a == "Breakfast":
            formattedMenu = "-Breakfast-"
        elif a == "Lunch":
            formattedMenu = "-Lunch-"
        elif a == "Dinner":
            formattedMenu = "-Dinner-"
        else:
            formattedMenu = formattedMenu + "\n {}".format(a)
    return formattedMenu


# def sendMenu(breakfast, lunch, dinner):
#     parser = ConfigParser()
#     parser.read('config.ini')
#     #Getting info to log in
#     myEmail = parser.get('SensitiveData', 'myEmail')
#     myPassword = parser.get('SensitiveData', 'myPassword')
#     hostName = parser.get('SensitiveData', 'hostName')
#     smtpCode = parser.get('SensitiveData', 'smtpCode')
#     subject = "Today's Menu"
#     #ADD DATE HERE IN FUTURE
#     message = "Hello, I am Boo Sung Kim's Dickinson Menu Bot. Today's menu is: \n \n" + breakfast + "\n \n" + lunch + "\n \n" + dinner
    
#     #Getting emails
#     with open('email.txt', 'r') as f:
#         recipientEmail = f.readline()

    # msg = MIMEMultipart()
    # msg['From'] = myEmail
    # msg['To'] = recipientEmail
    # msg['Subject'] = subject
    # msg.attach(MIMEText(message, 'plain'))
    # server = smtplib.SMTP()
    # server.connect('127.0.0.1', smtpCode)
    # server.starttls()
    # # server.ehlo()
    # server.login(myEmail, myPassword)
    # text = msg.as_string()
    # server.sendmail(myEmail, recipientEmail, text)
    # with open('email.txt', 'r') as f:
    #     for recipientEmail in f:
    #         server.sendmail(myEmail, recipientEmail, text)
    # server.quit()


def main():
    menuLink = getLink()
    threeMeals = getMenu(menuLink)
    breakfast = formatMenu(threeMeals[0])
    lunch = formatMenu(threeMeals[1])
    dinner = formatMenu(threeMeals[2])
    message = "Hello, I am Boo Sung Kim's Dickinson Menu Bot. Today's menu is: \n \n" + breakfast + "\n \n" + lunch + "\n \n" + dinner
    # sendMenu(breakfast, lunch, dinner)

    parser = ConfigParser()
    parser.read('config.ini')
    #Getting info to log in
    myEmail = str(parser.get('SensitiveData', 'myEmail'))
    myPassword = str(parser.get('SensitiveData', 'myPassword'))
    hostName = str(parser.get('SensitiveData', 'hostName'))
    smtpCode = int(parser.get('SensitiveData', 'smtpCode'))
    subject = "Today's Menu"

    recipientEmail = []
    with open('email.txt', 'r') as f:
        for line in f:
            line = line.strip()
            recipientEmail.append(str(line))
    #ADD DATE HERE IN FUTURE
    subject = "Today's Menu"
    msg = MIMEMultipart()
    msg['From'] = myEmail
    msg['To'] = ", ".join(recipientEmail)
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    server = smtplib.SMTP('127.0.0.1', smtpCode)
    server.starttls()
    server.login(myEmail, myPassword)
    text = msg.as_string()
    server.sendmail(myEmail, recipientEmail, text)
    server.quit()


if __name__ == "__main__":
    main()
>>>>>>> 4a3badd... Organized code, now has separate config and email list files
