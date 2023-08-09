##################示例一##############################################
# import datetime
# import random
# import time

# odds = [1,3,5,7,9,11,
#     13,15,17,19,21,23,25,27,
#     29,31,33,35,37,39,41,43,
#     45,47,49,51,53,55,57,59,]
# for i in range(5):
#     righttime = datetime.datetime.today().minute
#     if righttime in odds:
#         print("this minute seem in adds")
#     else:
#         print("minute not in odds")
#     if i < 4:
#         time.sleep(random.randint(1, 10))

####################示例二################################################
# vowels=['a','e','i','o','u']
# found=[]
# word=input('input:')
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# for i in found:
#     print(i)


#####################示例三###########################################3
# phrase="Don't panic!"
# plist=list(phrase)
# print(phrase)
# print(plist)
# for i in range(4):
#     plist.pop()
# plist.pop(0)###on't pa
# plist.remove("'")##ont pa
# plist.extend([plist.pop(),plist.pop()])##ont ap
# plist.insert(2,plist.pop(3))
# print(plist)

# newphrase="".join(plist)
# print(newphrase)

######################示例四###################################
# phrase="Don't panic!"
# plist=list(phrase)
# print(phrase)
# print(plist)
# newphrase=''.join(plist[1:3])
# newphrase=newphrase+''.join([plist[5],plist[4],plist[7],plist[6]])
# print(newphrase)

#########################示例五##################################
# str='abcdefg'
# lists=list(str)
# print(lists[-1:-2:-1])
# for char in lists:
#     print('\t',char)
# for char in lists:
#     print('\t'*2,char)

#######################示例六####################################
# person={'name':'ford prefect',
#         'gender':'male',
#         'occupation':'researcher',
#         'home plant':'betelgeuse seven'}
# print(person)
# person['age']=33
# print(person)

#######################示例七#####################################
# vowels=['a','e','i','o','u']
# found={}
# word=input('input:')
# for letter in word:
#     if letter in vowels:
#         if letter in found:
#             found[letter]+=1
#         else:
#             found[letter]=1
# for k,v in sorted(found.items()):
#     print(k,'was found',v,'time(s)')
#######################示例八###################################
# vowels=['a','e','i','o','u']
# found={}
# word=input('input:')
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found[letter]=0
#           #存在直接跳过判断执行加1，不存在就初始化，要把它初始化为0而不是1
#         found[letter]+=1
# for k,v in sorted(found.items()):
#     print(k,'was found',v,'time(s)')

###########################示例九##############################
# vowels=['a','e','i','o','u']
# found={}
# word=input('input:')
# for letter in word:
#     if letter in vowels:
#         found.setdefault(letter,0)
#         #字典.setdefault(键，初始值)  初始化如果有需要相当于上面的if判断加初始化
#         found[letter]+=1
# for k,v in sorted(found.items()):
#     print(k,'was found',v,'time(s)')

##########################示例十#################################
# vowels=set('aaeiiou')   #向set()传递一个序列可以自动生成集合
# found=vowels.intersection(set(input('input:'))) #interable意思是可迭代，数组、字符串、列表都是可迭代的
# for vowel in found:
#     print(vowel)

###########################示例十一##############################
# import pprint
# people={}
# people['ford']={'name':'fordprefect',
#                 'gender':'male',
#                 'occupation':'researcher',
#                 'homeplanet':'betelgeuseseven'}
# people['arthur']={'name':'arthurdent',
#                   'gender':'male',
#                   'occupation':'sandwich-maker',
#                   'homeplanet':'earth',
# }
# people['trillian']={'name':'tricamcmillan',
#                      'gender':'female',
#                      'occupation':'mathematician',
#                      'homeplanet':'earth'}
# people['robot']={'name':'marvin',
#                  'gender':'unknown',
#                  'occupation':'paranoidandroid',
#                  'homeplanet':'unknown'}
# pprint.pprint(people)
# #####嵌套字典采用二维数组定位方法，people[行][列]来唯一确定某一数据


##########################示例十二################################
# def search4vowels(word):
#   """Return a boolean based on any vowels found."""
#   vowels=set('aaeiiou')   #向set()传递一个序列可以自动生成集合
#   found=vowels.intersection(set(word))
#   return bool(found)

########################示例十三###########################33
# def search4vowels(word:str) -> set:
#   """Return any vowels found in a supplied word."""
#   vowels=set('aaeiiou')   #向set()传递一个序列可以自动生成集合
#   return vowels.intersection(set(word))


###########################示例十四#########################
# def search4letters(phrase:str,letters:str) -> set:
#   """Return any letters found in a supplied phrase."""
#   letter=set(letters)   #向set()传递一个序列可以自动生成集合
#   return letter.intersection(set(phrase))

##########################示例十五############################
# from flask import Flask
# from vsearch import search4letters
# app=Flask(__name__)

# @app.route('/')
# def hello() -> str:
#     return 'Hello world from Flask'
# #我自己根据要求编写的，代码有一些错误
# # @app.route('/search4')
# # def do_search(phrase:str,letters:str) ->str :
# #     return str(search4letters(phrase,letters))
# #..........................................................................
# @app.route('/search4')
# def do_search() -> str:
#     return str(search4letters('life, the universe, and everything','eiru'))
# app.run()

