"""
caesar.py - San Kwon
This program converts plaintext to a cyphertext through a caesar shift.
"""

abclower = "abcdefghijklmnopqrstuvwxyz"
abccaps = abclower.upper()

# This part asks for input and checks if it is an integer
shift = input("")
while shift.isdigit == False and shift.find(" ") != -1:
    shift = input("")
shift = int(shift)

# This part asks for plaintext
plain = input("plaintext: ")
cypher = ""

# This function converts a given letter to a new letter
def caesar(abc):
    newcharacter = abc[(abc.find(character) + shift) % 26]
    return(newcharacter)

# This converts the plaintext to cypher 
for i in range(len(plain)):
    character = plain[i]
    if character in abclower:
        cypher = cypher + caesar(abclower)
    elif character in abccaps:
        cypher = cypher + caesar(abccaps)
    else:
        cypher = cypher + character

print("cyphertext: " + cypher)
