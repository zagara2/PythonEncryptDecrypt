'''
Created on Feb 22, 2016

@author: Marimikael Seibert
'''
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

def shiftword(word, shift):
    '''
    Encrypts one word by a specified shift and returns that encrypted word
    '''
    the_alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    caesar_str_upper = the_alphabet_upper[shift:] + the_alphabet_upper[:shift]
    
    alphlower = "abcdefghijklmnopqrstuvwxyz"
    caesarlower = alphlower[shift:] + alphlower[:shift]
    
    blankstr = ""
    for letter in word:
        if letter.isalpha() == True:
            if letter.isupper() == True:
                letterIndex = the_alphabet_upper.find(letter)
                caesarLetter = caesar_str_upper[letterIndex]
                blankstr = blankstr + caesarLetter
            if letter.islower() == True:
               letterIndex = alphlower.find(letter)
               caesarLetter = caesarlower[letterIndex]
               blankstr = blankstr + caesarLetter             
        else:
            blankstr = blankstr + letter
    return blankstr
      
def encrypt(str, shift):
    '''
    Encrypts a phrase with multiple words by a specified shift and returns the encrypted phrase
    '''
    all = []
    for word in str.split():
        all.append(shiftword(word,shift))
    return ' '.join(all)

def eyeball(encrypted):
    '''
    Prints 26 rows, labeled with the value of the shift being applied, 
    an int from 0-25 inclusive, and the first 80 characters of the string that 
    results from applying a Caesar-cipher shift to the string parameter. 
    '''
    for x in range(26):
        xstr = str(x)
        row = xstr + " " + encrypt(encrypted, x)
        print row[0:80]

def decrypt(encrypted):
    '''
    Given an encrypted phrase, automatically returns the decrypted phrase.
    '''
    englishwordlist = readFile("melville.txt")
    maxnumberofwords = 0
    maxline = ""
    for x in range(26):
        row = encrypt(encrypted, x)
        row = row.split()
        engwordsinLine = 0
        for x in row:
            if x in englishwordlist:
                engwordsinLine = engwordsinLine + 1
        if engwordsinLine > maxnumberofwords:
            maxnumberofwords = engwordsinLine
            maxline = " ".join(row)
    return maxline

if __name__ == '__main__':
    # read in non-encrypted data file, tell number of words read
    words = readFile("little_brother.txt")
    print "read",len(words),"words"
    result = ' '.join(words)
    # encrypt and write to file "encrypted.txt" 
    encryptedstr = encrypt(result, 3)
    writeFile(encryptedstr.split(),"encrypted.txt")
    #print a sample from the new file
    print "Sample from ENCRYPTED file (little_brother.txt) with shift of 3:"
    print encryptedstr[0:100]
    print
    
     # read in encrypted file
    words2 = readFile("file2.txt")
    result2 = ' '.join(words2)
    # decrypt file that was read
    decryptstr = decrypt(result2)
    # write to file "decrypted.txt"
    writeFile(decryptstr.split(),"decrypted.txt")
    #print a sample from the new file
    print "Sample from DECRYPTED file (file2.txt):"
    print decryptstr[0:100]
    
    # This chunk of code demonstrates that the eyeball function works properly
    words3 = readFile("file1.txt")
    result3 = ' '.join(words3)
    print 
    print "Here's part of a file (file1.txt) to decrypt by eyeballing:"
    eyeball(result3)
    print
    print "You can figure out that a shift of 9 has been applied."


