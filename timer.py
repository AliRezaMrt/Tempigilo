import time
import datetime
import csv
import re

# Getting The date 
now = datetime.datetime.now()
current_day = now.strftime("%Y-%m-%d")


# Declaring a variable for counting pomodoros
pomodoro_count = 0

# The file name that the data will be stored
filename = "pomodoro_records.csv"

#This will make timer
def timerf():
    global pomodoro_count
    # input time in Minutes
    t = input("Enter the time in minutes: ")
    t = int(re.sub("\D","",t)) * 60
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        def_text = "               =====     {}     =====               ".format(timer)
        print(def_text, end="\r")
        time.sleep(1)
        t -= 1
    print("\n")
    pomodoro_count += 1
    print('Pomodoro is Complete!')
    
    #Saving The counts into the file
    reader_rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            reader_rows.append(row)
    if reader_rows[len(reader_rows)-1][0] == current_day:
        print(current_day," >>> ",pomodoro_count)
        last_count = int(reader_rows[len(reader_rows)-1][1])
        last_count += pomodoro_count
        reader_rows[len(reader_rows)-1][1] = str(last_count)
        with open(filename,"w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(reader_rows)
    else:
        rows = [[current_day,pomodoro_count]]
        print(current_day," >>> ",pomodoro_count)
        # writing to csv file
        with open(filename, 'a') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the data rows
            csvwriter.writerows(rows)
