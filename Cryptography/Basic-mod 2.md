## Challenge Statement
A new modular challenge!
Download the message [here](https://artifacts.picoctf.net/c/499/message.txt).
Take each number mod 41 and find the modular inverse for the result. 
Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Other Information
* Points: 100
* Subject: Cryptography

## Aproach and process:
* ***1.-*** This exercise gives you an encrypted message. In order to get the flag, I’d had to decrypt it following certain rules. We did this before. 

    **Those rules are:**

        • Take each number mod. 41, then find the ***modular inverse*** for the results and map it according these rules:
        
        • Numbers from 1 to 26 correspond to the letters of the alphabet (A-Z uppercase).
        
        • Numbers from 27 to 36 correspond to the decimal digits which means from 0 – 9.
        
        • The number 37 it’s an underscore ( _ ).
    **The message:**

            268, 413, 110, 190, 426, 419, 108, 229, 310, 379, 323, 373, 385, 236, 92, 96, 169, 321, 284, 185, 154, 137, 186
        
* ***2.-*** I used VS Code to create a python script that could solve this problem and decrypt the message.

### Script

      msg = [268, 413, 110, 190, 426, 419, 108, 229, 310, 379, 323, 373, 385, 236, 92, 96, 169, 321, 284, 185, 154, 137, 186]
      library = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
      
      for x in msg:
        result = pow(x, -1, 41)
        print(library[result-1]
            
            
## Flag
picoCTF{1NV3R53LY_H4RD_C680BDC1}
         
