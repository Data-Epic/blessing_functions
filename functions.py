#Task 1: Greetings
def greet_user():
  print("Hello, Welcome to Pythin Programming!")

greet_user()

print("======================================")

#Task 2: Name outputing
def display_full_name(first_name, last_name):
  print(f"Hello {first_name} {last_name}, nice to meet you")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

display_full_name(first_name, last_name)

print("======================================")

#Task 3: Sum
def add_numbers(a,b):
  return a+b

sum = add_numbers(int(input("Enter a number: ")), int(input("Enter a number: ")))
print(f"The sum is: {sum}")

print("======================================")


#Task 4
school_name = "Chris-Ade International Academy"
def print_school():
  teacher_name = "Mr. Esho" #This is a local variable
  print(f"This is from the local local scope: {teacher_name}")

  #overriding the global variable school_name overridden within the local scope
  school_name ="Local Chris-Ade International Academy" #this is also a local variable
  print(f"This is the overridden school_name from the local function: ", school_name)

print_school()
print("=============")
print(f"{school_name} - this is the global variable maintained outside as it was only overridden within the local function")