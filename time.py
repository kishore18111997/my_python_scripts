import datetime

def format_railway_time(time):
    hours = time.strftime("%H")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    return f"{hours}:{minutes}:{seconds}"


current_time = datetime.datetime.now()
railway_time = format_railway_time(current_time)
print(railway_time)

x = current_time + datetime.timedelta(seconds=10)
y = format_railway_time(x)
print(y)
