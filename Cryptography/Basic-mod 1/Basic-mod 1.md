## Challenge Statement
We found this weird message being passed around on the servers, we think we have a working decryption scheme.

Download the message [here](https://artifacts.picoctf.net/c/393/message.txt).

Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. 
Wrap your decrypted message in the picoCTF flag format 
>(i.e. picoCTF{decrypted_message}).

## Other Information
* Points: 100
* Subject: Cryptography

## Aproach and process:
* ***1.-*** This exercise gives you an encrypted message. In order to get the flag, I’d had to decrypt it following certain rules. 

    **Those rules are:**

        • Take each number mod. 37 and map it into the following character sets.
        
        • Numbers from 0 to 25 correspond to the letters of the alphabet (A-Z uppercase).
        
        • Numbers from 26 to 35 correspond to the decimal digits which means from 0 – 9.
        
        • The number 36 it’s an underscore ( _ ).
    **The message:**

            54, 396, 131, 198, 225, 258, 87, 258, 128, 211, 57, 235, 114, 258, 144, 220, 39, 175, 330, 338, 297, 288
        
* ***2.-*** I used VS Code to create a python script that could solve this problem and decrypt the message. Once I created the script I ran it and got the flag.

### Script

        #the given message
        
          msg = [54, 396, 131, 198, 225, 258, 87, 258, 128, 211, 57, 235, 114, 258, 144, 220, 39, 175, 330, 338, 297, 288]

        #library to decode the message following the given rules.
        
          library = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

        #calculate mod.37 for every number in msg and append it to a new list then print the index.
        
          for x in msg:
              results = x%37  
              print(library[results])
            
            
## Flag
picoCTF{R0UND_N_R0UND_79C18FB3}
         
