def xx(word, strs):
    word = [i for i in word]
    strs = [i for i in strs]
    for i in word:
        if i in strs:
            strs.remove(i)
    
    if strs == []:
        return True
    
    return False
    
xx("bat","tab")
