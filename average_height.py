a = 1
b = int(input("How many students are there to find out the average? "))
total_height = 0
student_count = 0

while a <= b:
    height = float(input(f"What is the height of person {a} (in Meters): "))
    total_height += height
    student_count += 1
    a += 1

average_height = total_height / student_count

print(f"The average height of {b} persons is: {average_height} meters")