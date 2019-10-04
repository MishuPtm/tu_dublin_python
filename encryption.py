"""
Author: Ionut Petrescu
Date: 01.01.2019
Encryption exercise

"""


def encrypt(text, key_nb = 1):
    output = ""
    for char in text:
        output = chr(ord(char)+key_nb) + output
    return output


def decrypt(text, key_nb = 1):
    output = ""
    for char in text:
        output = chr(ord(char)-key_nb) + output
    return output


examples = ["/ztbF!tj!hojnnbshpsq!/hojnnbshpsq!fwpM!J",
            "/sfuvqnpd!b!op!ovs!pu!tofqqbi!utvk!ubiu!hojwmpt.nfmcpsq!op!zbttf!ob!tj!nbshpsq!B",
            "ubfsh!tj!opiuzQ",
            "fujsx!pu!fwbi!uoeje!vpz!fojm!fiu!tj!fupsx!sfwf!vpz!fepd!gp!fojm!utfc!fiU"]

for example in examples:
    print(decrypt(example))