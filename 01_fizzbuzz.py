"""Distinct Python example #1."""
print("FizzBuzz", [("Fizz"*(i%3==0)+"Buzz"*(i%5==0)) or i for i in range(1,31)])
