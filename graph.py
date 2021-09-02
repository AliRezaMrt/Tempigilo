import matplotlib.pyplot as plt
import csv
import datetime

# Getting The date 
now = datetime.datetime.now()
current_day = now.strftime("%Y-%m-%d")

# The file name that the data will be stored
filename = "pomodoro_records.csv"

#This will make a plot from counts
def graphf():
    #Reading the data from the file
    reader_rows = []
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            reader_rows.append(row)
    #Making The plot
    fields = reader_rows[0]
    rows = reader_rows[1:len(reader_rows)]
    Labels = fields
    Dates = [row[0] for row in rows]
    counts = [int(row[1]) for row in rows]
    plt.bar(Dates, counts)
    plt.title('Pomodoro Counts')
    plt.xlabel(Labels[0])
    plt.ylabel(Labels[1])
    plt.show()
