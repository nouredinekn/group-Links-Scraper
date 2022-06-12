# 22
import os
import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import urllib
import datetime
# colors


class colors:
    R = '\033[91m'  # Red
    G = '\033[92m'  # Green
    Y = '\033[93m'  # Yellow
    B = '\033[94m'  # Blue
    P = '\033[95m'  # Purple
    C = '\033[96m'  # Cyan
    W = "\033[1;37m"  # White
    bold = '\033[1m'
    unbold = '\033[0m'


if datetime.datetime.now().date() > datetime.date(month=6, year=2022, day=12):
    print(colors.R, 'tool have expired ')
    sleep(2)
    exit()


def generatorCase(x):
    num = '0987654321'
    case = 'qwertyuiopasdfghjklzxcvbnm'
    uppercase = case.upper()
    geneCase = num+uppercase+case
    rancass = ''.join(random.choice(geneCase) for i in range(x))
    return rancass


# whatsapClass
class whatsapGroup:
    def __init__(self, x=''):
        self.__url = f'https://chat.whatsapp.com/invite/{x}'

    def __whatGroup(self):
        content = urllib.request.urlopen(self.__url)
        soup = BeautifulSoup(content, 'html.parser')
        return str(soup.find_all(class_="_9vd5 _9scr")[0].encode("utf-8")).split('>')[1].split('<')[0]

    def whatGroupchecker(self):
        if self.__whatGroup():
            return True
        else:
            return False

    def urlGetter(self):
        return self.__url

    def groupName(self):
        if self.__whatGroup():
            return self.__whatGroup()
        else:
            return 'Error, this group not found'

    def groupSaveAsText(self):
        __done = f'''
        ============ Group  Worked =========
        group Url: {self.urlGetter()}
        group Name: {self.groupName()}
        tool dev by : t.me/n2k4n
        =================Nouredienkn========
        \n
        '''
        open('groupsWhatspp.txt', 'a').write(__done)

    def groupSaveAsBot(self, tok='', chatId=''):
        __done = f'''
        ============ Group  Worked =========
        group Url: {self.urlGetter()}
        group Name: {self.groupName()}
        tool dev by : @n2k4n
        =================Nouredienkn========
        \n
        '''
        requests.post(
            f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={chatId}&text={__done}')

# telegram Class


class telegramGroup:
    def __init__(self, x):
        self.__url = f'https://t.me/+{x}'
        self.content = urllib.request.urlopen(self.__url)
        self.soup = BeautifulSoup(self.content, 'html.parser')

    def __tgGroup(self):
        try:
            return str(self.soup.find_all(class_="tgme_page_title")[0].encode("utf-8")).split('>')[2].split('<')[0]
        except:
            return 0

    def tgGroupChcker(self):
        if self.__tgGroup():
            return True
        else:
            return False

    def tgsubscribers(self):
        if self.tgGroupChcker():
            return str(self.soup.find_all(class_='tgme_page_extra')[0].encode("utf-8")).split('>')[1].split('<')[0]
        else:
            return ' Error <Group Not Found> '

    def tgGroupName(self):
        if self.tgGroupChcker():
            return self.__tgGroup()
        else:
            return 'Error  <Group Not Found>'

    def urlGetter(self):
        return self.__url

    def groupSaveAsText(self):
        __done = f'''
        ============ Group  Worked =========
        group Url: {self.urlGetter()}
        group Name: {self.tgGroupName()}
        subscribers: {self.tgsubscribers()}
        tool dev by : t.me/n2k4n
        =================Nouredienkn========
        \n
        '''
        open('groupsTelegram.txt', 'a').write(__done)

    def groupSaveAsBot(self, tok='', chatId=''):
        __done = f'''
        ============ Group  Worked =========
        group Url: {self.urlGetter()}
        group Name: {self.tgGroupName()}
        subscribers: {self.tgsubscribers()}
        tool dev by : @n2k4n
        =================Nouredienkn========
        \n
        '''
        requests.post(
            f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={chatId}&text={__done}')


def one():
    x = whatsapGroup(generatorCase(22))
    if x.whatGroupchecker():
        msg = f'''{colors.G}
        ---> GOOD 
        ---> {colors.C}MSG:{colors.G} WORKED
        ---> {colors.C}URL : {colors.P}{x.urlGetter()} {colors.G}
        ---> {colors.C}NAME: {colors.P} {x.groupName()}
        {colors.W}
        '''
        x.groupSaveAsText()
        print(msg)
    else:
        msg = f'''{colors.R}
        ---> BAD  
        ---> MSG: NOT FOUND
        ---> URL : {colors.C}{x.urlGetter()} 
        {colors.W}
        '''
        print(msg)


def two():
    x = telegramGroup(generatorCase(16))
    if x.tgGroupChcker():
        msg = f'''{colors.G}
        ---> GOOD 
        ---> {colors.C}MSG:{colors.G} WORKED
        ---> {colors.C}URL : {colors.P}{x.urlGetter()} {colors.G}
        ---> {colors.C}NAME: {colors.P} {x.tgGroupName()}{colors.G}
        --->{colors.C}subscribers: {colors.P} {x.tgsubscribers()}
        {colors.W}
        '''
        x.groupSaveAsText()
        print(msg)
    else:
        msg = f'''{colors.R}
        ---> BAD  
        ---> MSG: NOT FOUND
        ---> URL : {colors.C}{x.urlGetter()} 
        {colors.W}
        '''
        print(msg)


def oneb(chatid, tok):
    x = whatsapGroup(generatorCase(22))
    if x.whatGroupchecker():
        msg = f'''{colors.G}
        ---> GOOD 
        ---> {colors.C}MSG:{colors.G} WORKED
        ---> {colors.C}URL : {colors.P}{x.urlGetter()} {colors.G}
        ---> {colors.C}NAME: {colors.P} {x.groupName()}
        {colors.W}
        '''
        x.groupSaveAsBot(chatId=chatid, tok=tok)
        print(msg)
    else:
        msg = f'''{colors.R}
        ---> BAD  
        ---> MSG: NOT FOUND
        ---> URL : {colors.C}{x.urlGetter()} 
        {colors.W}
        '''
        print(msg)


def twob(chatid, tok):
    x = telegramGroup(generatorCase(16))
    if x.tgGroupChcker():
        msg = f'''{colors.G}
        ---> GOOD 
        ---> {colors.C}MSG:{colors.G} WORKED
        ---> {colors.C}URL : {colors.P}{x.urlGetter()} {colors.G}
        ---> {colors.C}NAME: {colors.P} {x.tgGroupName()}{colors.G}
        --->{colors.C}subscribers: {colors.P} {x.tgsubscribers()}
        {colors.W}
        '''
        x.groupSaveAsBot(chatId=chatid, tok=tok)
        print(msg)
    else:
        msg = f'''{colors.R}
        ---> BAD  
        ---> MSG: NOT FOUND
        ---> URL : {colors.C}{x.urlGetter()} 
        {colors.W}
        '''
        print(msg)


def lis():
    return f'''{colors.C} 
 ███████████                                                      
░█░░░███░░░█                                                      
░   ░███  ░   ███████            █████ ███ █████  ██████          
    ░███     ███░░███ ████{colors.B}██████░░███ ░███░░███  ░░░░░███         
    ░███    ░███ ░███░░░░░░░░░░  ░███ ░███ ░███   ███████         
    ░███    ░███ ░███            ░░███████████   ███░░███         
    █████   ░░███████             ░░████░████   ░░████████        
   ░░░░░     ░░░░░{colors.C}███              ░░░░ ░░░░     ░░░░░░░░         
             ███ ░███                                             
            ░░██████                                              
             ░░░░░░                                               
                                                                                                                   
  █████   ██████  ████████   ██████   ████████   ██████  ████████ 
 ███░░   ███░░███░░███░░███ ░░░░░███ ░░███░░███ ███░░███░░███░░███
░░█████ ░███ ░░░  ░███ ░░░   ███{colors.B}████  ░███ ░███░███████  ░███ ░░░ 
 ░░░░███░███  ███ ░███      ███░░███  ░███ ░███░███░░░   ░███     
 ██████ ░░██████  █████    ░░████████ ░███████ ░░██████  █████    
░░░░░░   ░░░░░░  ░░░░░      ░░░░░░░░  ░██{colors.C}█░░░   ░░░░░░  ░░░░░     
                                      ░███                        
                                      █████                       
                                     ░░░░░            
                                            
        {colors.bold} {colors.Y} [ {colors.R}! {colors.Y}] {colors.P} DEV BY:  {colors.G} NOUREDINE KN 
        {colors.bold} {colors.Y} [ {colors.R}! {colors.Y}] {colors.P}TG-USER:  {colors.G} t.me/n2k4n
        {colors.bold}{colors.Y} [ {colors.R}! {colors.Y}] {colors.P}github: {colors.G}  github.com/nouredinekn
        {colors.bold}{colors.Y} [ {colors.R}! {colors.Y}] {colors.P}DATE: {colors.G}{datetime.datetime.now().date()}
'''


print(lis())
sleep(2)


def li():
    print(f'{colors.R}=========================================================================')
    sleep(1)
    print(
        f'{colors.bold} {colors.Y} [{colors.R}1{colors.Y}] {colors.B} WHATSAPP GROUP SCRAPER')
    sleep(1)
    print(
        f'{colors.bold} {colors.Y} [{colors.R}2{colors.Y}] {colors.B} Telegram GROUP SCRAPER')
    sleep(1)
    print(
        f'{colors.bold} {colors.Y} [{colors.R}3{colors.Y}] {colors.B} Telegram And WHATSAPP ')
    sleep(1)
    print(
        f'{colors.bold} {colors.Y} [{colors.R}4{colors.Y}] {colors.B} Exit''')
    sleep(1)
    print(f'{colors.R}=========================================================================')
    sleep(1)


li()
chas = int(input(
    f'{colors.bold} {colors.Y}[ {colors.R}! {colors.Y}] {colors.G} ===>  {colors.B}\t'))


def clear():
    os.system('cls')
    os.system('clear')


if chas == 4:
    exit()
sleep(5)
clear()


def li2():
    print(f'{colors.R}=========================================================================')
    sleep(1)
    print(
        f'{colors.bold} {colors.Y} [{colors.R}1{colors.Y}] {colors.B} save as text')
    sleep(1)
    print(
        f'{colors.bold} {colors.Y} [{colors.R}2{colors.Y}] {colors.B} save as bot')
    sleep(1)
    print(f'{colors.R}=========================================================================')
    sleep(1)


print(lis())
li2()
chas2 = int(input(
    f'{colors.bold} {colors.Y}[ {colors.R}! {colors.Y}] {colors.G} ===>  {colors.B}\t'))

clear()

# text
if chas == 1 and chas2 == 1:
    while True:
        one()
if chas == 2 and chas2 == 1:
    while True:
        two()
if chas == 3 and chas2 == 1:
    while True:
        one()
        two()

# bot
if chas == 1 and chas2 == 2:
    tok = input(
        f'{colors.bold} {colors.Y}[ {colors.R}! {colors.Y}] {colors.G} ENTRE YOUR BOT TOKEN ===>  {colors.B}\t')
    chatid = input(
        f'{colors.bold} {colors.Y}[ {colors.R}! {colors.Y}] {colors.G}ENTRE YOUR ID ===>  {colors.B}\t')
    while True:
        oneb(tok=tok, chatid=chatid)
if chas == 2 and chas2 == 2:
    tok = input(
        f'{colors.bold} {colors.Y}[ {colors.R}! {colors.Y}] {colors.G} ENTRE YOUR BOT TOKEN ===>  {colors.B}\t')
    chatid = input(
        f'{colors.bold} {colors.Y}[ {colors.R}! {colors.Y}] {colors.G}ENTRE YOUR ID ===>  {colors.B}\t')
    while True:
        twob(tok=tok, chatid=chatid)
if chas == 3 and chas2 == 2:
    tok = input(
        f'{colors.bold} {colors.Y}[ {colors.R}! {colors.Y}] {colors.G} ENTRE YOUR BOT TOKEN ===>  {colors.B}\t')
    chatid = input(
        f'{colors.bold} {colors.Y}[ {colors.R}! {colors.Y}] {colors.G}ENTRE YOUR ID ===>  {colors.B}\t')

    while True:
        oneb(tok=tok, chatid=chatid)
        twob(tok=tok, chatid=chatid)
