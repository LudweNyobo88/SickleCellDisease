import time

#TRANSLATE FUNCTION
def translate(DNA_seq):                                 #Defining translate function with DNA_seq as a parameter
    
#Declaring the table of SLC and codon constants as a variable(dictionary)
    
    table = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'CTA':'L',
        'CTC':'L', 'CTG':'L', 'CTT':'L','TTA':'L',
        'TTG':'L', 'GTA':'V', 'GTC':'V','GTG':'V',
         'GTT':'V', 'TTC':'F', 'TTT':'F','ATG':'M',}
    
    protein =""

#Control statements
    
    if len(DNA_seq)%3 == 0:                                 #DNA_seq to handle sequences that of length divisible by 3
        for i in range(0, len(DNA_seq), 3):
            codon = DNA_seq[i:i + 3] 
            protein+= table[codon] 
    return protein

#User input

DNA_seq=input("enter sequence:\n").upper()

#Display
print(translate(DNA_seq))

#MUTATE FUNCTION
import re
def Mutate():
    readfile=open('DNA.txt','r')
    seq= readfile.read()
    search=re.search("[a]",seq).start()
    print(search)
    return search
Mutate()#Calling on the function

#Normal DNA text output
def Normal_DNA():
    readfile=open('DNA.txt','r')
    
    seq= readfile.read()
    seq = seq.replace("a", "A")
    ofile=open('Normal_DNA.txt','w')
    ofile.write(seq)
    ofile.close()
    return(seq)

Normal_DNA()#Calling on the function

#Mutated DNA text output
def Mutated_DNA():
    readfile=open('DNA.txt','r')
    seq1= readfile.read()
    seq1 = seq1.replace("a", "T")
    ofile=open('Mutated_DNA.txt','w')
    ofile.write(seq1)
    ofile.close()
    return(seq1)

Mutated_DNA()#Calling on the function



#TEXT TRANSLATE FUNCTION

def txtTranslate(inputfile):
    with open(inputfile,'r') as f:
     seq=f.read()
    return translate(seq)#Calling on the function within a function

#Amino Acid output#Display

print(txtTranslate('Normal_DNA.txt'))
print(txtTranslate('Mutated_DNA.txt'))

time.sleep(100)