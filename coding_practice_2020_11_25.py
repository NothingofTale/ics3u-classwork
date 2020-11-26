# Jeffery Huang - Coding Bat + If Statements Questions 
# String 1
# hello_name: 
# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

def hello_name(name):
  return "Hello {}!".format(name)

# make_abba: 
# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi"

def make_abba(a, b):
  return a+b+b+a

# make_tags: 
# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

def make_tags(tag, word):
  html = "<{}>{}</{}>".format(tag, word, tag)
  return html

# make_out_world: 
# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

def make_out_word(out, word):
  outstring_one = out[0:2]
  outstring_two = out[2:4]
  return outstring_one + word + outstring_two

# extra_end: 
# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

def extra_end(string):
  last_index = (string[-2:]*3
  return last_index

# first_two: 
# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "

def first_two(str):
  return str[0:2]

# first_half: 
# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
  is_even = len(str) % 2
  if is_even == 0:
    str_half = len(str)/2
    return str[:str_half]
  else:
    return "Odd length"

# string_without_end: 
# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
#  without_end('Hello') → 'ell'
#  without_end('java') → 'av'
#  without_end('coding') → 'odin

def without_end(string):
  if len(string) >= 2:
    return string[1:len(string)-1]
  else:
    return

# combo_string: 
# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
#  combo_string('Hello', 'hi') → 'hiHellohi'
#  combo_string('hi', 'Hello') → 'hiHellohi'
#  combo_string('aaa', 'b') → 'baaab'

def combo_string(a, b):
  length_a = len(a)
  length_b = len(b)
  if length_a > length_b:
    return b + a + b
  elif length_b > length_a:
    return a + b + a
  else:
    return

# non_start: 
#  Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
#  non_start('Hello', 'There') → 'ellohere'
#  non_start('java', 'code') → 'avaode'
#  non_start('shotl', 'java') → 'hotlava
 
def non_start(a, b):
  Omit_Char_a = a[1:]
  Omit_Char_b = b[1:]
  return Omit_Char_a + Omit_Char_b







# if-statements Workbook Questions 1-10
#                https://repl.it/@JefferyHuang1/codingpractice20201125py 
# Exercise 34: Even or Odd
integer = int(input("Find if an integer is even or odd: "))
if integer % 2 == 0:
  print("even")
else:
  print("odd")


# Exercise 35: Dog Years
First 2 human years = 10.5 dog years each
human_year = float(input("Enter the age of the human to calculate the # of dog years: "))

if human_year < 2:
  dog_years = human_year * 10.5
  print(dog_years)
elif human_year >= 2:
  dog_years = 21 + (human_year - 2) * 4
  print(dog_years)
else:
  print("ERROR")

# Exercise 36: Vowel or Consonant
while True:
  letter = input("Enter a letter to find if it is a vowel: ").lower()
  vowels = ("a", "e", "i", "o", "u")

  if letter in vowels:
    print("Your letter is a vowel")
  elif letter == "y":
    print("Y is sometimes a vowel")
  else:
    print("Your letter is a consonant")
    
# Exercise 37: Name that shape
while True:
  sides = int(input("How many sides does your shape have? (Note: we support shapes with" "sides from 3-10): "))
  shapes = {3:"triangle", 4:"Quadrilateral", 5:"Pentagon", 6:"Hexagon", 7:"Septagon", 8:"Octogon", 9:"nonogon", 10:"decagon"}
  
  if sides in shapes:
    print(f"Your shape has {sides} sides")
    print(f"Your shape is a {shapes[sides]}.")
  else:
    print("ERROR")

# Exercise 38: Month Name to Number of Days
while True:
  month = input("What is the month?: ").lower()
  thirty_day_months = ['april', 'june', 'september', 'november']
  thirtyone_day_months = ['janurary', 'march', 'may', 'july', 'august', 'october', 'december']
  if month in thirty_day_months:
    print("There are thirty days in this month")
  elif month in thirtyone_day_months:
    print("There are thity-one days in this month")
  elif month == 'feburary':
    print("There are 28 or 29 days in this month")
  else:
    print('ERROR')

#Exercise 39: Sound Levels
while True:
  sound = float(input("Enter a sound level in decibals: "))
  sound_table = {130:'jackhammer', 106:'lawnmower', 70:'alarm clock', 40:'quiet room'}
  if sound == 130:
    print('Your sound is as loud as a jackhammer')
  elif sound > 130:
    print('Your sound is louder than a jackhammer')
  elif sound == 106:
    print('Your sound is as loud as a lawnmower')
  elif 106 < sound < 130:
    print('Your sound is louder than a lownmower but quieter than a jackhammer') 
  elif sound == 70:
    print('Your sound is as loud as an alarm clock')
  elif 70 < sound < 106:
    print('Your sound is louder than an alarm clock but quieter than a lawnmower')
  elif sound == 40:
    print('Your sound is as loud as a quiet room')
  elif 40 < sound < 70:
    print('Your sound is louder than a quiet room but quieter than an alarm clock') 
  elif sound < 40:
    print('Your sound is as loud as a quiet room')
  else:
    print('error')

# Exercise 40: Name That Triangle
while True:
  side_one = float(input('What is the length of the first side of your triangle?: '))
  side_two = float(input('What is the length of the second side of your triangle?: '))
  side_three = float(input('What is the length of the third side of your triangle?: '))

  if side_one == side_two and side_one == side_three:
    print('This is an equalateral triangle')
  elif side_one != side_two and side_one != side_three:
    print('This is a scalene triangle')
  else:
    print('This is an isosceles triangle')


# Exercise 41: Note to Frequency
while True:
  note = input("Enter a note: ").upper()
  note_freq = {"C4":261.63 ,"D4":293.66, "E4":329.63, "F4":349.23, "G4": 392, "A4":440, "B4":493.88}
  if note[0] == "C":
    frequency = note_freq["C4"]/2**(4 - int(note[1]))
  elif note[0] == "D":
    frequency = note_freq["D4"]/2**(4 - int(note[1]))
  elif note[0] == "E":
    frequency = note_freq["E4"]/2**(4 - int(note[1]))
  elif note[0] == "F":
    frequency = note_freq["F4"]/2**(4 - int(note[1]))
  elif note[0] == "G":
    frequency = note_freq["G4"]/2**(4 - int(note[1]))
  elif note[0] == "A":
    frequency = note_freq["A4"]/2**(4 - int(note[1]))
  elif note[0] == "B":
    frequency = note_freq["B4"]/2**(4 - int(note[1]))
  else:
    print('ERROR')
    break

  print(f"The frequency of this note is {frequency}Hz\n")

# Exercise 42: Frequency to Note
while True:
  frequency = float(input("Enter a frequency: "))
  note_freq = {"C4":261.63 ,"D4":293.66, "E4":329.63, "F4":349.23, "G4": 392, "A4":440, "B4":493.88}
  if frequency >= note_freq["C4"] - 1 and frequency <= note_freq["C4"] + 1:
    print("Your note is C4")
  elif frequency >= note_freq["D4"] - 1 and frequency <= note_freq["D4"] + 1:
    print("Your note is D4")
  elif frequency >= note_freq["E4"] - 1 and frequency <= note_freq["E4"] + 1:
    print("Your note is E4")
  elif frequency >= note_freq["F4"] - 1 and frequency <= note_freq["F4"] + 1:
    print("Your note is F4")
  elif frequency >= note_freq["G4"] - 1 and frequency <= note_freq["G4"] + 1:
    print("Your note is G4")
  elif frequency >= note_freq["A4"] - 1 and frequency <= note_freq["A4"] + 1:
    print("Your note is A4")
  elif frequency >= note_freq["B4"] - 1 and frequency <= note_freq["B4"] + 1:
    print("Your note is B4")
  else:
    print("The frequency does not correspond to any of the notes")

# Exercise 43: Faces on Money
while True:
  denomination = int(input("Enter a denomination of a US banknote: $"))
  individual = {100:"Benjamin Franklin", 50:"Ulysses S. Grant", 20:"Andrew Jackson", 10:"Alexander Hamilton", 5:"Abraham Lincoln", 2:"Thomas Jefferson", 1:"Geroge Washington"}
  if denomination in individual:
    print(f"The denomination you entered is the ${denomination} US bank note with an image of {individual[denomination]}")
  else:
    print("error")
