'''
Simple Fizzbuzz game
Author: Joshua Ola Sorungbe
'''

def fizzbuzz():
#The program will print numbers from 1 to 100
    for number in range(1, 101):
        #print FIZZBUZZ where number is divisible by 3 and 5
        if number % 3 == 0 and number % 5 == 0:
            print(f"{number}. FizzBuzz")
        #print Buzz if number is divisible by 5
        elif number % 5 == 0:
            print(f"{number}. Buzz")
        # print Buzz if number is divisible by 3
        elif number % 3 == 0:
            print(f"{number}. Fizz")
        else:
            print(number)

if __name__ == "__main__":
    print("Welcome to Fizz buzz...")
    fizzbuzz()
    print("End..")