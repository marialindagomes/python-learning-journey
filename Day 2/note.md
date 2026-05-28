# Day 02 - Variables, Data Types & Strings 🐍

## Topics I Learned
- Variables
- Data Types
- Strings
- Escape Sequences
- Formatted Strings
- String Methods
- Numbers
- Type Conversion

# Variables

Variables are used to store data in Python.

## Example

name = "Linda"
age = 22

print(name)
print(age)


# Data Types

Python has different types of data.

| Data Type | Example |

| String | `"Hello"` |
| Integer | `10` |
| Float | `3.14` |
| Boolean | `True` |

## Example

name = "Linda"
age = 22
cgpa = 3.02
is_student = True


# Strings

Strings are text values written inside quotes.

## Example

message = "Python is fun"
print(message)


# Escape Sequences

Escape sequences are special characters used inside strings.

| Escape Sequence | Meaning |

| `\n` | New line |
| `\t` | Tab |
| `\"` | Double quote |

## Example

print("Hello\nWorld")
print("Python\tProgramming")


# Formatted Strings

Formatted strings make it easier to insert variables into strings.

## Example

name = "Linda"
age = 22

print(f"My name is {name} and I am {age} years old.")


# String Methods

String methods help manipulate strings.

## Common Methods
- upper()
- lower()
- replace()
- find()

## Example

text = "python"

print(text.upper())
print(text.capitalize())
print(text.replace("python", "Python"))


# Numbers

Python supports:
- Integers
- Floats

## Example

x = 10
y = 3.5

print(x + y)
print(x * y)


# Type Conversion

Type conversion changes one data type into another.

## Example

age = "22"

converted_age = int(age)

print(converted_age)
print(type(converted_age))


# Problems I Faced
- Confusion between string and integer
- Understanding escape sequences

# Today's Progress 🚀
Learned Python basics about variables, strings, and type conversion successfully.