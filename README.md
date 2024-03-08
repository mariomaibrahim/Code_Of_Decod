enmorse= {"a":"*-", "b":"-***", "c":"-*-*", "d":"-**", "e":"*", "f":"**-*", "g":"--*", "h":"****", "i":"**", "j":"*---", "k":"-*-", "l":"*-**", "m":"--", "n":"-*", "o":"---", "p":"*--*", "q":"--*-", "r":"*-*", "s":"***", "t":"-", "u":"**-", "v":"***-", "w":"*--", "x":"-**-", "y":"-*--", "z":"--**", " ":"|"}

demorse= {"*-":"a", "-***":"b", "-*-*":"c", "-**":"d", "*":"e", "**-*":"f", "--*":"g", "****":"h", "**":"i", "*---":"j", "-*-":"k", "*-**":"l", "--":"m", "-*":"n", "---":"o", "*--*":"p", "--*-":"q", "*-*":"r", "***":"s", "-":"t", "**-":"u", "***-":"v", "*--":"w", "-**-":"x", "-*--":"y", "--**":"z", " ":"|"}



try1 = input("Enter <encrypt> or <decrypt>: ")



if try1 == "encrypt":

    en = input("Enter your text: ").lower()  

    text1 = ""

    for char in en:

        if char in enmorse:

            text1 += enmorse[char] + " "  

        else:

            text1 += " "  

    print(text1)

elif try1 == "decrypt":

    de = input("Enter your code: ")

    de = de.split() 

    text2 = ""

    for char in de:

        if char in demorse:

            text2 += demorse[char]  

            text2 += " "  

    print(text2)

else:

    print("This is only morse")