##################################################################################
# from flask import escape
# contents1=[]
# with open ('log.txt') as log:
#     for line in log:
#         linelist=escape(line.split('|'))
#         contents1.append(linelist)
# print(str(contents1))
# print('..........................................................')
# #..................................................................
# contents2=[]
# with open ('log.txt') as log:
#     for line in log:
#         contents2.append([])
#         for item in line.split('|'):
#             contents2[-1].append(escape(item))
# print(str(contents2))
# #这两个输出结果是一样的,至少列表层数是一样的

###############################示例十六###################################
# import mariadb
# dbconfig = {'host':'127.0.0.1',
#             'user':'vsearch',
#             'password':'vsearchpasswd',
#             'database':'vsearchlogDB'}
# conn = mariadb.connect(**dbconfig)
# cursor = conn.cursor()
# # _sql = """describe log"""
# _sql = """insert into log (phrase,letters,ip,browser_string,results)
#        values (%s,%s,%s,%s,%s)"""
# cursor.execute(_sql,('hitch-hiker','xyz','127.0.0.1','safari','set()'))
# conn.commit()
# _sql="""select * from log"""
# cursor.execute(_sql)
# for row in cursor.fetchall():
#     print(row)
# cursor.close
# conn.close
# 运行结果
# (1, datetime.datetime(2023, 5, 19, 21, 27, 26), 'hitch-hiker', 'xyz', '127.0.0.1', 'safari', 'set()')
# 因为cursor.fetchall返回的各行是一个元组，而元组是不可变的列表，因此可以使用中括号计数法，
# 比日row[2]就会挑出phrase,roe[3]就会挑出letters


##################################示例十七########################################
# 创建类
# class CountFromBy:
#     def __init__(self, v: int=0, i: int=1) -> None:
#         self.val = v
#         self.inc = i

#     def increase(self) -> None:
#         self.val += self.inc

#     def __repr__(self) -> str:
#         return str(self.val)


# a = CountFromBy(v=0, i=0)
# b = CountFromBy(v=1, i=1)
# a.increase()
# 当访问属性a.val和a.inc德时候他能正确输出，但是当访问a这个对象时会输出一个难懂的信息
# <__main__.CountFromBy object at 0x7f037b541a30>
# 这代表对象a的类型和id值的十六进制表示
######################################示例十八#################################
# from flask import Flask,session

# app=Flask(__name__)

# app.secret_key='YouWillNeverGuess'

# @app.route('/setuser/<user>')
# def setuser(user: str) -> str :
#     session['user']=user  #这个看起来每一个都是以‘user’作为健，实际是以每一个cookue作为健，session库内部作了替换
#     return 'User value set to:'+ session['user']

# @app.route('/getuser')
# def getuser() ->str :
#     return 'User value is currently set to:' +session['user']

# if __name__=='__main__':
#     app.run(debug=True)
##############################################示例十九####################################
# from flask import Flask,session
# from checker import check_log_in

# app=Flask(__name__)
# app.secret_key='YouWillNeverGuess'

# @app.route('/')
# def hello() -> str:
#     return 'hello from the simple webapp'

# @app.route('/login')
# def login() -> str :
#     session['logged_in']=True
#     return 'You are logged in'

# @app.route('/logout')
# def logout() -> str:
#     session.pop('logged_in')
#     return 'you are logged out'
# #注销时可以将log_in健对应的值设置为False，也可以删除这个键值对，而删除是个好办法

# # @app.route('/status')
# # def check_status() ->str :
# #     if 'logged_in' in session:
# #         return 'You are currently logged in'
# #     else:
# #         return 'you are NOT logged in'
        
# @app.route('/page1')
# @check_log_in
# def page1() ->str :
#     return 'this is page1'

# @app.route('/page2')
# @check_log_in
# def page2() ->str :
#     return 'this is page2'

# @app.route('/page3')
# @check_log_in
# def page3() ->str :
#     return 'this is page3'

# if __name__=='__main__':
#     app.run(debug=True)
####################################示例二十################################################
# def outer(func):
#     def inner(*args,**kwargs):
#         print('this is inner')
#         return func(*args,**kwargs)
#     print('this is outer,invoking inner')
#     return inner
# def func(a):
#     a=a+1
#     return a
# print(outer(func)(1))
# #####################################示例二十一#############################################
# stu = {
#     'name': '小王',
#     'age': 14,
#     'gender': '男',
#    }
# for k,v in stu.items():
#     print(k,v,sep='->',end='<-')
# print()
# print(stu.items()))a


# import sys
# try:
#     1/0
# except:
#     err=sys.exc_info()
#     print(err)

##########################连接数据库error####################################
import mariadb

class ConnErr(Exception):
    pass
dbconfig = {'host':'127.0.0.1',
            'user':'vsearch',
            'password':'vsearchpasswd',
            'database':'vsearchlogDB'}
try:
    conn = mariadb.connect(**dbconfig)

    cursor = conn.cursor()
# _sql = """describe log"""
    _sql = """insert into log (phrase,letters,ip,browser_string,results)
       values (%s,%s,%s,%s,%s)"""
    cursor.execute(_sql,('hitch-hiker','xyz','127.0.0.1','safari','set()'))
    conn.commit()
    _sql="""select * from log"""
    cursor.execute(_sql)
    for row in cursor.fetchall():
        print(row)
    cursor.close
    conn.close
except mariadb.OperationalError as err:
    print('???',str(err))
    # raise ConnErr(err)