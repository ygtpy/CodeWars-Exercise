# tek mi cift mi 1

def even_or_odd(num):
   
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("input number "))
print(even_or_odd(number))

#%%  tek mi cift mi 2

def even_or_odd2(num):
    return ["Even","Odd"][num % 2]

number = int(input("input number "))
print(even_or_odd2(number))


#%% isim yazdirma 1

def greet(name):
    return f"Hello, {name} how are you doing today?"

print(greet("ayse"))


#%% liste icinde hedef kontrolu 1

def check(liste,hedef):
    return  hedef in liste


liste = [1, 2, 3, 4, 5]
hedef = 3

print(check(liste,hedef))


#%% liste icinde hedef kontrolu 2  

def check(value1,array1):
    
    if value1 in array1:
        return True
    else:
        return False


array1 = [1, 2, 3, 4, 5]
value1 = 3

print(check(value1,array1))


#%% liste icinde hedef kontrolu 3

from typing import List, Union

def check(seq: List[Union[int, str]], elem: Union[int, str]) -> bool:
    """ Check if the element is in the array. """
    return elem in seq

#%% liste icinde hedef kontrolu 4

check=lambda array1,value1: value1 in array1

array1 = [1, 2, 3, 4, 5]
value1 = 3
print(check(array1, value1))

#%% liste icinde hedef kontrolu 5

def check(array1, value1):
    return array1.count(value1) > 0


array1 = [1, 2, 3, 4, 5]
value1 = 3
print(check(array1, value1))


#%% split ile cumleyi kelimelere cevirme 1

def string(text):
    return text.split()


text = "Merhaba dünya! Python öğreniyorum."
print(string(text))

#%% split ile cumleyi kelimelere cevirme 2

def string_to_array(string=''):
    return string.split() if string else ['']


string = "Merhaba dünya! Python öğreniyorum."
print(string_to_array(string))
#%% split ile cumleyi kelimelere cevirme 3

def deneme(cumle):
    return cumle.split() or [" "]

cumle = " "
print(deneme(cumle))

#%% split ile cumleyi kelimelere cevirme 4

def deneme2(cumle):
    word = []
    if cumle == " ":
        word.append(cumle)
    else:
        word = cumle.split()
    return word
cumle = "Merhaba dünya! Python öğreniyorum."
print(deneme2(cumle)) 


#%% calisma ve tatil durumuna gore alarm kuran  1

def set_alarm(employed, vacation):
    
    if employed:
        if vacation:
            return False
        return True
    return False


print(set_alarm(False, True))

#%% calisma ve tatil durumuna gore alarm kuran funcion 2

def alarm(work,tatil):
    if work and not tatil:
        return True
    else:
        return False

print(alarm(True, False))

#%% calisma ve tatil durumuna gore alarm kuran function 3

set_alarm = lambda e, v: e > v
print(set_alarm(True,False))    
    
    
#%% cuboid(dikdortgen prizma) hacim hesapla 1

def calc(uzunluk, genislik, yukseklik):
    return uzunluk*genislik*yukseklik

print(calc(10, 10, 1))



#%% cuboid(dikdortgen prizma) hacim hesapla 2
import math

def calc(*vol):
    return math.prod(vol)

print(calc(10, 10, 1))



# *vol fonksiyonun sınırsız degisken almasini saglar
# math.prod parantez icerisindeki degiskenin tuttugu sayilari carpar
a = 2,3,4,5
print(math.prod(a)) # cikti = 120

#%% cuboid(dikdortgen prizma) hacim hesapla 3

from functools import reduce

def calc(*args):
    return int(reduce(lambda x,y: x*y, args))
              
print(calc(3, 4, 5))

# --- reduce func---
# def multiply(x, y):
#     return x * y

# numbers = [1, 2, 3, 4, 5]

# result = reduce(multiply, numbers)

# İlk olarak, listedeki ilk iki öğeyi (1 ve 2) çarpar: 1 * 2 = 2
# Sonra, bu sonucu listedeki üçüncü öğe ile çarpar: 2 * 3 = 6
# Ardından, bu sonucu listedeki dördüncü öğe ile çarpar: 6 * 4 = 24

#%% ya donemleri hesapla 1
def quarter_of(month):
    
    if month > 12 or month <= 0:
        return None
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    else:
        return 4
    
    
print(quarter_of(11))

#%% ya donemleri hesapla 2

def month_calc(ay):
    donem = {1:1,2:1,3:1,4:2,5:2,6:2,7:3,8:3,9:3,10:4,11:4,12:4}
    return donem.get(ay,None)

print(month_calc(11))


#%% isogram hesapla 1

def isogram(cumle):
    cumle = cumle.lower()
    char = set()
    
    for i in cumle:
        if i.isalpha():
            if i in char:
                return False
            char.add(i)
    return True

