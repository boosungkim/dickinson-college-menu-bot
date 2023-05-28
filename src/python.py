import datetime
# import schedule
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from configparser import ConfigParser
import re

#CHANGE TO A SOLID TIMEZONE TIME

def getLink():
    currentDatetimeRaw = datetime.datetime.today()
    currentDatetime = str(currentDatetimeRaw)
    
    todayDate = currentDatetime[:10]
    yr = currentDatetime[2:4]
    mo = currentDatetime[5:7]
    if mo[0] == "0":
        mo = currentDatetime[6]
    da = currentDatetime[8:10]
    if da[0] == "0":
        da = currentDatetime[9]
    #use date to get website number
    link = "https://www.dickinson.edu/site/custom_scripts/dc_dining_menus_index.php?yr={}&mo={}&da={}".format(yr,mo,da)
    return [link, todayDate]


def getMenu(a_link):
    #Grab data
    page = requests.get(a_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    #convert list elements into string
    overallRaw = soup.select("div p")
    overallStr = [str(i) for i in overallRaw]
    #Isolate Dining Hall menu
    indices = [i for i, x in enumerate(overallStr) if x == '<p><span style="color:#666;">Lunch</span></p>']
    print(indices)
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


def getUnion(a_link):
    #Grab data
    page = requests.get(a_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    #convert list elements into string
    overallRaw = soup.select("div p")
    overallStr = [str(i) for i in overallRaw]
    #Isolate Dining Hall menu
    indices = [i for i, x in enumerate(overallStr) if x == '<p><span style="color:#666;">Lunch</span></p>']
    # toRemove = indices[1]
    isolatedRawUnion = overallRaw[indices[1]:indices[2]]
    isolatedStrUnion = overallStr[indices[1]:indices[2]]
    # Divide into sections
    lcStart = isolatedStrUnion.index('<p><span style="color:#666;">Lunch</span></p>')
    dnStart = isolatedStrUnion.index('<p><span style="color:#666;">Dinner</span></p>')
    
    # breakfastRawList = isolatedRawMenu[0:lcStart]
    lunchRawListU = isolatedRawUnion[lcStart:dnStart]
    dinnerRawListU = isolatedRawUnion[dnStart:]
    # Final lists
    lunchStrListU = []
    dinnerStrListU = []
    #Lunch String List
    for j in lunchRawListU:
        lunchStrListU.append(str(j.get_text()))
    #Dinner String List
    for k in dinnerRawListU:
        dinnerStrListU.append(str(k.get_text()))
    return [lunchStrListU, dinnerStrListU]


def getKove(a_link):
    #Grab data
    page = requests.get(a_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    #convert list elements into string
    overallRaw = soup.select("div p")
    overallStr = [str(i) for i in overallRaw]
    #Isolate Dining Hall menu
    indices = [i for i, x in enumerate(overallStr) if x == '<p><span style="color:#666;">Lunch</span></p>']
    isolatedRawKove = overallRaw[indices[2]:]
    isolatedStrKove = overallStr[indices[2]:]
    # Divide into sections
    lcStart = isolatedStrKove.index('<p><span style="color:#666;">Lunch</span></p>')
    dnStart = isolatedStrKove.index('<p><span style="color:#666;">Dinner</span></p>')
    
    # breakfastRawList = isolatedRawMenu[0:lcStart]
    lunchRawListK = isolatedRawKove[lcStart:dnStart]
    dinnerRawListK = isolatedRawKove[dnStart:-1]
    # Final lists
    lunchStrListK = []
    dinnerStrListK = []
    #Lunch String List
    for j in lunchRawListK:
        lunchStrListK.append(str(j.get_text()))
    #Dinner String List
    for k in dinnerRawListK:
        dinnerStrListK.append(str(k.get_text()))
    return [lunchStrListK, dinnerStrListK]


def formatMenu(stringList):
    formattedMenu = ""
    for ln in stringList:
        if ln == "Breakfast":
            formattedMenu = "---Breakfast---"
        elif ln == "Lunch":
            formattedMenu = "---Lunch---"
        elif ln == "Dinner":
            formattedMenu = "---Dinner---"
        else:
            f_ln = re.compile(ln)
            f_ln = re.sub(":", ": ", ln)
            f_ln_2 = re.sub("w/", "with ", f_ln)
            f_ln_3 = re.sub("&", "and", f_ln_2)
            formattedMenu = formattedMenu + "\n {}".format(f_ln_3)
    return formattedMenu


def formatUnion(stringList):
    formattedUnion = ""
    for wn in stringList:
        if wn == "Lunch":
            formattedUnion = "---Lunch---"
        elif wn == "Dinner":
            formattedUnion = "---Dinner---"
        else:
            f_ln = re.compile(wn)
            f_ln = re.sub(":", ": ", wn)
            f_ln_2 = re.sub("w/", "with ", f_ln)
            f_ln_3 = re.sub("&", "and", f_ln_2)
            formattedUnion = formattedUnion + "\n {}".format(f_ln_3)
    return formattedUnion


def formatKove(stringList):
    formattedKove = ""
    for kn in stringList:
        if kn == "Lunch":
            formattedKove = "---Lunch---"
        elif kn == "Dinner":
            formattedKove = "---Dinner---"
        else:
            f_kn = re.compile(kn)
            f_kn = re.sub(":", ": ", kn)
            f_kn_2 = re.sub("w/", "with ", f_kn)
            f_kn_3 = re.sub("&", "and", f_kn_2)
            formattedKove = formattedKove + "\n {}".format(f_kn_3)
    return formattedKove


def main():
    menuLink = getLink()
    threeMeals = getMenu(menuLink[0])
    breakfast = formatMenu(threeMeals[0])
    lunch = formatMenu(threeMeals[1])
    dinner = formatMenu(threeMeals[2])

    mUnion = getUnion(menuLink[0])
    lunchU = formatUnion(mUnion[0])
    dinnerU = formatUnion(mUnion[1])

    mKove = getKove(menuLink[0])
    lunchK = formatKove(mKove[0])
    dinnerK = formatKove(mKove[1])
    message = "Hello, I am Boo Sung Kim's Dickinson Menu Bot V1.0.0\n\n" + "Today's Dining Hall menu is:\n" + breakfast + "\n" + lunch + "\n" + dinner + "\n\n\n" + "Today's Union Station menu is:\n" + lunchU + "\n" + dinnerU + "\n\n\n" + "Today's Kove menu is:\n" + lunchK + "\n" + dinnerK + "\n\n" + "Have a nice day! \n" + "Project GitHub link: https://github.com/boosungkim/Dickinson_Menu_Bot"
    parser = ConfigParser()
    parser.read('config.ini')
    # Getting info to log in
    myEmail = str(parser.get('SensitiveData', 'myEmail'))
    myPassword = str(parser.get('SensitiveData', 'myPassword'))
    hostName = str(parser.get('SensitiveData', 'hostName'))
    smtpCode = int(parser.get('SensitiveData', 'smtpCode'))
    subject = "{} Dickinson Dining Menu".format(menuLink[1])

    recipientEmail = []
    with open('email.txt', 'r') as f:
        for line in f:
            line = line.strip()
            recipientEmail.append(str(line))
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


# if __name__ == "__main__":
#     main()