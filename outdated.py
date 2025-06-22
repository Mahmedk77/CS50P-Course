months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        Date=input('Date: ')
        if "," in Date:
            month,day,year=Date.split(' ')
            day=day.removesuffix(',')
            if (month in months) and (day<=31):
                print(f'{int(year)}-{(months.index(month)+1):02}-{int(day):02}')
                break
        elif "/" in Date:
            Date=Date.split('/')
            m,d,y=map(int,Date)
            if (m<=12) and (d<=31):
                print(f'{y}-{m:02}-{d:02}')
                break
    except:
        pass

#SOMEONE ELSE CODE
while True:
    Date=input('Date: ')
    if '/' in Date:
        month,day,year=Date.split('/')
    elif ',' in Date:
        Date=Date.replace(',',"")
        month,day,year= Date.split(" ")
        if month in months:
            month=months.index(month)+1
    try:
        if int(month)>12 or int(day)>31:
            continue
        else:
            break
    except:
        continue
print(f'{year}-{int(month):02}-{int(day):02}')

            


    


