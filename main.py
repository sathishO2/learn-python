import datetime
def q2(dt : datetime):

    return dt.strftime("%d/%m/%Y %I:%M")

r = q2(datetime.datetime.now())
print(r)