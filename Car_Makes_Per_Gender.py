import itertools
from collections import defaultdict
from Combined_Data import combined_iterable


def car_makes(iterable):
    male = defaultdict(int)
    female = defaultdict(int)
    for item in iterable:
        if item.gender == 'Male':
            male[item.vehicle_make] += 1
        elif item.gender == 'Female':
            female[item.vehicle_make] +=1

    sorted_male = sorted(male.items(),key = lambda x: x[1], reverse = True)
    sorted_female = sorted(female.items(), key=lambda x: x[1], reverse = True)

    #print(sorted_female)
    max_male = sorted_male[0][1]
    max_female = sorted_female[0][1]
    for item in sorted_male:
        if item[1] == max_male:
            print('Male:',item)
        else:
            break
    for item in sorted_female:
        if item[1] == max_female:
            print('Female:',item,end = "  ")
        else:
            break

if __name__ == '__main__':
    car_makes(combined_iterable())