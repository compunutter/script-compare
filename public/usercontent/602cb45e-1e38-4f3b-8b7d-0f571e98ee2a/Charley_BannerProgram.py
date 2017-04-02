text = 'Python|12|Python is great'.split('|')

stars = []
words = []
for word in text:
        stars.append('*'*(len(word)+2))
        words.append('*'+word+'*')


print('\n',' '.join(stars),'\n',' '.join(words),'\n',' '.join(stars),'\n')


