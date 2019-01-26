def set_word(word,unlock_letter=''):
    temp=''
    for a in word:
        if a.upper()==unlock_letter.upper():
            temp+=a
        elif a.upper()  not in 'AEIOU':
            temp+='_'
        else:
            temp+=a
    return temp.upper()

print set_word('HOLLA','l')
