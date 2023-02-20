## Challenge Statement
This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can. You can download the file from [here](https://artifacts.picoctf.net/c/323/Flag.pdf).

## Other Information
* Points: 100
* Subject: Forensics

## Aproach and process:
 * ***1.-*** Downloaded the and run `file` utility to determine the file type. I change the file permissions with the command `chmod +x` and the file
name with the command `mv` from ***Flag.pfd*** to ***Flag.sh*** in order to execute it.

* ***2.-*** I extracted a file called ***flag*** which is `ar` archive. In order to extract it I used `Binwalk` with arguments `-e` (automatically
extract known file types) and `--run-as=root` (indicate root user).

* ***3.-*** This created a folder called ***_flag.extracted***. In this folder there is a file called ***64***. I ran the
command `file` on it. It indicates it’s a `GZIP` compressed data file, so I ran again `Binwalk` with the same options as the step before.

* ***4.-*** This created a folder called ***_64.extracted*** with two files: ***Flag.gz’*** and ***flag***. I ran file command on ***flag*** and determines it 
is a `LZIP` compressed archive. Then I decompressed ***flag.gz*** and result in the same `LZIP` file than before so I worked with it. I tried to decompress 
the file with `Binwalk`, but it doesn’t work so I installed `LZIP` (`apt-get install lzip`) in order to do so. (I will have to do this installation step with `LZ4`,
`LZMA` and `LZOP` in the following steps) Once I installed it, I decompressed the file called ***flag*** with `LZIP` and the options `-d` (for decompress) and `-k` 
(to keep the output during compression or decompression). Finally, I obtained a file called ***flag.out***.

* ***5.-***  I used the command `file` again to determine de file type of ***flag.out*** and it indicates it is a `LZ4` compressed file. I used `LZ4 -d -k` to decompres
the file.

* ***6.-*** I used `file` again to determine the file type of the extract file and it indicates it is a `LZMA` compressed file. If I try to decompress it with `LZMA` 
it doesn’t work because I need to change the file from ***flag1.out*** to ***flag1.lzma*** with `mv`. Then I proceed to decompress it with `LZMA -d -k`.

* ***7.-*** It created the file ***flag1***. The command file indicates this is a `LZOP` compressed file. In order to decompress it with `LZOP` I need to change the name 
of the file from ***flag1*** to ***flag1.lzop*** with the command `mv` and I ran `LZOP` with `-d` and `-k` options and an output called ***flag2***.

* ***8.-*** I used `file` again to determine the file type and it indicates it is a `LZIP` compressed file. I used `LZIP` with options `-d` and `-k` to decompress it and extract 
the file.

* ***9.-*** I got a file called ***flag2.out*** which it’s a `XZ` compressed file. In order to decompress it I need to change the name of ***flag2.out*** to ***flag3.xz***. Then
I ran `XZ -d -k` and obtain an ***ASCII*** text file. I ran the command `cat` to see the text.


* ***10.-*** Finally copyed the ***ASCII*** string into `CyberChef`and decode the flag.

## Flag
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_3c79c5ba}
