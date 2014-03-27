#!/usr/bin/env python

fname_in = 'lab1.txt'
fname_out = 'mylab1.txt'

# read in the 1st file
with open(fname_in) as f:
    txt = f.read()

# write it out to 
with open(fname_out, 'w') as f:
    f.write(txt)

#def copy(file1, file2):
#
#    with open(file1) as f:
#        txt = f.read()
#
#    with open(file2, 'w') as f:
#        f.write(txt)

#copy(fname_in, fname_out)
