from __future__ import print_function
import sys, os
file = sys.argv[1]

# These magic strings were obtained from the web page
#   http://tutorialsto.com/database/access/crack-access-*.-mdb-all-current-versions-of-the-password.html
# and refer to a non-password protected access database byte sequence at file
# positions x42 (XOR'd password at every second byte) and x62 (magic salt variable)
#
no_pass_62 = '0C'
no_pass_42 ='BE68EC3765D79CFAFECD28E62B258A606C077B36CDE1DFB14F671343F73C'

with open(file, 'rb') as f:
    f.seek(66, 0) # x42 == 66
    myfile_42 = f.read(30)
    f.seek(98) # x62 == 98
    myfile_62 = f.read(1)

salt = ord(no_pass_62.decode("hex")) ^ ord(myfile_62)

add_salt = True
word = ''
for i in range(0, 52, 4):
    xored = ord(no_pass_42[i:i+2].decode("hex")) ^ ord(myfile_42[i/2])
    if add_salt: xored = xored ^ salt
    # print i, myfile_42[i:i+2], xored, chr(xored)
    word = word + chr(xored)
    add_salt = not add_salt

print(word)
