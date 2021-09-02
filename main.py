import sys
import time
import datetime
import csv
import re
import graph
import timer

# Getting The date 
now = datetime.datetime.now()
current_day = now.strftime("%Y-%m-%d")

# The file name that the data will be stored
filename = "pomodoro_records.csv"
#Validated Prompts
valid_prompts = ["timer","t","rest","r","graph","g","records","rec","quit","q",
"res","reset"]

# Defining the functions
#This will show the count
def record():
    reader_rows = []
    with open(filename,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            reader_rows.append(row)
        
        print(reader_rows[0][0],"       ",reader_rows[0][1])
        for row in reader_rows[1:]:
            print(row[0],"   ",row[1])

#This will reset the count
def resetf():
    fields = ["Date","Count"]
    with open(filename,"w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
    print("Count was reset.\n")

#Exiting From The program
def quit():
    print("Have a happy day")
    sys.exit()

#Mainting All the tasks
def main(prm):
    global prompt
    if prm == "t" or prm == "timer":
        timer.timerf()
        prompt = input(":> ")
        prompt = re.sub("\W|\d","",prompt).lower()
        while prompt not in valid_prompts:
            print("You Typed Sth Wrong!")
            prompt = input(":> ")
            prompt = re.sub("\W|\d","",prompt).lower()
            if prompt in valid_prompts:
                break
    elif prm == "rec" or prm == "records":
        record()
        prompt = input(":> ")
        prompt = re.sub("\W|\d","",prompt).lower()
        while prompt not in valid_prompts:
            print("You Typed Sth Wrong!")
            prompt = input(":> ")
            prompt = re.sub("\W|\d","",prompt).lower()
            if prompt in valid_prompts:
                break
    elif prm == "g" or prm == "graph":
        graph.graphf()
        prompt = input(":> ")
        prompt = re.sub("\W|\d","",prompt).lower()
        while prompt not in valid_prompts:
            print("You Typed Sth Wrong!")
            prompt = input(":> ")
            prompt = re.sub("\W|\d","",prompt).lower()
            if prompt in valid_prompts:
                break

    elif prm == "res" or prm == "reset":
        resetf()
        prompt = input(":> ")
        prompt = re.sub("\W|\d","",prompt).lower()
        while prompt not in valid_prompts:
            print("You Typed Sth Wrong!")
            prompt = input(":> ")
            prompt = re.sub("\W|\d","",prompt).lower()
            if prompt in valid_prompts:
                break
    elif prm == "q" or prm == "quit":
        quit()

#Contorling The flow of Program
def runf():
    global prompt
    prompt = input(":> ")
    prompt = re.sub("\W|\d","",prompt).lower()
    while prompt not in valid_prompts:
        print("You Typed Sth Wrong!")
        prompt = input(":> ")
        prompt = re.sub("\W|\d","",prompt).lower()
        if prompt in valid_prompts:
            break
    while prompt in valid_prompts:
        main(prompt)


# Things that will be printed every time application starts
print("\nWelcome to my pomodoro app :)\n")
print("""\nHere is a guide:
- Enter \"timer\" or \"t\" for Timer
- Enter \"graph\" or \"g\" for making a graph from your pomodoro count
- Enter \"records\" or \"rec\" for showing your pomodoro records
- Enter \"reset\" or \"res\" to reset the records
- Enter \"quit\" or \"q\" to exit from program""")

runf()






