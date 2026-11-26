attended = int(input("Enter attended classes: "))
total = int(input("Enter total classes: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance")
else:
    percentage = (attended / total) * 100

    print("Current Attendance:", percentage)

    extra = 0

    while ((attended + extra) / (total + extra)) * 100 < 75:
        extra += 1

    print("Extra classes required:", extra)