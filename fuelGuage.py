while True:
        try:
            values= input('fraction: ')
            x,y=map(int,values.split('/')) #pythonic way or x,y=int(x),int(y)
            frac= (x/y)
            if frac<1:
                frac=int(frac*100) #again so it doesnt converts to float
                break
        except:
            print('oops that wrong')
if frac>=99:
     print('F')
elif frac<=1:
     print('E')
else:
     print(f'{frac}%')

