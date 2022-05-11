import datetime

def datetime_to_str(date_time):
    month_numbers_list = [number for number in range(1,13)]
    month_names_list = list(map(lambda month_num: datetime.datetime(1,month_num, 1).strftime("%b"),month_numbers_list))
    month_name_str = [string for string in date_time.split("-") if string in month_names_list]
    month_number = datetime.datetime.strptime(month_name_str[0], '%b').month
    if month_number < 10:
        month_number = "0"+str(month_number)
    new_date_str = date_time.replace(month_name_str[0],str(month_number))
    #date_object =  datetime.datetime.fromisoformat(new_date_str)
    #print(new_date_str)
    list_of_dates = [new_date_str, datetime.datetime.strptime(new_date_str,'%Y-%m-%d %H:%M')]
    return list_of_dates