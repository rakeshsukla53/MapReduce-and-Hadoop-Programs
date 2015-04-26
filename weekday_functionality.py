__author__ = 'rakesh'


from datetime import datetime


date = '2015-04-26'

weekday = datetime.strptime(date, "%Y-%m-%d").weekday()

print weekday  #sunday means 6 and monday means 0

#just convert the date to a given weekday and make the weekday as the key of the map reduce function and cost of those items
#as the value
#mean = TotalSales/Count and it will be for all the weeks
#just remember to find the weekday using the date field



