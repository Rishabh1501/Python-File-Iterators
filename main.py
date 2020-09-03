from itertools import islice
from Combined_Data import combined_iterable
from Car_Makes_Per_Gender import car_makes
from Current_Records import current_data
from datetime import datetime


filename1 = "personal_info.csv"
filename2 = "employment.csv"
filename3 = "vehicles.csv"
filename4 = "update_status.csv"

#cleaned and Combined Files
for item in islice(combined_iterable(),5):
    print(item)

print(end='\n\n\n')


#Current Records
for item in islice(current_data(combined_iterable(),datetime.strptime('3/1/2017','%m/%d/%Y')),5):
    print(item)
    
print(end='\n\n\n')


#Car Makes by each Gender
car_makes(combined_iterable())