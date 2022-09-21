import time as t
import datetime as dt

all_people=[]
people=''
def form():
    global people
    while people!='stop':
        print('Aby przerwać wpisywanie wpisz "stop"')
        people=input('Podaj osobę do której chcesz wysyłać wiadomość:\n')
        if people!='stop':
            all_people.append(people)
        else:
            pass
    print(all_people)
form()