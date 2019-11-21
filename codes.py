#!/usr/bin/env python

codes = {"Euro ==": "EUR",
         "Pound Sterling ==": "GBD",
         "US Dollar ==": "USD",
         "Japanese Yen ==": "YEN",
         "Australian Dollar ==": "AUD",
         "Canadian Dollar ==": "CAD",
         "Chinese Yuan ==": "CNY"}  #dictionary that shows the universal currency code of each currency

import time
name = raw_input("Please enter your name\n")
print "Hello", name + ",","welcome to our currency converter!" #welcome
time.sleep(2)
print "Designed by Jack, Fiachra and Luke."
time.sleep(2)
print "These are the currencies we have and their respective currency codes . . .\n"
time.sleep(3)

for value in sorted (codes):
  print value, codes[value]

print "\nWhen entering the currency you wish to transfer, please do so by entering its universal CURRENCY CODE."
time.sleep(3)