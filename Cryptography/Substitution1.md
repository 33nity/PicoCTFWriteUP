## Challenge Statement
A second message has come in the mail, and it seems almost identical to the first one. Maybe the same thing will work again. Download the message [here](https://artifacts.picoctf.net/c/414/message.txt).
## Other Information
* Points: 100
* Subject: Cryptography, Substituton_cipher

## Aproach and process:
 * ***1.-*** I downloaded the file. I'm goint to be using the same tool as [Substitution0](https://github.com/33nity/PicoCTFWriteUP/blob/main/Cryptography/Substitution0.md)

### Message:

              IECj (jqfue cfu ixzelus eqs coxa) xus x emzs fc ifrzlesu jsiludem ifrzsededfy. 
              Ifyesjexyej xus zusjsyesk hdeq x jse fc iqxoosyasj hqdiq esje eqsdu iusxedgdem, 
              esiqydixo (xyk affaodya) jpdooj, xyk zuftosr-jfogdya xtdodem. Iqxoosyasj ljlxoom 
              ifgsu x ylrtsu fc ixesafudsj, xyk hqsy jfogsk, sxiq mdsokj x jeudya (ixoosk x coxa) 
              hqdiq dj jltrdeesk ef xy fyodys jifudya jsugdis. 
              IECj xus x ausxe hxm ef osxuy x hdks xuuxm fc ifrzlesu jsiludem jpdooj dy x jxcs, 
              osaxo sygdufyrsye, xyk xus qfjesk xyk zoxmsk tm rxym jsiludem auflzj xuflyk eqs hfuok cfu cly xyk zuxiedis. 
              Cfu eqdj zuftosr, eqs coxa dj: zdifIEC{CU3NL3YIM_4774IP5_4U3_I001_4871S6CT}

* ***2.-*** Knowing that picoCTF flag format is *picoCTF{flag}* I could know that the letters `Z, D, I, F, E and C` would correspond to `p, i, c, o, t, and f`.

* ***3.-*** By doing these with each letter I could easily guess the other correspondences and get the flag.



![0](https://user-images.githubusercontent.com/124062596/220339441-88c31993-4922-4f19-b540-2cfab0622583.PNG)



## Flag
 picoctf{fr3qu3ncy_4774ck5_4r3_c001_4871e6fb}
