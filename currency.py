#!/usr/bin/env python

print "Now lets move onto the currency converter"

fro = raw_input('Please enter the currency you currently have (by entering its CURRENCY CODE):\n').lower() #allows you to enter the currency you wish to convert from
to = raw_input('Please enter the currency you wish to convert your money to (by entering its CURRENCY CODE):\n').lower() #allows you to enter the currency you wish to money to
amo = input('Please enter the amount of money you wish to convert:\n') #allows you to enter the amount of money you wish to convert

currency_list = ("eur, gbd, usd, aud, cad, cny, yen") #lists of currencies you can use

if fro == "eur" and to == "gbd": #if statement converting one currency to another 
  x = amo * 0.859118
  print "-->", float(x), "Pound Sterling"
elif fro == "eur" and to == "usd":
  x = amo * 1.12224
  print "-->", float(x), "US Dollars"
elif fro == "eur" and to == "aud":
  x = amo * 1.57621
  print "-->", float(x), "Australian Dollars"
elif fro == "eur" and to == "cad":
  x = amo * 1.49873
  print "-->", float(x), "Canadian Dollars"
elif fro == "eur" and to == "cny":
  x = amo * 7.53788
  print "-->", float(x), "Chinese Yuan"
elif fro == "eur" and to == "yen":
  x = amo * 125.224
  print "-->", float(x), "Japanese Yen"

if fro == "gbd" and to == "eur":
  x = amo * 1.16402
  print "-->", float(x), "Euros"
elif fro == "gbd" and to == "usd":
  x = amo * 1.30619
  print "-->", float(x), "US Dollars"
elif fro == "gbd" and to == "aud":
  x = amo * 1.83477
  print "-->", float(x), "Australian Dollars"
elif fro == "gbd" and to == "cad":
  x = amo * 1.74452
  print "-->", float(x), "Canadian Dollars"
elif fro == "gbd" and to == "cny":
  x = amo * 8.77478
  print "-->", float(x), "Chinese Yuan"
elif fro == "gbd" and to == "yen":
  x = amo * 145.800
  print "-->", float(x), "Japanese Yen"

if fro == "yen" and to == "eur":
  x = amo * 0.00798574
  print "-->", float(x), "Euro"
elif fro == "yen" and to == "gbd":
  x = amo * 0.00685840
  print "-->", float(x), "Pounds Sterling"
elif fro == "yen" and to == "usd":
  x = amo * 0.00896078
  print "-->", float(x), "US Dollars"
elif fro == "yen" and to == "aud":
  x = amo * 0.0125879
  print "-->", float(x), "Australian Dollars"
elif fro == "yen" and to == "cad":
  x = amo * 0.0119686
  print "-->", float(x), "Canadian Dollars"
elif fro == "yen" and to == "cny":
  x = amo * 0.0601910
  print "-->", float(x), "Chinese Yuan"

if fro == "cad" and to == "eur":
  x = amo * 0.667230
  print "-->", float(x), "Euro"
elif fro == "cad" and to == "gbd":
  x = amo * 0.572922
  print "-->", float(x), "Pounds Sterling"
elif fro == "cad" and to == "usd":
  x = amo * 0.748662
  print "-->", float(x), "US Dollars"
elif fro == "cad" and to == "aud":
  x = amo * 1.05178
  print "-->", float(x), "Australian"
elif fro == "cad" and to == "cny":
  x = amo * 5.02877
  print "-->", float(x), "Chinese Yuan"
elif fro == "cad" and to == "yen":
  x = amo * 83.5393
  print "-->", float(x), "Japanese Yen"

if fro == "usd" and to == "gbd":
  x = amo * 0.765262
  print "-->", float(x), "Pounds Sterling"
elif fro == "usd" and to == "eur":
  x = amo * 0.891190
  print "-->", float(x), "Euro"
elif fro == "usd" and to == "aud":
  x = amo * 1.40511
  print "-->", float(x), "Australian Dollars"
elif fro == "usd" and to == "cad":
  x = amo * 1.33579
  print "-->", float(x), "Canadian Dollars"
elif fro == "usd" and to == "cny":
  x = amo * 6.71739
  print "-->", float(x), "Chinese Yuan"
elif fro == "usd" and to == "yen":
  x = amo * 111.586
  print "-->", float(x), "Japanese Yen"

if fro == "aud" and to == "eur":
  x = amo * 0.634258
  print "-->", float(x), "Euro"
elif fro == "aud" and to == "gbd":
  x = amo * 0.544551
  print "-->", float(x), "Pounds Sterling"
elif fro == "aud" and to == "usd":
  x = amo * 0.711722
  print "-->", float(x), "US Dollars"
elif fro == "aud" and to == "cad":
  x = amo * 0.950728
  print "-->", float(x), "Canadian Dollars"
elif fro == "aud" and to == "cny":
  x = amo * 4.78056
  print "-->", float(x), "Chinese Yuan"
elif fro == "aud" and to == "yen":
  x = amo * 79.4205
  print "-->", float(x), "Japanese Yen"

if fro == "cny" and to == "eur":
  x = amo * 0.132658
  print "-->", float(x), "Euro"
elif fro == "cny" and to == "gbd":
  x = amo * 0.113881
  print "-->", float(x), "Pounds Sterling"
elif fro == "cny" and to == "usd":
  x = amo * 0.148874
  print "-->", float(x), "US Dollars"
elif fro == "cny" and to == "aud":
  x = amo * 0.209188
  print "-->", float(x), "Australian Dollars"
elif fro == "cny" and to == "cad":
  x = amo * 0.198869
  print "-->", float(x), "Canadian Dollars"
elif fro == "cny" and to == "yen":
  x = amo * 16.6117
  print "-->", float(x), "Japanese Yen"

if fro not in currency_list or to not in currency_list:
  print  "Ohh there seems to be an error in your input, please try again"
  import try_again #if statement which allows you to try again if you entered an incorrect currency code