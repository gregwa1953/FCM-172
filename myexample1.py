#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     myexample1.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue #172
# Written by G.D. Walters
# Copyright (c) 2021 by G.D. Walters
# This source code is released under the MIT License
# ======================================================
import sys
from dataclasses import dataclass


@dataclass
class TbookRec:
    Title: str
    Author: str
    ISBN: str
    Price: float
    QtyOnHand: int


myRecs = []


def setup_structures():
    myRec = TbookRec("I Robot", "Isaac Asimov", "978-0553382563", 6.79, 2)
    myRecs.append(myRec)
    myRec = TbookRec("The Gentle Giants of Ganymede", "James P. Hogan",
                     "978-0345298126", 6.11, 1)
    myRecs.append(myRec)
    myRec = TbookRec("Raise The Titanic", "Clive Cussler", "978-0425194522",
                     9.99, 1)
    myRecs.append(myRec)
    myRec = TbookRec("The Hitchiker's Guide to the Galaxy", "Douglas Adams",
                     "978-0345391803", 6.83, 1)
    myRecs.append(myRec)
    myRec = TbookRec("The Restaurant at the End of the Universe",
                     "Douglas Adams", "978-1529034530", 7.99, 0)
    myRecs.append(myRec)


def books():
    print(f'Number of Unique Books: {len(myRecs)}')
    for rec in myRecs:

        print(
            f'Title: {rec.Title}  Author: {rec.Author}  Price: {rec.Price}  Qty: {rec.QtyOnHand}'
        )


def startup():
    setup_structures()
    print(books())


def sell(title):
    found = False
    for rec in myRecs:
        if rec.Title == title:
            if rec.QtyOnHand > 0:
                rec.QtyOnHand -= 1
                print(f'There are now {rec.QtyOnHand} book(s) left in stock.')
            else:
                print('There is no stock of this title to sell!')
            found = True
    if found == False:
        print(f'Could not find {title} in stock.')


def infoTitle(title):
    found = False
    for rec in myRecs:
        if rec.Title == title:
            print(
                f'Title: {rec.Title}   Author: {rec.Author}   ISBN: {rec.ISBN}   Price: {rec.Price}   Qty: {rec.QtyOnHand}'
            )
            found = True
    if found == False:
        print(f'Could not find {title} in the database.')


def infoAuthor(author):
    for rec in myRecs:
        found = False
        if rec.Author == author:
            print(
                f'Title: {rec.Title}   Author: {rec.Author}   ISBN: {rec.ISBN}   Price: {rec.Price}   Qty: {rec.QtyOnHand}'
            )
            found = True
    if found == False:
        print(f'Could not find {author} in the database.')


def infoISBN(isbn):
    for rec in myRecs:
        found = False
        if rec.ISBN == isbn:
            print(
                f'Title: {rec.Title}   Author: {rec.Author}   ISBN: {rec.ISBN}   Price: {rec.Price}   Qty: {rec.QtyOnHand}'
            )
            found = True
    if found == False:
        print(
            f'Could not find any books with the ISBN of {isbn} in the database.'
        )


def work():
    quitit = False
    while quitit == False:
        print(
            "1 - Find book by Title   2 - Find book by Author   3 - Find book by ISBN   4 - Show All Books   5 - Sell A Book   0 - Quit",
            end='')
        resp = input(' -> ')
        if resp == "0":
            quitit = True
        if resp == "1":
            resp = input('Enter Book Title -> ')
            infoTitle(resp)
        if resp == "2":
            resp = input('Enter Author name -> ')
            infoAuthor(resp)
        if resp == "3":
            resp = input('Enter ISBN -> ')
            infoISBN(resp)
        if resp == "4":
            books()
        if resp == "5":
            resp = input('Enter Title ->')
            sell(resp)


if __name__ == "__main__":
    startup()
    work()