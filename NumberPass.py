'''
Created on 23/02/2012

Last Update on 07/09/2014

@author: ultrazoid_
'''

import random 
import time

"""
^ imports time and random features
"""

"""
### NOTES FOR WHAT TO DO HERE

IF LINE NEEDS TO BE OVERWRITTEN WILL NOT OVERWRITE BUT PRINT AGAIN FILE CONTENTS AGAIN
"""

print "Welcome to:\nultrazoid_'s\nPassword number generator" #prints a welcome message to the program
filename2 = "pass.settings"
sf = open (filename2, "r")
sef = sf.read(8)
if sef == ' ':
	sf.close()
	print "pass.settings not found creating..."
	sf = open (filename2, "w")
	ff = raw_input('Please enter a filename to store password numbers in:')
	ff += '.yml'
	sf.write(ff)
else:
	ff=sef
sf.close()
filename=ff
fo = open (filename, "r") 

ss = raw_input('press any key to continue(end to end):') #asks user to press any key or enter 'end' to stop the program

while ss != 'end':
    bb = raw_input('What is this Password number for:')

    #check to see if line needs to be overwritten
    overCheck = fo.readlines()
    overDo = False 
    for locale in overCheck:
    	if bb in locale:
    		overDo = True
    		overCheck.remove(locale)
    	else:
    		do = "nothing"
    fo.close()
    if overDo == True:
    	open(filename, 'w').close()
    	for line in overCheck:
    		fo = open (filename, "a") 
    		fo.write(line)
 	else:
 		do = "nothing"
    if overDo == False:
        fo = open (filename, "a")

    ab = str(random.randrange(0,9))
    ac = str(random.randrange(0,9))
    ad = str(random.randrange(0,9))
    ae = str(random.randrange(0,9))
    aa = str(ab+ac+ad+ae)
    """
    Defines the values of ab,ac,ad,ae as single digit natural numbers
    Then combines them in a 4 digit PIN styled number
    """
    print aa #prints the value of variables aa
    fo.write(bb)
    fo.write(':   ')
    fo.write(aa)
    fo.write('\n')
    ss = raw_input('press any key to continue(end to end):') #asks user to press any key or enter 'end' to stop the program
print 'ending...' #prints ending...
print 'saving...'
fo.close
time.sleep(5) #waits 5 seconds before ending
