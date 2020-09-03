from datetime import datetime
#from Combined_Data import combined_iterable
#import itertools

stale_date = datetime.strptime('3/1/2017','%m/%d/%Y')

def current_data(iterable,stale_date):
    for item in iterable:
        if item.last_updated >= stale_date:
            yield item

#for item in itertools.islice(current_data(combined_iterable(),stale_date),3):
#    print(item)
