import time
from selenium import webdriver
from getpass import getpass

driver=webdriver.Chrome('chromedriver.exe')

regulamin='/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]'


login=input("Podaj swój login:\n")
password=getpass("Podaj swoje hasło:\n")
person=input("Podaj osobę lub grupę gdzie chcesz wysłać wiadomość:\n")
message=input("Podaj jaką wiadomość chcesz wysyłać:\n")
count=int(input("Ile wiadomości chcesz wysłać:\n"))
timet=int(input("Podaj co ile sekund ma się wysyłać wiadomość:\n"))


def findByXpath(xpath):
    global driver
    elementy=driver.find_elements("xpath",xpath)
    while len(elementy)==0:
        time.sleep(0.5)
        elementy=driver.find_elements("xpath",xpath)
    print(elementy[0])
    return elementy[0]
def exception():
    global driver
    elementy=driver.find_elements("xpath",'/html/body/div/div/div/div[1]/div/div[2]/div/div/form/div[1]/div[1]')
    while len(elementy)!=0:
        time.sleep(0.5)
        print("Błędne loginy!")
        login=input("Podaj ponownie swój login:\n")
        password=input("Podaj ponownie swoje hasło:\n")
        findByXpath('//input[@name=\"email\"]').clear()
        findByXpath('//input[@name=\"pass\"]').clear()
        findByXpath('//input[@name=\"email\"]').send_keys(login)
        findByXpath('//input[@name=\"pass\"]').send_keys(password)
        findByXpath('//button[@name=\"login\"]').click()
        elementy=driver.find_elements("xpath",'/html/body/div/div/div/div[1]/div/div[2]/div/div/form/div[1]/div[1]')
    print('zalogowano!')
    
def login_in():
    driver.get('https://www.messenger.com/login/')
    findByXpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]').click()
    findByXpath('//input[@name=\"email\"]').send_keys(login)
    findByXpath('//input[@name=\"pass\"]').send_keys(password)
    findByXpath('//button[@name=\"login\"]').click()
    exception()
def send():
    global timet
    i = 0
    while i<count:
        findByXpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]').send_keys(message)
        findByXpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/span[2]/div').click()
        i=i+1
        time.sleep(timet)
if len(login)!=0 and len(password)!=0:
    login_in()
else:
    print('Podaj Swoje haslo i login')
agree='nie'
while agree=='nie':
    findByXpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div/div/label/input').send_keys(person)
    findByXpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]').click()
    agree=input('Czy to do tej osoby chcesz wysłać spam?\ntak/nie\n')
    if agree=='nie':
        findByXpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div/div/label/input').clear()
        person=input("Podaj Ponownie osobę lub grupę gdzie chcesz wysłać wiadomość:\n")
send()

