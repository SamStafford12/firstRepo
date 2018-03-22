pageBreak = "################ \n"
# + - * / // ** %

add = 2+2
print("This is the add variable")
print(add)
print(pageBreak)

minus = 3-2
print("This is the minus variable")
print(minus)
print(pageBreak)

mult = 2*2
print("This is the multiplication variable")
print(mult)
print(pageBreak)

div = 5/2
print("This is the division variable") 
print(div)
print(pageBreak)

roundeddiv = 5//2
print("This is the rounded division variable")
print(roundeddiv)
print(pageBreak)

expo = 2**3
print("This is the exponent variable")
print(expo)
print(pageBreak)

remainder = 5%2
print("This is the remainder variable")
print(remainder)
print(pageBreak)


print("This is defining a variable be sure is it defined before called for")
def printLyrics():
    lyrics = ("Im a lumberjack, and im really lazy.\n")
    lyrics = lyrics + ("i sleep all night and I work all day.")
    return lyrics


print(printLyrics())


i = 0
while i < 5:
    print('Hello')
    i += 1

for number in range(12, 20):
    print(number)

i = 0
j = 0
while i < 5:
    while j < 5:
        print(j, end='')
        j += 1
    print('\n#####################')
    j = 0
    i += 1



    



