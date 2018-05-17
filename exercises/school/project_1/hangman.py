#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python_learning - Hangman.py
# Created by JT on 4/1/2018 23:14.
# Blog: https://blog.jtcat.com/

# 2.Hangman
# The program should play a game of Hangman with the user.
# First choose a secret word at random out of a list of words.
# Then display a dash for each letter of the secret word.
# The user should guess letters, one at a time, to try to guess the secret word.
# If the user guesses a letter in the secret word that letter should replace the dash in the correct position.
# If the user guesses a letter that does not appear in the secret word the program
# should reduce the number of incorrect guesses available by one.
# If the user correctly guesses all the letters in the word, the user wins the game.
# Otherwise when the user runs out of incorrect guesses the program wins.
# After each game the user should have the option to play again.
__author__ = 'JT <jiting@jtcat.com>'

import random


class HangMan(object):
    version = "v0.1 Alpha (words: programming language)"
    words = "Java C Python PHP JavaScript Ruby Perl Swift Delphi Go Lisp Kotlin Haskell Bash".split()
    guesses = 5

    def choose_word(self):
        return self.words[random.randint(0, len(self.words) - 1)]

    @staticmethod
    def ask_evaluate(word, result, missed):
        guess = input()
        if guess is None or len(guess) != 1 or (guess in result) or (guess in missed):
            return None, False
        i = 0
        right = guess in word
        for x in word:
            if x == guess:
                result[i] = x
            i += 1
        return guess, right

    @staticmethod
    def play_again():
        print("Do you want to play again? (yes or no)", end="")
        status = input()
        if status == "yes":
            HangMan().main()
        else:
            pass

    def main(self):
        # welcome message
        print("Author: ", __author__, "\nVersion: ", HangMan.version)
        print("\nWelcome to Hangman game!")

        word = list(self.choose_word().lower())
        result = list("_" * len(word))
        print('The word is: ', result)
        success, i, missed = False, 0, []
        while i < self.guesses:
            print("You have", self.guesses - i, "more guesses.")
            print('Guess the word: ', end='')
            guess, right = self.ask_evaluate(word, result, missed)
            if guess is None:
                print('You\'ve already entered this character or doing something wrong.')
                continue
            print(''.join(result))
            if result == word:
                print('Congratulations ! You\'ve just saved a life !')
                success = True
                break
            if not right:
                missed.append(guess)
                i += 1
            print('Missed characters: ', missed)

        if not success:
            print('The word was \'' + ''.join(word) + '\' ! You\'ve just killed a man!')
        self.play_again()


if __name__ == "__main__":
    HangMan().main()
