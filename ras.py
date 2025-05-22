import json
import pyautogui as py


def save_question() -> bool:
    question = input("You want to save this (y/n) ? ")
    if question == "y":
        return True
    else:
        return False

passwd = "Guiomar1@"

file_name = "dados.json"

try:
    with open(file_name, "r") as file:
        data = json.load(file)

except FileNotFoundError:
    data = []



while True:

    datas = input("Write here the RAs or 'q'to quit: ")

    if datas == "q":
        break

    datas2 = {
        "Ra":datas, 
        "Password":passwd}

    data.append(datas2)

if save_question() == True:
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


































