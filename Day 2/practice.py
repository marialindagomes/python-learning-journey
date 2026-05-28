
name = " Linda Maria Gomes "
nickname = "Linda"
age = "22"
is_student = True
cgpa = "3.02"
course_name = "python programming"

print("My name is  ", name)
print("You can call me ", nickname)
print("I'm ", age, "years old.")
print("I'm a student.", is_student)
print("My CGPA is ", cgpa)
print("Now I'm learning ", course_name)

favourite_language = input("Enter your favourite programming language:  ")
print("My favourite language is ", favourite_language)

print(len(name))
print(name[0])
print(name[-1])
print(name[0:4])
print(name[0:])
print(name[:3])
print(name[:])

course = "python \" programming"
print(course)
department = "Computer science & \n Engineering"
print(department)

first_name = "Linda"
last_name = "Gomes"
full_name = first_name + " " + last_name
print(full_name)

full_name = f"{first_name} {last_name}"
print(full_name)

print(name.upper())
print(name.lower())
print(name.title())
print(name.lstrip())
print(name.rstrip())
print(name.find("Lin"))
print(nickname.replace("Linda", "Liveo"))
print("Lin" in name)

print(type(name))
print(type(name) == str)
print(isinstance(age, int))

number = "2026"
year = int(number)
print("Year: ", year)

name += "  is my name"
print(name)


print(name.islower())
print(name.isupper())
print(name.isalpha())

name = input("what's your name ?").strip().title()
first, last = name.split("  ")
print(f"Hello, {first}")

email = "marialindagomes29@gmail.com"
print(email.endswith("@gmail.com"))

website = "https//github.com"
print(website.startswith("https"))

a = 10
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a % b)
print(a**b)

x = 30
x += 10
print(x)
