import csv
from datetime import datetime



with open('sample_csv.csv') as csv_data:
    reader = csv.reader(csv_data, delimiter=',')
    first_line = reader.next() #if you want to skip first line

    # sorting with date
    days_sorted = sorted(reader, key=lambda day: datetime.strptime(day[0], "%Y-%m-%d"), reverse=True)
    print days_sorted
    # reader is the csv data
    # day[0] is the first column here(you change which one you want)
    # reverse = False/True change this to get ascn/descn
    # days_sorted will give you sorted list by days

    # sorting with number
    number_sorted = sorted(reader, key=lambda x:int(x[1]), reverse=True)
    print number_sorted
    # reader is the csv data
    # x[1] is the second column here(you change which one you want)
    # reverse = False/True change this to get ascn/descn
    # number_sorted will give you sorted list by numbers

