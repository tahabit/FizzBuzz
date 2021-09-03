"""
File: fizzbuzz_functions.py
--------------------
This program plays the game fizzbuzz up to a given number entered by the user.
"""

fizzbuzz = 0
def main():
    number = int(input("Number to count to: "))
    for fizzbuzz in range(number):
        fizzbuzz = fizzbuzz+1
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("Fizzbuzz")
        elif fizzbuzz %3 == 0:
            print("Fizz")
        elif fizzbuzz %5 == 0:
            print("Buzz")

        else:
            print(fizzbuzz)
    pass

if __name__ == "__main__":
    main()
