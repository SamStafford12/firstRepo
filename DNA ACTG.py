hello = """TCATCCGACGCCGAGGCTAATAGCAATTGACGTGGGTAGTACCTAGGGTAACATTACATG
GACCTCCTGTCGCACCTTTACTTCGCAGGGAGCTGCTTCGTACACGCGCTGTTCAGCCTA
AGTTTTCTGGCGCAGACTTACTCGGTTCGTCAGACCACCGTTATCGTGTTTATTAGTTTG
AGGAAATAGCTCCCTCGAAGTAGTGCAGTGCGGGGGCGAGCCAAACAAGGGGGCTCCGCG
CTACCTATTGTTCATTTCGGTGAGACAGTAACTAGTCGTTCGATAGCCGGCAAGCCTAAA
GCCTATTCGCAGTCCCATCAATAGGGGCATATGAATAGTTCCTGGGTTCCGTAAGTCCAG
ATTGCCCACAGGTACACTATTTAGTGCTGGGTGTGGTTGGTGCTCACTGCTTCTTGGGGC
ATGAAAGCGTATCCTTTTAACACTGTACGTGGAAGACTTTGAAACGGCCCTGCAGGCACT
ACTCGCGGTTGATAAAAGGCCGCGACGTAAAAAAACCATGTCAATTCGAACGAGGCACGA
TCACACCAATCATCTACTACGCCTGTATTAAACGGGAAAGGCACGGCCGAGGTAGAGTAC
TAGCTCCCAGTGGATACCGTTGAAGAGCGATTTAGTTACAAGATATTAACATTTGGGTAG
GTGGAGTCGTGTCAGTCTAACCCGCTGTCACGGTAGAAGTTGGATCGTAAAGTGAATGGA
ACACTCCCAGCCTTGCCTCAACCCGCATGATAGAAAAGATATCGAAGGGATAAAGCAGCT
AGGGGAGGATCAAGACTTTCTTGTGTCAAAACTCTTATCTTTGACCGCGATACTTCTGGA
TCGAGGATAGCTACTGGAGATATGTTACGGAGATTAGACGCCCGAAGATTTTTACAGTTT
CACTTTCCTTGTAGATTG"""
tally_c = 0
tally_g = 0
tally_a = 0
tally_t = 0
for letter in hello:
    if letter == 'C':
        tally_c +=1
    if letter == 'G':
        tally_g +=1
    if letter == 'A':
        tally_a +=1
    if letter == 'T':
        tally_t +=1
  
add = tally_a + tally_c + tally_g + tally_t
print(add)

divide = tally_a / add
multiply = divide * 100
print("the percent of A is")
print(multiply)

divide = tally_c / add
multiply = divide * 100
print("the percent of C is")
print(multiply)

divide = tally_g / add
multiply = divide * 100
print("the percent of G is")
print(multiply)

divide = tally_t / add
multiply = divide * 100
print("the percent of T is")
print(multiply)


