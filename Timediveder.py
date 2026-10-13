a=int(input())
minutes=a//60
seconds=a%60
if minutes>=60:
    hours=minutes//60
    minutes=minutes%60
    if hours>24:
        days = hours//24
        hours = hours%24
        print("Days: "+str(days))
    print("Hours: "+str(hours))
print("Minutes: "+str(minutes))
print("Seconds: "+str(seconds))
