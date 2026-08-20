tam = int(input("enter the tamil mark: "))
eng = int(input("enter the english mark: "))
mat = int(input("enter the maths mark: "))
sci = int(input("enter the science mark: "))
soc = int(input("enter the social science mark: "))

avg = (tam + eng + mat + sci + soc) / 5
print("Your average:", avg)

if avg >= 65:
    available_courses = ["bio", "cs", "ca", "bm"]
else:
    available_courses = ["ca", "bm"]

print(f"{', '.join(available_courses)} are available for your mark:")

while True:
    course = input("enter the course name: ").lower()
    if course in available_courses:
        print("course selection is successful")
        break
    else:
        print("invalid course. Try again.")
