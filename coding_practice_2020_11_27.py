# WHILE LOOP COUNTER VARIABLE PRACTICE GENERATOR
# ==============================================

# Three steps to looping with a counter variable:
# - what is the first value I want to output?
#     Set 'i' to that value.
# - what is the final value I want to output?
#     Include that in the while condition.
# - what do I want it to go up by?
#     Increase 'i' by that amount.

# Exercises
# ---------
# Create a while loop that will print:
#     1. from -29 to 178 by 9.
#     2. from -422 to 406 by 18.
#     3. from 109 to 265 by 4.
#     4. from 478 to 500 by 1.
#     5. from 304 to 712 by 12.
#     6. from -376 to -188 by 4.
#     7. from -461 to -389 by 4.
#     8. from 284 to 317 by 3.
#     9. from -428 to 418 by 18.
#     10. from -162 to -127 by 1.

index = -29
while index <= 178:
  print(index)
  index += 9

index = -422
while index < 406:
  print(index)
  index += 18
  
index = -109
while index < 265:
  print(index)
  index += 4
  
index = 478
while index < 500:
  print(index)
  index += 1
  
index = 304
while index < 712:
  print(index)
  index += 12
  
index = -376
while index < -188:
  print(index)
  index += 4
  
index = -461
while index < -389:
  print(index)
  index += 4

index = 284
while index < 317:
  print(index)
  index += 3
  
index = -428
while index < 418:
  print(index)
  index += 18
  
index = -162
while index < -127:
  print(index)
  index += 1