print(isogram("Dermatoglyphics"))
print(isogram("isogram"))
print(isogram("aba"))
print(isogram("moOse"))
print(isogram(""))

#%% isogram hesapla 2

def isogram2(cumle):
    return len(cumle) == len(set(cumle.lower()))


print(isogram2("Dermatoglyphics"))
print(isogram2("isogram"))
print(isogram2("aba"))
print(isogram2("moOse"))
print(isogram2(""))

#%% isogram hesapla 3

def isogram3(cumle):
     cumle = cumle.lower()
     
     for i in cumle:
         if cumle.count(i) >1:
             return False
     return True
  

print(isogram3("Dermatoglyphics"))
print(isogram3("isogram"))
print(isogram3("aba"))
print(isogram3("moOse"))
print(isogram3(""))

#%% isogram hesapla 4

deneme = lambda cumle: len(set(cumle.lower())) == len(cumle)


print(isogram3("Dermatoglyphics"))
print(isogram3("isogram"))
print(isogram3("aba"))
print(isogram3("moOse"))
print(isogram3(""))

#%% DNA

def dne(dna):
    karsilik= {"A":"T", "T":"A", "G":"C", "C":"G"}
    birlestir = ''.join(karsilik[i] for i in dna)
    return birlestir

print(dne("AATG"))
#%% DNA

karsilik= {"A":"T", "T":"A", "G":"C", "C":"G"}
def dnaa(dna):
    return ''.join([karsilik[x] for x in dna])


print(dnaa("AATG"))

#%% DNA

import string

