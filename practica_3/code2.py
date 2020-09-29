import datetime
date_string = '05-02-2001'
date_format = '%d-%m-%Y'
try:
  date_obj = datetime.datetime.strptime(date_string, date_format)
  print(date_obj)
except ValueError:
  print("Incorrect data format, should be YYYY-MM-DD")