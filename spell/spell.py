
def spell(word):
    '''little spelling game I made for my 3 year old.
    
    Parameters
    ----------
    word : str
        The word to be spelled
        
    Returns
    -------
    None
    
    Examples
    --------
    >>> spell('happy')
    Spell the word: happy
    h
    Great!
    ...
    h____
    ...
    a
    Great!
    ...
    ha___
    ...
    p
    Great!
    ...
    hap__
    ...
    y
    ...
    Try again!
    hap__
    ...
    p
    Great!
    ...
    happ_
    ...
    y
    Great!
    ...
    happy
    ...
    ...
    Yaaaaaaay!!!
    You spelled "happy"!
    ...
    '''
    print('Spell the word: {}'.format(word))
    letter = 0
    spelled = []
    letters_left = '_' * len(word)
    while letter < len(word):
        x = input()
        if x.lower() == word[letter].lower():
            spelled.append(x)
            print('Great!')
            print()
            letters_left = letters_left[:-1]
            print(''.join(spelled)+letters_left)
            print()
            letter += 1
            if letter == len(word):
                print('\nYaaaaaaay!!!')
                print('You spelled "{}"!\n'.format(''.join(spelled)))
                break
        else:
            print('\nTry again!')
            print(''.join(spelled)+letters_left)
            print()
