import itertools
import csv
from datetime import datetime
from collections import namedtuple

filename1 = "personal_info.csv"
filename2 = "employment.csv"
filename3 = "vehicles.csv"
filename4 = "update_status.csv"


#reading from files
def readfiles(filename):
    with open(filename) as f:
        rows = csv.reader(f,delimiter=',',quotechar='"')
        for item in rows:
            yield cleaner(item)


personal_info = readfiles(filename1)
employment = readfiles(filename2)
vehicles = readfiles(filename3)
update_status = readfiles(filename4)


def cleaner(lst):
    lst = [item.replace('-','_') for item in lst]
    for i in range(len(lst)):
        try:
            lst[i] = int(lst[i])
        except ValueError:
            try:
                lst[i] = datetime.strptime(lst[i],'%Y_%m_%dT%H:%M:%SZ')
            except ValueError:
                continue
    return lst


#for item in itertools.islice(itertools.chain(personal_info,employment),5):
#    print(item)


