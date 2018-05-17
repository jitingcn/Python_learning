#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - atm.py
# Created by JT on 4/2/2018 22:14.
# Blog: https://blog.jtcat.com/

# 3.ATM
# The program should simulate an ATM banking machine. The program should first ask for the user’s PIN code.
# If the PIN code is entered correctly the user should be able to:
# •	Check their balance
# •	Withdraw money from their account up to the total of their balance
# •	Deposit money into the account
# The user’s balance at the beginning of the transaction should be a randomly generated total between £100 - £1000.
__author__ = 'JT <jiting@jtcat.com>'

import random


class ATM(object):
    version = "v1.0 Release"

    def __init__(self):
        self.user_pin = "1234"
        self.user_init_balance = random.randint(100, 1000)
        self.user_balance = self.user_init_balance

    def login(self):
        tries = 4
        while tries > 0:
            pin = input("Logging... Please Enter Your 4 Digit Pin:")
            if self.verify_pin(pin):
                print("Pin accepted!")
                return True
            else:
                tries -= 1
                print("Invalid pin.", tries, "tries left.")
        print("To many incorrect tries. Could not log in!")
        return False

    def verify_pin(self, pin):
        if pin == self.user_pin:
            return True
        else:
            return False

    def check_balance(self, show_type=1):
        if show_type == 1:
            print('\nYour balance: ', self.user_balance)
        elif show_type == 2:
            print("Your remain balance: ", self.user_balance)

    def withdraw(self):
        self.check_balance()
        input_amount = input("How much do you want to withdraw?")
        if str.isdigit(input_amount):
            amount = int(input_amount)
            if amount <= self.user_balance:
                self.user_balance = self.user_balance - amount
                print("\nSuccess!")
                self.check_balance(2)
            else:
                print("Wrong number! You don't have enough balance!")
        else:
            print("Failed... Wrong number!")

    def deposit(self):
        self.check_balance()
        input_amount = input("How much do you want to deposit?")
        if str.isdigit(input_amount):
            amount = int(input_amount)
            self.user_balance = self.user_balance + amount
            print("\nSuccess!")
            self.check_balance(2)
        else:
            print("Failed... Wrong number!")

    def menu(self):
        run = True
        print("\nHello customer!")
        while run:
            operation = input("\n1: Check balance\n"
                              "2: Withdraw\n"
                              "3: Deposit funds\n"
                              "4: Log out\n"
                              "Please select operation:")
            if operation == "1":
                self.check_balance()
                print("What do you want to do next?")
            elif operation == "2":
                if self.user_balance > 0:
                    self.withdraw()
                else:
                    self.check_balance()
                    print("Operation Failed! There is no balance in your account.")
            elif operation == "3":
                self.deposit()
            elif operation == "4":
                run = False
            else:
                print("\nWrong number, please type again.")

    def start(self):
        print("Author: ", __author__, "\nVersion: ", ATM.version)
        print("\nWelcome to JT Bank ATM!")
        ATM.run = True
        while ATM.run:
            operation = input("\n1: Log in\n"
                              "2: quit\n"
                              "Please select operation:")
            if operation == "1":
                if self.login():
                    self.menu()
                    print("Thanks for using!")
                else:
                    ATM.run = False
            elif operation == "2":
                ATM.run = False
            else:
                print("\nWrong number, please type again.")


if __name__ == "__main__":
    ATM().start()
