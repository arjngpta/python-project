import os
import datetime
from time import gmtime, strftime
name = raw_input("Hello, what is your name? ")
print "Hello "+ name +"!"
task = raw_input("What can I do for you today? ")
if "time" in task:
	print "The time is: "+ strftime("%H:%M:%S on %d %B, %Y")
else:
	print "Goodbye, "+ name +"!"