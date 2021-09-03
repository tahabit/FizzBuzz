"""
File: fizzbuzz_functions.py
--------------------
This program plays the game fizzbuzz up to a given number entered by the user.
"""

a = 0
def main():
    sayi = int(input("Number to count to: "))
    for a in range(sayi):
        a = a+1
        if a %3 == 0:
            print("Fizz")
        elif a %5 == 0:
            print("Buzz")
        else:
            print(a)
    pass

if __name__ == "__main__":
    main()
