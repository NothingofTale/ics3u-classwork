# Jeffery Huang - Coding Bat + If Statements Questions 
## String 1
>> hello_name: 
>>Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

~~~
def hello_name(name):
  return "Hello {}!".format(name)
~~~
>> make_abba: 
>> Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi"
~~~
def make_abba(a, b):
  return a+b+b+a
~~~
>> make_tags: 
>> The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
~~~
def make_tags(tag, word):
  html = "<{}>{}</{}>".format(tag, word, tag)
  return html
~~~
>>make_out_world: 
>> Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
~~~
def make_out_word(out, word):
  outstring_one = out[0:2]
  outstring_two = out[2:4]
  return outstring_one + word + outstring_two
~~~
>> extra_end: 
>> Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
~~~
def extra_end(string):
  last_index = (string[-2:]*3
  return last_index
~~~
>> first_two: 
>> Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "
~~~
def first_two(str):
  return str[0:2]
~~~
>> first_half: 
>> Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
~~~
def first_half(str):
  is_even = len(str) % 2
  if is_even == 0:
    str_half = len(str)/2
    return str[:str_half]
  else:
    return "Odd length"
~~~
>> string_without_end: 
>> Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
  without_end('Hello') → 'ell'
  without_end('java') → 'av'
  without_end('coding') → 'odin
~~~ 
def without_end(string):
  if len(string) >= 2:
    return string[1:len(string)-1]
  else:
    return
~~~
>> combo_string: 
>> Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
  combo_string('Hello', 'hi') → 'hiHellohi'
  combo_string('hi', 'Hello') → 'hiHellohi'
  combo_string('aaa', 'b') → 'baaab'
~~~
def combo_string(a, b):
  length_a = len(a)
  length_b = len(b)
  if length_a > length_b:
    return b + a + b
  elif length_b > length_a:
    return a + b + a
  else:
    return
~~~
>> non_start: 
>>  Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
  non_start('Hello', 'There') → 'ellohere'
  non_start('java', 'code') → 'avaode'
  non_start('shotl', 'java') → 'hotlava
~~~
def non_start(a, b):
  Omit_Char_a = a[1:]
  Omit_Char_b = b[1:]
  return Omit_Char_a + Omit_Char_b
~~~
## if-statements Workbook Questions 1-10
                https://repl.it/@JefferyHuang1/codingpractice20201125py 
