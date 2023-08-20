# 12hr to 24hr clock system converter
def time_converter( hour, minute, period ):
    if period == "pm":
        if hour == 12:
            time = 12
        else:
            time = hour + 12

    else:
        # if period == "am":
        if hour == 12:
            time = 0
        else:
            time = hour

    formatted_time = str("{:02}".format(time))
    formatted_minute = str("{:02}".format(minute))

    return formatted_time + formatted_minute


hour = 6
minute = 7
period = "pm"
time = time_converter(hour, minute, period)
print(time)