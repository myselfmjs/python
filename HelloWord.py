#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math

def foo():
    '这是函数说明'
    str="function"
    print(str);

def foo1(num):
    print('num' ,num);

def foo2(name ,age):
    print('name' ,name);
    print('age' ,age);

def init(data):
    data['frist'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data,label,name):
    return data[label].get(name)

def score(data,full_name):
    names = full_name.split()
    if len(names) == 2:names.insert(1,'')
    labels = 'frist','middle','last'
    for label,name in zip(labels,names):
        people = lookup(data,label,name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


def print_param(*param):
    print(param)

def add(x,y):
    return x+y

def factorial(n):
    '递归-阶乘'
    if n ==1:
        return  1
    else:
        return n * factorial(n-1)

def search(sequence,number,lower=0,upper=None):
    if upper is None: upper = len(sequence)-1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper)/2
        if number > sequence[middle]:
            return search(sequence,number,middle+1,upper)
        else:
            return search(sequence,number,lower,upper)


'''
定义对象
'''
class Peson:
    def setName(self,name):
        self.name = name
    def getName(self,name):
        return self.name
    def greet(self):
        print("Hello, World! I'm %s." %self.name)


class Filter:
    def init(self):
        self.bloked = []
    def filter(self,sequence):
        return [x for x in sequence if x not in self.bloked]

class SPAMFilter(Filter):
    def init(self):
        self.bloked = ['SPAM']


class Fibs:
     def __init__(self):
         self.a = 0
         self.b = 1
     def __next__(self):
         self.a, self.b = self.b, self.a + self.b
         return self.a
     def __iter__(self):
         return self





if __name__=="__main__":

    lis = {1,2,3,4,5}
    tup = tuple(lis)
    print(lis)
    print(tup)


    '''
    fibs = Fibs()
    for f in fibs:
        if f > 1000:
            print(f)
            break
    '''


    # raise Exception('错误信息')

    '''
    f = Filter()
    f.init()
    t = f.filter([1,2,3])
    print(t)

    s = SPAMFilter()
    s.init()
    v = s.filter(['SPAN','SPAM','AAAA','BBBB','SPAM','SPAN'])
    print(v)

    print(SPAMFilter.__bases__)
    '''

    '''
    bar = Peson()
    bar .setName("BBBB")
    bar.greet()
    '''

    '''
    print_param('a','b','c')
    '''
    '''
    me = 'Magnus Lie Hetland'
    you = 'Magnus Lie AAA'
    her = 'AAA BBB AAA'
    storage = {}
    init(storage)
    score(storage,me)
    score(storage,you)
    score(storage,her)
    print(lookup(storage,'last','AAA'))
    '''

   # storage['middle']['Lie'] = me
   # middle = lookup(storage,'middle','Lie')
   # print(middle)

    '''
    print("main")
    foo2('yuhui' ,30)
    foo1(6)
    foo()
    '''

    '''
    name = input("What your name?")
    if name.endswith("a"):
        print("Hello a")
    else:
        print("Who are you?")
    
    '''

    '''
    print(3 if 2>0 else 2)
    '''

    '''
    name = ''
    while not name:
        name = input("Please enter your name:")
        print('Hello. %s!' % name)
    '''
    '''
    for number in range(101):
        print(number)
    '''

    '''
    strings = ['a','b','a','b','a','b','a','b','a','b','a','b']
    strings[2] = 'c'
    print(strings)
    for index,string in enumerate(strings):
        if 'b' in string:
            print(index , '-----' ,strings[index])
            strings[index] = 'c'

    print(strings)
    '''
    '''
   fibs = [0,1]
   for i in range(8):
       fibs.append(fibs[-2] + fibs[-1])

   print(fibs)
   '''

    '''
    print(foo.__doc__)
    '''




