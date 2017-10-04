'''
Created on February 9, 2016
@author: Marimikael Seibert
'''
def isVowel(chara):
    '''
    returns True if a character is included in "aeiou" or "AEIOU"
    '''
    if chara in "aeiouAEIOU":
        return True
    else:
        return False
    
def noVowels(word):
    '''
    returns True if a word (other than the first letter) does not have 
    an a,e,i,o,u, or y in it. Returns True when word is only 1 letter, regardless of 
    whether that letter is a vowel.
    '''
    restofword = word[1:]
    for i in range(len(restofword)):
        if restofword[i] in "aeiouyAEIOUY":
            return False  
    return True

def isVowelexception(chara):
    ''' 
    returns True if a character is a member of "aeiouy" or "AEIOUY"
    '''
    if chara in "aeiouyAEIOUY":
        return True
    else:
        return False

def firstVowelexception(word): 
    '''
    Discounting the first character of a word, returns the first vowel in a word, 
    defining a vowel as a member of "aeiouy" or "AEIOUY"
    '''
    for i in range(len(word)):
        if i == 0:
            pass
        elif isVowelexception(word[i]) == True:
            firstvowel = word[i]
            return firstvowel
    return 0 #in the context of this program, this will never happen because
            #this function will never be called on a word with no vowels 
            #or a word with no vowels other than the first letter 
 
def pigifyword(word):
    '''
    This method has one parameter word of type string. The parameter is a single word.  
    It returns a string that is the piglatin translation of the original word.
    '''
    firstchar = word[0]
    first2chars = word[0:2]
    if len(word) == 1:
        final_string = word + "-way"
        return final_string.strip()
    if isVowel(firstchar) == True:
        final_string = word + "-way"
        return final_string.strip()
    elif noVowels(word) == True:
        final_string = word + "-way"
        return final_string.strip()
    elif first2chars.lower() == "qu":  
        #assuming that words beginning with a "qu" will have a vowel immediately after the "qu"
        #I didn't find any cases that violated my assumption and a TA on Piazza said the assumption was OK
        restofword = word[2:]
        beginningofword = word[0:2]
        prefix = beginningofword +"ay"
        final_string = restofword + "-" + prefix
        return final_string.strip()
    else:
        restofword = word[1:]
        firstvowelinWord = firstVowelexception(word)
        firstvowelIndex = restofword.find(firstvowelinWord)
        correctIndex = firstvowelIndex + 1
        wordbeginning = word[0:correctIndex] + "ay"
        wordend = word[correctIndex:]
        final_string = wordend+"-"+wordbeginning
        return final_string.strip()

def pigifyall(phrase):
    '''
    returns a piglatin-ized string of string parameter phrase
    '''
    all = []
    for word in phrase.split():
        all.append(pigifyword(word))
    return ' '.join(all)

def unpigifyword(word):
    '''
    This method has one parameter word of type string that is in pig-latin. 
    It returns a string that is the translation of the pig-latin word into English.
    '''
    splitwords = word.split("-")
    if splitwords[-1] == "way":
        final_string = splitwords[0]
        return final_string.strip()
    else:
        prefix = splitwords[-1][:-2]
        final_string = prefix + "-".join(splitwords[0:-1])#correcting for words with a hyphen in the middle like "to-day"
        return final_string.strip()

def unpigifyall(phrase):
    '''
    returns an un-piglatin-ized string of string parameter phrase
    '''
    all = []
    for word in phrase.split():
        all.append(unpigifyword(word))
    return ' '.join(all)

def readFile(fname):
    '''
    returns a list of words read from file specified by fname
    '''
    f = open(fname)
    st = f.read()
    f.close()
    return st.split()

def writeFile(words, fname):
    '''
    write every element in words, a list of strings
    to the file whose name is fname
    put a space between every word written, and make
    lines have length 80
    '''
    LINE_SIZE = 80
    f = open(fname,"w")
    wcount = 0
    for word in words:
        f.write(word)
        wcount += len(word)
        if wcount + 1 > LINE_SIZE:
            f.write('\n')
            wcount = 0
        else:
            f.write(' ')
    f.close()
    
if __name__ == '__main__':
    # start with reading in data file
    words = readFile("romeo.txt")
    print "read",len(words),"words"
    result = ' '.join(words)
    # convert to piglatin and write to file
    pigstr = pigifyall(result)
    writeFile(pigstr.split(),"pig-romeo.txt")
    print "PIGIFIED romeo.txt"
    print pigstr[0:100]

    # read in pigified file
    words2 = readFile("pig-romeo.txt")
    result2 = ' '.join(words2)
    # unpigify file that was read
    unpigstr = unpigifyall(result2)
    # write to file "unpig-romeo.txt"
    writeFile(unpigstr.split(),"unpig-romeo.txt")
    print "UNPIGIFIED romeo.txt"
    print unpigstr[0:100]

