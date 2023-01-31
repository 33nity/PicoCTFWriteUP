

#Rules

#Take each number mod. 37 and map it into the following character sets.       
#Numbers from 0 to 25 correspond to the letters of the alphabet (A-Z uppercase).
#Numbers from 26 to 35 correspond to the decimal digits which means from 0 – 9.
#The number 36 it’s an underscore ( _ ).

#the given message
msg = [54, 396, 131, 198, 225, 258, 87, 258, 128, 211, 57, 235, 114, 258, 144, 220, 39, 175, 330, 338, 297, 288]

#library to decode the message following the given rules.
library = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

#calculate mod.37 for every number in msg and append it to a new list then print the index.
for x in msg:
    results = x%37  
    print(library[results])