def dnna(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

print(dnna("AATG"))

#%% tek cift

def calc(number):
    if number % 2 != 0:
        return number * 9
    else:
        return number * 8
    
    
print(calc(2))
print(calc(1))
print(calc(8))
print(calc(4))
print(calc(5))

#%% tek cift

calc3 = lambda number: number * 9 if number % 2 != 0 else number*8 

print(calc3(2))
print(calc3(1))
print(calc3(8))
print(calc3(4))
print(calc3(5))

#%%

def simple_multiplication(numara) :
    return numara * (8 + numara%2)


#%% play bonjo

def kontrol(name):
    liste= {}
    for i in range(1):
        if name[i] == "r" or name[i] == "R":
            return f"{name} plays banjo"
        else:
            return f"{name} does not play banjo "

print(kontrol("martin"))
print(kontrol("bravo"))
print(kontrol("rolf"))
print(kontrol("Rikke"))


#%% play bonjo 

def kontrol(name):
    if name[0] == "r" or name[0] == "R":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
print(kontrol("martin"))
print(kontrol("bravo"))
print(kontrol("rolf"))
print(kontrol("Rikke")) 

#%% play bonjo

kontrol = lambda name: f"{name} plays banjo" if name[0].lower() == 'r' else f"{name} does not play banjo"

print(kontrol("martin"))
print(kontrol("bravo"))
print(kontrol("rolf"))
print(kontrol("Rikke")) 

#%% cumledeki kelimelerin bas harflerini buyuk yazdir

def up(string):
    return " ".join(word.capitalize() for word in string.split())
    # return string.title() 


print(up("How can mirrors be real if our eyes aren't real"))


#%% cumledeki kelimelerin bas harflerini buyuk yazdir

def up(string):
    words = string.split()
    cap_words = [word[0].upper() + word[1:].lower() if word else "" for word in words]
    
    return " ".join(cap_words) 


print(up("How can mirrors be real if our eyes aren't real"))


#%% cumledeki kelimelerin bas harflerini buyuk yazdir


def deneme(cumle):
    kelimeler = cumle.split()
    hallet = [kelime[0].upper() + kelime[1:].lower() if kelime else "" for kelime in  kelimeler]
    return ' '.join(hallet)


print(deneme("How can mirrors be real if our eyes aren't real"))

#%% string to int
def deneme(number):
    return int(number)


print(deneme("2345"))
#%% string to int


def deneme1(number):
    num_int=0
    for char in number:
        num_int = num_int * 10 + (ord(char) - ord("0"))
    return num_int


print(deneme("345"))

#%%  her karakteri bir kez tekrar et

def f(kelime):
    cikti = "".join([karakter * 2 for karakter in kelime])
    return cikti 

print(f("naber"))


#%% her karakteri bir kez tekrar et

def f(kelime):
    sonuc = ""
    
    for harf in kelime:
        sonuc += harf * 2
    return sonuc

print(f("naber"))

#%% 

def maxx(liste):
    liste.sort()
    return liste[-1]

print(max([-52, 56, 30, 29, -54, 0, -110]))

def minn(liste):
    liste.sort()
    return liste[0]

print(min([-52, 56, 30, 29, -54, 0, -110]))


#%%
def maxxx(liste):
    return max(liste)

def minnn(liste):
    return min(liste)

print(maxxx([-52, 56, 30, 29, -54, 0, -110]))
print(minnn([-52, 56, 30, 29, -54, 0, -110]))

#%%

def find_min(liste):
    if len(liste) == 0:
        return None
    
    min_v = liste[0]
    
    for numara in liste:
        if numara < min_v:
            min_v = numara
    return min_v

print(find_min([-52, 56, 30, 29, -54, 0, -110]))

def find_max(liste):
    if len(liste) == 0:
        return None
    
    max_v= liste[0]
    for numara in liste:
        if numara > max_v:
            max_v = numara
    return max_v

print(find_min([-52, 56, 30, 29, -54, 0, -110]))

#%% [new_element for element in iterable]

def number(lines):
    return [f"{i+1}: {line}" for i, line in enumerate(lines)]

print(number(["a", "b", "c"])) 

#%% enumerate(iterable, start=0)

def indexle(metin):
    return [f"{index}: {kelime}" for index, kelime in enumerate(metin,start=1)]

print(indexle(["a", "b", "c"]))



#%%

def indexle(cumle):
    sonuc = []
    for index, kelime in enumerate(cumle,1):
        sonuc.append(f"{index}: {kelime}")
    return sonuc
print(indexle(["a", "b", "c"]))

#%%  yazilan sayilari int cevirip topla

def hesapla(sayilar):
    toplam = sum(int(x) for x in sayilar)
    return toplam

print(hesapla([9, 3, '7', '3'])) 

#%% yazilan sayilari int cevirip topla

def hesapla2(num):
    return sum(map(int, num))

print(hesapla2([9, 3, '2', '3']))


#%% yazilan sayilari int cevirip topla

def hesapla3(num):
    sonuc = 0
    for i in num:
        sonuc += int(i)
    return sonuc
print(hesapla2([9, 3, '2', '23']))

#%%

def litres(time):
    return (time * 0.5) //1
print(litres(11.8))

#%%

def litres2(time):
    return "haha loser" if time < 0 else int(time/2)

print(litres2(11.8))
print(litres2(-2))




#%%

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
    
print(bool_to_word(True))

#%%

bool_to_word2 = lambda boolean: "Yes" if boolean else "No"
print(bool_to_word2(False))

    

#%%

bool_to_word3 = {True:"Yes", False:"No"}.get


print(bool_to_word3(True))


#%% toplama

def summation(num):
    n = 0
    for i in range(num +1):
        n += i
    return n
print(summation(4))

#%%  toplama

def summation2(num):
    return sum(range(num+1))
print(summation2(4))

#%% Gauss'un toplama formülü

def summation3(num):
    return num*(num+1)//2
print(summation3(4))

#%% otobus durak yolcu 

def number(bus_stops):
    yolcu = 0
    for durak in bus_stops:
        yolcu += durak[0]
        yolcu -= durak[1] 
    return yolcu
        
        
print(number([[10,0],[3,5],[5,8]])) # 5
#%% otobus durak yolcu

def number2(bus_stop):
    return sum(binen - inen for binen, inen in bus_stop)

print(number([[10,0],[3,5],[5,8]])) # 5

#%% basic calc

def hesap(operator,value1,value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2
  
print(hesap("%", 10, 5))  
  
#%% basic calc

hesap2 = lambda op, val1, val2: val1 + val2 if op == "+" else val1 - val2 \
    if op == "-" else val1 * val2 if op == "*" else val1 / val2 if op == "/" else None

print(hesap2("/", 10, 5))  

#%% basic calc
def basic_op(o, a, b):
    return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)

print(basic_op("*", 10, 5))

#%% basic calc
def basic_op(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')

print(basic_op("-", 10, 5))


#%%  basic calc

def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))
print(basic_op("+", 10, 5))
 
#%% basic calc
def basic_op(operator, value1, value2):
    ops = {'+': lambda a, b: a + b, 
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b}
    return ops[operator](value1, value2)

print(basic_op("+", 10, 5))


#%% basic calc
from operator import add, truediv, mul, sub, mod

def basic_op(op, a, b):
    operations = {
        '+': add,
        '/': truediv,
        '*': mul,
        '-': sub,
        '%': mod
    }
    if op in operations:
        return operations[op](a, b)
    else:
        return "Geçersiz operatör"

print(basic_op("+", 10, 5))
print(basic_op("^", 10, 5)) 
#%% convert number to negative

def make_negative(number):
    if number < 0:
        return number
    elif number == 0:
        return number
    else:
        return - + number
print(make_negative(0))

#%% convert number to negative

def make_negative(number):
    return -abs(number)

print(make_negative(123))


