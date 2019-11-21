#!/usr/bin/env python
import time
time.sleep(2)
print "Press 1 if you would like to try again" #gives you the option tp try again
time.sleep(2)
print "Press 2 if you would like to move onto the currency converter" #gives the user the option to move onto the currency converter
time.sleep(2)
direction = raw_input("Please dictate where you would like to go:\n") #makes you pick one of the two options

while direction != "1" and direction != "2":
  direction = raw_input("Please choose either 1 or 2:\n") #while loop making you only enter direction 1 or 2

if direction == "1":
  currency = raw_input('To view what countries use what currency, please enter its respective CURRENCY CODE:\n').upper()

  country_list = ("EUR, GBD, USD, AUD, CAD, CNY, YEN")

  EUR = ['Austria', 'Belgium', 'Cyprus', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Portugal', 'Slovakia', 'Slovenia', 'Spain', 'San Marino']
  GBD = ['England', 'Scotland', 'Wales', 'Gibraltar', 'Isle of Man']
  USD =['USA', 'Samoa', 'Ecuador', 'Puerto Rico']
  YEN = ['Japan']
  AUD = ['Australia']
  CAD = ['Canada']
  CNY = ['China'] #list of all the countries that use what currency

  i = 0
  n = 0
  if currency in "EUR":
    while i < len(EUR):
      print "->", EUR[n]
      n = n + 1
      i = i + 1

  i = 0
  n = 0
  if currency in "GBD":
    while i < len(GBD):
      print "->", GBD[n]
      n = n + 1
      i = i + 1

  i = 0
  n = 0
  if currency in "USD":
    while i < len(USD):
      print "->", USD[n]
      n = n + 1
      i = i + 1

  i = 0
  n = 0
  if currency in "AUD":
    while i < len(AUD):
      print "->", AUD[n]
      n = n + 1
      i = i + 1

  i = 0
  n = 0
  if currency in "CAD":
    while i < len(CAD):
      print "->", CAD[n]
      n = n + 1
      i = i + 1

  i = 0
  n = 0
  if currency in "CNY":
    while i < len(CNY):
      print "->", CNY[n]
      n = n + 1
      i = i + 1

  i = 0
  n = 0
  if currency in "YEN":
    while i < len(YEN):
      print "->", YEN[n]
      n = n + 1
      i = i + 1
else:
  print "" #skips to the currency converter