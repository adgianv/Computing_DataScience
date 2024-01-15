##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

def count_simba(list):
    str = 'Simba'
    counter = 0
    for i in list:
        count = i.count(str)
        counter += count
    return counter

# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

import pandas as pd
from datetime import date

def get_day_month_year(date_list):
    day_list = [date.day for date in date_list]
    month_list = [date.month for date in date_list]
    year_list = [date.year for date in date_list]

    data = {'day': day_list, 'month': month_list, 'year': year_list}
    return pd.DataFrame(data)

# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

from geopy.distance import geodesic

def compute_distance (location_list):
    distance_list = []
    for location in location_list:
        coordinate_1, coordinate_2 = location
        measure = geodesic(coordinate_1, coordinate_2).kilometers
        distance_list.append(measure)
    return distance_list

#################################################
# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#

def sum_general_int_list(list_1):
    to_sum = []
    for i in list_1:
        if type(i) is int:
            to_sum.append(i)
        elif type(i) is list:
            to_sum.append(sum_general_int_list(i))
    return sum(to_sum)
