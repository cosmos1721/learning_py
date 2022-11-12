hrs =input("hours")
rate= input("rate")
h= float(hrs)
rate=float(rate)
r=h*rate
if h<40 :
    print("not eligible", r)
elif h==40:
    print("ok will see what can be done",r)
else:
    print('theek hai bhaai jeet gayi india iss baar')
    p=h-40
    p=p*1.5*rate
    p=(40*rate)+p
    print(p)