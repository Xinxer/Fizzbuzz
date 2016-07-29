import sys

if len(sys.argv) == 2 and len(sys.argv) <= 2:
  a = abs(int(sys.argv[1]))
elif len(sys.argv) == 1:
  a = abs(int(input("Enter an upper limit, or else:")))
else: 
  print("You entered too many arguments. Do less.")

for n in range(1,a):
    if n % 5 == 0 and n % 3 == 0:
        print("Fizz Buzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
        
print("Fizz Buzz counting up to {}\a".format(a))