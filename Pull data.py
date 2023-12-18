from aocd import get_data
import os

os.environ["AOC_SESSION"] = '53616c7465645f5f34f19f0a2e183853db7a905f9408a576b69bd803d00a46dce7cd9fcc857e79661ee08f33deb38043a666390fe6682180d86c316c6c3d241a'
token = os.getenv('AOC_SESSION')
#print(token)




fetch_date = 1
fetch_year = 2023

def make_data_file(fetch_date):

    data = get_data(day=fetch_date, year=2023)

    filename = path + 'Day_' + str(fetch_date) + ".txt"

    with open(filename, 'w')as output:
        output.write(data)

if os.path.isdir(str(fetch_year)):
    parent_dir = str(fetch_year)
    path = parent_dir + '/' + str(fetch_date)
    if os.path.isdir(path):
        # make file
        make_data_file(fetch_date)
    else:
        os.mkdir(path)
        #make file
        path = path + 'Day_' + str(fetch_date)
        make_data_file(fetch_date)
else:
    os.mkdir(str(fetch_year))
    parent_dir = str(fetch_year)
    path = parent_dir + '/' + str(fetch_date)
    os.mkdir(path)



'''

directory = str(fetch_year) +  '/Day' + str(fetch_date)
parent_dir = 'C:/Users/user/Advent-of-code/Advent-of-code'

path  = os.path.join(parent_dir, directory)

os.mkdir(path)


'''