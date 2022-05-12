hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
x = (hour * 60) + mins + dura
y = str ((x // 60)%24)
z = str (x % 60)
print (y + ":" + z)