from aocd import get_data
import os

token = os.getenv('AOC_SESSION')

fetch_date = 1
fetch_year = 2023

def make_data_file(fetch_date, path):
    data = get_data(day=fetch_date, year=2023)
    filename = path + "/data.txt"

    with open(filename, 'w')as output:
        output.write(data)

# \fetch_year exists?
if os.path.isdir(str(fetch_year)):
    parent_dir = str(fetch_year)
    path = parent_dir + '/Day_' + str(fetch_date)
    # \fetch_year\fetch_date exists?
    if os.path.isdir(path):
        make_data_file(fetch_date, path)
    else:
        os.mkdir(path)
        #path = path + '/Day_' + str(fetch_date)
        make_data_file(fetch_date, path)
else:
    os.mkdir(str(fetch_year))
    parent_dir = str(fetch_year)
    path = parent_dir + '/Day_' + str(fetch_date)
    os.mkdir(path)
    path = path + '/Day_' + str(fetch_date)
    make_data_file(fetch_date, path)
