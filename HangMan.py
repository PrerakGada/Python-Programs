import random

words = [''] # Type your word list here
word = random.choice(words)
hangman = ''
s = ''
chance = 10
l = len(word)
a = 0
w = ''
check = 0
for p in range(0, l):
    hangman += '-'
while chance > 0 and hangman != word:
    print(w)
    print(hangman)
    print('Chances left :', chance)
    c = input('Guess a character: ')
    c = c.lower()
    if c in word:
        s += c
        sl = len(s)
        hangman = ''
        for x in range(0, l, 1):
            for j in range(0, sl, 1):

                if (s[j] == word[x]):
                    hangman += s[j]
                    a = 1
            if (a != 1):
                hangman += '-'
            a = 0
    else:
        chance -= 1
        w = w + c + ' '
    if (hangman == word):
        check = 1
if (check == 1):
    print(hangman)
    print('You won!!')
else:
    print('Chances Over!!')
