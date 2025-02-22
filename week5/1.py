import re 
f=open("input.txt","r",encoding="utf-8")
text=f.read()
#1
def ppp(string):
    pattern = r'ab*' 
    if re.fullmatch (pattern,string):
        return True
    return False

strings=text 
for s in strings:
    print(f"'{s}' matches: {ppp(s)}")

#2
def nnn(string):
    pattern=r'ab{2,3}'
    if re.fulllmatch(pattern,string):
        return True 
    return False 

strings=text 
for n in strings:
    print(f"'{n}' matches: {nnn(n)}")

#3
def lll(string):
    pattern=r'\b[a-z]+_[a-z]+\b'
    return re.findall(pattern,string)

#4
def fff(string):
    pattern=r'[A-Z][a-z]+'
    return re.findall(pattern, string)

#5
def mmm(string):
    pattern=r'a.*b$'
    return bool (re.fullmatch(pattern,string))

#6
def rrr(string):
    pattern=r'[ ,.]'
    return re.sub(pattern,':',string)

#7
def sss(string):
    return ''.join(word.capitalize() for word in string.split('_'))

#8
def sp(string):
    pattern=r'[A-Z][^A-Z]*'
    return re.findall(pattern,string)

#9
def iii(string):
    pattern=r'([A-Z][a-z]*)'
    return ' '.join (re.findall(pattern,string))

#10
def ccc(string):
    pattern=r'([a-z][A-Z])'
    return re.sub(pattern, r'\1_ \2', string).lower()

