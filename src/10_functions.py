# Write a function is_even that will return true if the passed-in number is even.

def get_even(x):
 if x % 2 == 0:
  print(True)
 else:
  print(False)

print(
 get_even(4),
 get_even(3)
)
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
# Num is here three times with no name collisions, I think that's really cool.

# Print out "Even!" if the number is even. Otherwise print "Odd"

def even_odd(num):
 if num % 2 == 0:
  print("Even")
 else:
  print("Odd")

print(even_odd(num))

