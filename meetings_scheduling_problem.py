"""
Given n rooms and m meetings (all meetings in the same day), write an algorithm to determine if all meetings can be scheduled.

Example 1: n = 1, meetings = [[1,2],[2,3]], return True
Example 2: n = 1, meetings = [[1,2],[1,3]], return False
Example 3: n = 2, meetings = [[1,2],[1,3]], return True

The meetings list contains sublists with contents: [startTime, endTime]
"""

def schedule_check(meetings_list, n_rooms):
    """
    input var
    meetings_list - contains a sublist of meeting times in format [startTime, endTime]
    n_rooms - number of meeting rooms available

    output var
    True/False - stating if a there are enough rooms for all meetings
    """

    time_frequencies = {}

    for subList in meetings_list:

        for hour in range(subList[0], subList[1]+1):

            # increment hour in dictionary if it already exists
            if hour in time_frequencies:
                time_frequencies[hour] += 1

            # intialise hour in dictionary
            else:
                time_frequencies[hour] = 1

    ## Check if frequencies is ok
    for frequency in list(time_frequencies.values()):
        if frequency > n_rooms:
            return(False)

    return(True)


def main():

    meetings = [[1,2],[1,3],[3,5]] ## meeting times
    n = 2 ## number of meeting rooms

    print(schedule_check(meetings,n))


if __name__ == "__main__":
    main()