#%% fuel calc

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left >= distance_to_pump / mpg:
        return True
    else:
        return False
    
print(zero_fuel(100, 50, 1))


#%% fuel calc

def zero_fuel(dist, mpg, fuel):
    return mpg*fuel >= dist

print(zero_fuel(100, 100, 1))

#%% kare dikdortgen hesapla

def area_or_perimeter(l , w):
    return l * w if l == w else 2*(l+w)

print(area_or_perimeter(4, 4))
print(area_or_perimeter(6, 10))

#%% do you factor 
def check_for_factor(base, factor):
    if base % factor == 0:
        return True
    else:
        return False
         

print(check_for_factor(24612, 3)) #True
print(check_for_factor(9, 2)) # False

#%% do you factor 

def check_for_factor(base, factor):
    return base % factor == 0

print(check_for_factor(24612, 3)) #True
print(check_for_factor(9, 2)) # False

#%% is it triangle

def test(a,b,c):
    aa,bb,cc = sorted([a,b,c])
    return cc < aa + bb

print(test(4, 5, 8))


#%% rock paper scissors

def play(p1, p2):
    return ("Draw!" if p1 == p2
            else "Player 1 won!" 
            if (p1 == "scissors" and p2 == "paper") or
               (p1 == "rock" and p2 == "scissors") or
               (p1 == "paper" and p2 == "rock")
            else "Player 2 won!")

print(play("scissors", "paper"))
print(play("scissors", "rock"))
print(play("paper", "paper"))


#%%

def feast(beast,dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1 ]

print(feast("great blue heron", "garlic naan"))
print(feast("chickadee", "chocolate cake"))
print(feast("brown bear", "bear claw"))

#%% ziplayan top sees

def bouncingBall(h, bounce, window):
    if h <=0 or bounce <= 0 or bounce >=1 or window >= h:
        return -1
    return 2 + bouncingBall(h*bounce, bounce, window)

print(bouncingBall(3, 0.6, 0.5))


#%% ziplayan top sees

def bouncingBall2(h, bounce, window):
    if not (0 < bounce < 1) or h <= 0 or window >=h:
        return -1
    
    sees = 0
    while h > window:
        sees +=1
        h *= bounce
        if h > window:
            sees +=1
    return sees

print(bouncingBall2(3, 0.6, 0.5))

#%%
import string

def is_pangram(st):
    letters = set(string.ascii_lowercase)
    st = st.lower()
    for char in st:
        if char in letters:
            letters.remove(char)
        if not letters:  
            return True
    return False

print(is_pangram("The quick brown fox jumps over the lazy dog"))
#%%
import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())

#%%


def tribonacci(sign,n=0):
    if n == 0:
        return [0]
    if n < 3:
        return sign[:n]

    ts = sign[:]
    for i in range(3,n):
        next_v = ts[-1]+ts[-2]+ts[-3]
        ts.append(next_v)
    return ts

print(tribonacci([1, 1, 1],10)) # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print(tribonacci([0, 0, 1], 10)) # [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
print(tribonacci([0, 1, 1], 10)) # [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
print(tribonacci([1, 0, 0], 10)) # [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]
print(tribonacci([0, 0, 0], 10)) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(tribonacci([1, 2, 3], 10)) # [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]
print(tribonacci([3, 2, 1], 10)) # [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]
print(tribonacci([1, 1, 1], 1)) # [1]
print(tribonacci([300, 200, 100])) # 0

#%% make a tower

def build_pyramid(floors):
    pyramid = []
    for i in range(1, floors + 1):
        spaces = ' ' * (floors - i)
        stars = '*' * (2 * i - 1)
        pyramid.append(spaces + stars + spaces)
    return pyramid


print(build_pyramid(3))
print(build_pyramid(6))

#%% make a tower

def tower_builder(n):
    return [("*" * (2*i-1)).center(n*2-1) for i in range(1, n+1)]

print(tower_builder(3))
print(tower_builder(6))


#%%
import math
def square(n):
    if n < 0 :
        return False
    nn = math.isqrt(n)
    return (nn*nn)==n

print(square(2))


#%% kelimeleri birlestir


def deneme(kelimeler):
    return " ".join(kelimeler)

print(deneme(["naber","müdür"]))

#%% kelimeleri birlestir

kelimeler = " ".join
print(kelimeler(["naber", "müdür"]))

#%%

def is_valid_walk(walk):

    if len(walk) != 10:
        return False
    
    vertical = 0
    horizontal = 0
    for direction in walk:
        if direction == 'n':
            vertical += 1
        elif direction == 's':
            vertical -= 1
        elif direction == 'e':
            horizontal += 1
        elif direction == 'w':
            horizontal -= 1
            
    return vertical == 0 and horizontal == 0

# Tes
print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))  
print(is_valid_walk(['w']))





































