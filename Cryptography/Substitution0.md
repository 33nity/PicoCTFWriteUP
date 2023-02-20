## Challenge Statement
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher? Download the message [here](https://artifacts.picoctf.net/c/379/message.txt).
## Other Information
* Points: 100
* Subject: Cryptography, Substituton

## Aproach and process:
 * ***1.-*** I downloaded the file and searched for a tool online. It's a substitution challenge so I search for frequency analysis tool online and found [this one](https://math.dartmouth.edu/~awilson/tools/frequency_analysis.html). This is the tool I'm going to be using futher on this exercise.
### Quick didactic break:
* Why frecuency analysis?

In cryptanalysis, frequency analysis (also known as counting letters) is the study 
the frequency of letters or groups of letters in a ciphertext. 
The method is used as an aid to breaking classical ciphers. 
In this case the challenge is to crack a substitution cipher which is a classical one.

### Message:

                      Mjbjhfly Ujcbeyz eblgj, rxpm e cbenj eyz gpepjui exb, eyz kblhcmp dj pmj kjjpuj
                      tbld e cuegg segj xy rmxsm xp reg jysulgjz. Xp reg e kjehpxthu gsebekejhg, eyz, ep
                      pmep pxdj, hyqylry pl yephbeuxgpg—lt slhbgj e cbjep fbxwj xy e gsxjypxtxs flxyp
                      lt nxjr. Pmjbj rjbj prl blhyz kuesq gflpg yjeb lyj jvpbjdxpi lt pmj kesq, eyz e
                      ulyc lyj yjeb pmj lpmjb. Pmj gseujg rjbj jvsjjzxycui mebz eyz culggi, rxpm euu pmj
                      effjebeysj lt khbyxgmjz cluz. Pmj rjxcmp lt pmj xygjsp reg njbi bjdebqekuj, eyz,
                      peqxyc euu pmxycg xypl slygxzjbepxly, X slhuz mebzui kuedj Ohfxpjb tlb mxg lfxyxly
                      bjgfjspxyc xp.

                      Pmj tuec xg: fxslSPT{5HK5717H710Y_3N0UH710Y_59533E2J}

* ***2.-*** Knowing that picoCTF flag format is *picoCTF{flag}* I could know that the letters `F, X, S, L, P and T` would correspond to `p, i, c, o, t, and f`.

* ***3.-*** By doing these with each letter I could easily guess the other correspondences and get the flag.

![6](https://user-images.githubusercontent.com/124062596/220174442-b0dcefd1-0e3a-4dcc-8a5e-3e9660d1580c.PNG)

## Flag
picoCTF{5ub5717u710n_3v0lu710n_59533a2e}
