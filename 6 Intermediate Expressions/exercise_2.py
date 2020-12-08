# link to assignment video  = https://www.youtube.com/watch?v=wgkC8SxraAQ&feature=youtu.be
# link to assignment in the book = http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
# page = 30
# exercise 3

#Exercise 3: Write a program to prompt the user for hours and rate per
#hour to compute gross pay
#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25
#We won’t worry about making sure our pay has exactly two digits after the decimal
#place for now. If you want, you can play with the built-in Python round function
#to properly round the resulting pay to two decimal places.

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
bill = float(hours) * float(rate)
print('Pay: ', bill)

