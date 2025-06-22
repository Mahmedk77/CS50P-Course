grocery={}
value=1
while True:
    try:
        item=input().upper()
        if item in grocery:
            grocery[item]=grocery[item]+1
        else:
            grocery[item]=1
    except EOFError:
        grocery=dict(sorted(grocery.items()))
        for key,values in grocery.items():
            print(f"{values} {key}")
        break
