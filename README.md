# accessor
remember ms access db password

The inspiration for this prgram came from the web page:
  http://tutorialsto.com/database/access/crack-access-*.-mdb-all-current-versions-of-the-password.html

The program takes one parameter, the name of an ms access database file and attempts to remind you of the
password you forgot that is protecting the file.

The password is hidden at position 0x42 in the file, and each character of the password occurs at every second
byte (at bytes, 0x42, 0x44, 0x46, ...) I don't know the length limit here, but I heard it may be 13 characters.
There are also standard values at these positions if a password is not set. These standard values are XOR'd 
against the password bytes in order to produce the protected passord. Deviously, every second password character
starting at the first is also XOR'd against the result of an XOR between the byte at 0x62 in the password
protected file and byte 0x62 in the standard, non-password protected file.

This is a first effort and is not tested thoroughly against various versions.

This program should not be used for hacking or cracking purposes and is purely for educational purposes.
