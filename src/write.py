import csv
import os

# only this function can be called by other files
# calling other functions may result undefined behavior
def writeToCSVFiles(respondent, rating, ID):
    writeToRespondent(respondent)
    writeToRating(rating, ID, 4)


# ['age','gender','education level','ip address', 'mturk-id']
def writeToRespondent(respondent):
    if(len(respondent) != 5):
        print("Respondent data misMatch. Expected: 5, Given: " + str(len(respondent)))
        print("The given data is: " + respondent)
        return

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "../userResponseData/", 'Respondent.csv')
    with open(filename, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(respondent)


# ['mturk-id','algorithm','query','rating','time spent']
def writeToRating(rating, ID, num):
    if (len(rating) != 160):
        print("Rating data misMatch. Expected: 160, Given: " + str(len(rating)))
        return

    rating = [rating[x:x+num] for x in range(0, len(rating), 4)]
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "../userResponseData/", 'UserRating.csv')
    with open(filename, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for i in range(40):
            current = rating[i]
            current.insert(0,ID)
            writer.writerow(current)

    """
    print(len(rating))
    print(rating[0])
    """






