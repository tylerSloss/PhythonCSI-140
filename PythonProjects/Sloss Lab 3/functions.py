"""DESCRIPTION OF THE MODULE GOES HERE

Author: Tyler Sloss
Class: CSI-160
Assignment: Lab 3 Week 3
Due Date: 9/19/22

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""


def digit_sum(number, digits):
    """ Gets sum of digits of inputted number

        Arguments:
          number (int): actual number 
          digits (int): number of digits in number

        Return:
          sum of digits (int)

        Assumptions:
          number and digits must be an int
        """
    i = digits
    digitSum = 0
    currentNum = 0
    prevNum = 0

    while i > 0:
        divider = 10 ** (i - 1)
        currentNum = number // divider
        digitSum += currentNum - (prevNum * 10)
        prevNum = currentNum
        i -= 1
    return digitSum


def hours_to_days(hours):
    """ Converts hours to days

    Arguments:
      hours (int): number of hours as an integer

    Return:
      number of days (int)

    Assumptions:
      hours must be an int
    """
    days = hours // 24
    return days


def days_to_weeks(days):
    """ Converts days to weeks

        Arguments:
          days (int): number of days as an integer

        Return:
          number of weeks (int)

        Assumptions:
          days must be an int
        """
    numWeeks = days // 7
    return numWeeks


numIn = int(input("Enter an integer: "))
numDigits = int(input("How many digits in the integer you entered: "))
print("The sum of the digits in the integer you entered is: " + str(digit_sum(numIn, numDigits)))

numHours = int(input("Enter hours to convert to days: "))
print(str(numHours) + " hours is approximately " + str(hours_to_days(numHours)) + " days.")

numDays = int(input("Enter days to convert to weeks: "))
print(str(numDays) + " days is approximately " + str(days_to_weeks(numDays)) + " weeks.")
