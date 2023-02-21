## Challenge Statement
It seems that another encrypted message has been intercepted. The encryptor seems to have learned their lesson though and now there isn't any punctuation! Can you still crack the cipher? Download the message [here](https://artifacts.picoctf.net/c/107/message.txt).
## Other Information
* Points: 100
* Subject: Cryptography, Substituton_cipher

## Aproach and process:
 * ***1.-*** I downloaded the file. This time the message has no space between the characters. No problem, I'm going to crack it with the same online tool I used for solving [Substitution0](https://github.com/33nity/PicoCTFWriteUP/blob/main/Cryptography/Substitution0.md) and [Substitution1](https://github.com/33nity/PicoCTFWriteUP/blob/main/Cryptography/Substitution1.md).

### Message:
              gvjwjjoeugujajwqxzgvjwkjxxjugqfxeuvjivecvumvzzxmzbpsgjwujmswegrmzbpjgegezhuehmxsieh
              cmrfjwpqgwezgqhisumrfjwmvqxxjhcjgvjujmzbpjgegezhunzmsupwebqwexrzhurugjbuqibeheugwqg
              ezhnshiqbjhgqxukvemvqwjajwrsujnsxqhibqwdjgqfxjudexxuvzkjajwkjfjxejajgvjpwzpjwpswpzu
              jznqvecvumvzzxmzbpsgjwujmswegrmzbpjgegezheuhzgzhxrgzgjqmvaqxsqfxjudexxufsgqxuzgzcjg
              ugsijhguehgjwjugjiehqhijomegjiqfzsgmzbpsgjwumejhmjijnjhueajmzbpjgegezhuqwjzngjhxqfz
              wezsuqnnqewuqhimzbjizkhgzwshhehcmvjmdxeuguqhijojmsgehcmzhnecumwepguznnjhujzhgvjzgvj
              wvqhieuvjqaexrnzmsujizhjopxzwqgezhqhiebpwzaeuqgezhqhizngjhvqujxjbjhguznpxqrkjfjxeja
              jqmzbpjgegezhgzsmvehczhgvjznnjhueajjxjbjhguznmzbpsgjwujmswegreugvjwjnzwjqfjggjwajve
              mxjnzwgjmvjaqhcjxeubgzugsijhguehqbjwemqhvecvumvzzxunswgvjwkjfjxejajgvqgqhshijwugqhi
              ehcznznnjhueajgjmvhelsjueujuujhgeqxnzwbzshgehcqhjnnjmgeajijnjhujqhigvqggvjgzzxuqhim
              zhnecswqgezhnzmsujhmzshgjwjiehijnjhueajmzbpjgegezhuizjuhzgxjqiugsijhgugzdhzkgvjewjh
              jbrqujnnjmgeajxrqugjqmvehcgvjbgzqmgeajxrgvehdxedjqhqggqmdjwpemzmgneuqhznnjhueajxrzw
              ejhgjivecvumvzzxmzbpsgjwujmswegrmzbpjgegezhgvqgujjdugzcjhjwqgjehgjwjugehmzbpsgjwume
              jhmjqbzhcvecvumvzzxjwugjqmvehcgvjbjhzscvqfzsgmzbpsgjwujmswegrgzpelsjgvjewmswezuegrb
              zgeaqgehcgvjbgzjopxzwjzhgvjewzkhqhijhqfxehcgvjbgzfjggjwijnjhigvjewbqmvehjugvjnxqceu
              pemzMGN{H6W4B_4H41R515_15_73I10S5_8J1FN808}

* ***2.-*** At the botton of the text there's a certain piece of text: ***pemzMGN{H6W4B_4H41R515_15_73I10S5_8J1FN808}*** which look suspiciously like picoCTF flag format. I'm going to be using this piece of text to start cracking the letters `Z, D, I, F, E and C` that would correspond to `P, I, C, O, T, and F`.

* ***3.-*** If I take a look at the words before the flag I could guess the text was *The flag is*, this indicates that the letters `V, J, X, Q, C and U` which correspond to `H, E, L, A, G, and S`.

   ![1](https://user-images.githubusercontent.com/124062596/220344672-60ae5b78-fd6c-4dc6-be60-2cea41119589.PNG)

* ***4.-*** If you look closely to the flag there is just 7 letters left to be able to read the flag. These are: `H, W, B, R, I, S, and F`. I need to find a piece of text which contains and which allows me to guess these 7 letters.

* ***5.-*** Navigating through the text, at the beggining of it, I could see a piece containing the letters `B, S, W, R and H` which I've managed to read and decode. There are just to letters left: `F and I`.

    ![3](https://user-images.githubusercontent.com/124062596/220345645-aba989a4-105c-434f-ba68-d55ebff86b85.PNG)


* ***6.-*** The following words of these piece contains `F and I` which are so easy to guess.

    ![4](https://user-images.githubusercontent.com/124062596/220347185-ef7f9471-801e-49b3-9da5-def31bb317df.PNG)

* ***7.-*** Finally the flag was readable.

    ![6](https://user-images.githubusercontent.com/124062596/220347565-781412c7-6077-4ab2-83af-6c7183ebcb5c.PNG)


## Flag
picoctf{n6r4m_4n41y515_15_73d10u5_8e1bf808}
