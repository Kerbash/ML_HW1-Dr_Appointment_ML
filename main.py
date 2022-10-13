"""

Data Index
0 = PatientID
1 = AppointmentID
2 = Gender
3 = Day of appointment
4 = Date of registration for appointment
5 = Age
6 = Neighbourhood, Where the appoint takes place
7 =  Scholarship
8 = Hipertension
9 = Diabetes
10 = Alcoholism
11 = Handicap
12 = Text Recived
13 = No show

"""
import numpy as np
import datetime

# name of the data sheet
FILE_NAME = "data.csv"

# load the and process the dataset
with open(FILE_NAME, "r") as f:
    data_set = f.read()

# process the data
data_set = data_set.split("\n")
# remove header and trailing blank
del data_set[0]
del data_set[-1]
temp = data_set
data_set = []
for item in temp:
    data_set.append(item.split(','))

data_set = np.asarray(data_set)


# Tokenized different value into numbers
# 4 tokenization
# - Gender to binary 0 dude 1 lady
# - 2 dates seconds since 2000
# - Location
def tokenizer(data_set, index_num):
    """
    turn variable into numbers base on uniqueness
    :param data_set: the array being manipulated
    :param index_num: the location of the element
    :return: key and modified array
    """
    key = {}
    counter = 0
    for array in data_set:
        # check if its a new label
        try:
            array[index_num] = key[array[index_num]]
        except KeyError:
            key[array[index_num]] = counter
            array[index_num] = counter
            counter += 1

    # turn hashed dictionary into array
    output_key = [None] * (counter)
    for k in key.keys():
        output_key[key[k]] = k

    return output_key

def timeToSecond(data_set, index_num):
    for array in data_set:
        time = datetime.datetime.strptime(array[index_num], "%Y-%m-%dT%H:%M:%SZ")
        time = time - datetime.datetime(2015, 0, 0, 0, 0)
        print(time)


# tokenized the two string field gender and location
gender_key = tokenizer(data_set, 2)
place_key = tokenizer(data_set, 6)

timeToSecond(data_set, 3)
timeToSecond(data_set, 4)
