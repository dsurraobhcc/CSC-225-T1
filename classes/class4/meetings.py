# 1. Complete the code below:
# a. Create a 'Meeting' class that stores the following information 
# about an event in your calendar: title, location, start time, end time

# b. Instantiate the following events using this class and add them to a list
# Doctor appointment, MGH, 10/18/2020 9-10 am
# Soccer practice, BU athletic field, 9/1/2020 5-7pm
# Foliage trip, Berkhires, 11/24/2020 - 11/25/2020

# c. Implement the special method __lt__ that compares start times of two 
# Meeting objects (this should be only one line of code!).

# d. Sort the above meeting list to check if this method works.

# Hint: datetime(2019, 5, 18, 15, 17) represent a time '2019-05-18T15:17:00'

from datetime import datetime

class Meeting(object):
    #TODO: implement the constructor
    def __init__(self, title, location, start_time, end_time):
        self.title = title
        self.location = location
        self.start_time = start_time
        self.end_time = end_time

    #TODO: implement this method
    def __lt__(self, other):
        return self.start_time < other.start_time

    def __str__(self):
        return self.title + ', ' + self.location + ', ' \
            + datetime.__str__(self.start_time) + ', ' \
                + datetime.__str__(self.end_time)

#TODO: instantiate three instances of the above class using data in b.
m1 = Meeting('Doctor appointment', 'MGH', \
    datetime(2020, 10, 18, 9), datetime(2020, 10, 18, 10))
m2 = Meeting('Soccer practice', 'BU athletic field', \
    datetime(2020, 9, 1, 17), datetime(2020, 9, 1, 17))
m3 = Meeting('Foliage trip', 'Berkshires', \
    datetime(2020, 11, 24), datetime(2020, 11, 25))

#TODO: create a list, sort it using list.sort(), and print meetings in the list
meetings = [m1, m2, m3]
meetings.sort()
for meeting in meetings:
    print(meeting)