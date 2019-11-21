#!/usr/bin/env python

currency = raw_input('To view what countries use what currency, please enter its respective CURRENCY CODE:\n').upper() #allows you to see what countries use what currency

country_list = ("EUR, GBD, USD, AUD, CAD, CNY, YEN") #list of options that you can pick from, if you select something else or input your selection wrong then you will be able to try again

EUR = ['Austria', 'Belgium', 'Cyprus', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Portugal', 'Slovakia', 'Slovenia', 'Spain', 'San Marino']
GBD = ['England', 'Scotland', 'Wales', 'Gibraltar', 'Isle of Man']
USD =['USA', 'Samoa', 'Ecuador', 'Puerto Rico']
YEN = ['Japan']
AUD = ['Australia']
CAD = ['Canada']
CNY = ['China'] #list of all the countries that use what currency

i = 0 #while loops that show each value of the list's one per line
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

if currency not in country_list:
    print  "We do not have this currency in our database or maybe you did not insert the correct currency code"
    import backup #if statement which allows you to try again if you entered your value in wrong

import time
time.sleep(1) #sleep function which makes the code come up easier on the eye for its user and easier to read