"""write a program in which a function takes a string argument"""
"""that returns the first letter of every word in capitals"""
""">>> 'hello i'm fine'"""
"""     Hello I'm Fine"""

def LetterCapitalization(a):

    words = a.split(' ')

    for i in range(len(words)):
        words[i] = words[i][0].upper() + words[i][1:] 

    return ' '.join(words)

print(LetterCapitalization('hello how are you my boy'))

# Alternate Method
 a= "hello i'm fine"

 w = a.title()
 print(w)
                
""".title() is a beautiful object method that returns"""
"""the first letter of every word or every word in a sentence in capitals."""     
