def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
    
    
OR

def pig_it(text):
    word = text.split(' ')
    res = []
    for i in word:
        if i[:-2] + i[:-1] != 'ay' and i[0].isalpha():
            temp = i[1:] + i[0] + 'ay'
            res.append(temp)
        else:
            res.append(i)
    return ' '.join(res)

# Test Cases

print(pig_it('Pig latin is cool'))
print(pig_it('This is my string'))



OR

def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res)
