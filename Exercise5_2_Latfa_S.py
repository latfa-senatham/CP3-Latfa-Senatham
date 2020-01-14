distance = float(input("Distance(km) : "))
time = float(input("Time(h) : "))
if distance>=1 and time>=1:
    print(distance/time,"km/h")
else:
    print("Distance and time must have values from 1 up")
