import Cleaned_Data
import itertools
from collections import namedtuple


def combined_iterable():
    filename1 = "personal_info.csv"
    filename2 = "employment.csv"
    filename3 = "vehicles.csv"
    filename4 = "update_status.csv"
    personal_info = Cleaned_Data.readfiles(filename1)
    employment = Cleaned_Data.readfiles(filename2)
    vehicles = Cleaned_Data.readfiles(filename3)
    update_status = Cleaned_Data.readfiles(filename4)

    Data = namedtuple('Data',(next(personal_info)+next(employment)[:3]+next(vehicles)[1:]
                              +next(update_status)[1:]))
    for _ in itertools.count():
        try:
            yield Data(*(next(personal_info)+next(employment)[:3]+next(vehicles)[1:]
                        +next(update_status)[1:]))
        except StopIteration:
            break

#for item in combined_iterable():
#    print(item)