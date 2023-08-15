from flask import Flask,render_template,request,session
from vsearch import search4letters
# import mariadb
from DBcm import UseDatabase,ConnErr
from ua_parser import user_agent_parser
from checker import check_log_in
from threading import Thread

app=Flask(__name__)

app.config['dbconfig'] = {'host':'127.0.0.1',
        'user':'vsearch',
        'password':'vsearchpasswd',
        'database':'vsearchlogDB'}

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display webapp's form"""
    return render_template('entry.html',)


@app.route('/search4' ,methods=['POST'])  #methods=['GET','POST'],可以既支持get又支持post.
def do_search() -> 'html':
    """Extract thr posted data; perform the research; return the results"""
    letters=request.form['letters']  #request.form[]是一个字典，可以获取html表单中的数据，键就是html中的name属性
    phrase=request.form['phrase']   
    results = str(search4letters(phrase, letters))
    try:
        # log_request(request,results)
        l_r=Thread(target=log_request,args=(request,results))
        l_r.start()
    except Exception as err:
        print('logging failed with this error:',str(err))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)  #最后可以有这个逗号也可没有，render提供，template模板
#....................................................................................................................
# def log_request(req:'flask_request',res:str) -> None:
#     with open('log.txt','a') as log:
#         # # print(req,file=log)
#         # # print(res,file=log)
#         # # print(req,res,file=log)  #这三句是我自己看要求写的，但是错误了
#         # print(req.form,file=log,end='|')
#         # print(req.remote_addr,file=log,end='|')
#         # print(req.user_agent,file=log,end='|')
#         # print(res,file=log)
#         print(req.form,req.remote_addr,req.user_agent,res,file=log,sep='|')
#使用数据库替换成下面的代码

def log_request(req:'flask_request',res:str) -> None:
    """Log details of the web request and results"""
    with UseDatabase(app.config['dbconfig'] ) as cursor:
        _sql = """insert into log (phrase,letters,ip,browser_string,results) 
            values (%s,%s,%s,%s,%s)"""
        user_agent_browser=user_agent_parser.ParseUserAgent(req.user_agent.string)['family']
        cursor.execute(_sql,(req.form['phrase'],req.form['letters'],req.remote_addr,user_agent_browser,res))
#.................................................................................................................   
#我写的，这个是错误的，使用.split('|')后得到的是包含字符的列表，如果对整个列表使用escape(),那么整个列表就变成了字符
#而不是列表本身了，因为使用escape()后其内包含了一个markup()方法,他会将所有对象转化为字符
# @app.route('/viewlog')
# def viewlog() -> str:
#     contents=[]
#     with open ('log.txt') as log:
#         for line in log:
#             linelist=line.split('|')
#             contents.append(linelist)
#         print(str(contents))
#     return str(contents)

#书上的，这个是正确的
# @app.route('/viewlog')
# def viewlog() -> 'html':
#     """Display the contents of the log file as a html table"""
#     contents=[]
#     with open ('log.txt') as log:
#         for line in log:
#             contents.append([])
#             for item in line.split('|'):
#                 contents[-1].append(escape(item))
#         # print(str(contents))
#     with UseDatabase(dbconfig) as cursor:
#         _sql=
#         titles=['From Data','Remote_addr','User_agent','Results']
#     return render_template('viewlog.html',therowtitles=titles,thedata=contents)
#改为使用数据库
@app.route('/viewlog')
@check_log_in
def viewlog() -> 'html':
    """Display the contents of the log file as a html table"""
    try:
        with UseDatabase(app.config['dbconfig'] ) as cursor: #返回一个游标，那我该如何获取我想要的数据并传输到前端呢？
            _sql="""select phrase,letters,ip,browser_string,results from log"""
            cursor.execute(_sql)
            contents=cursor.fetchall()
            titles=['Phrase','Letters','Remote_addr','User_agent','Results']
        return render_template('viewlog.html',therowtitles=titles,thedata=contents)
    except ConnErr as err:
        print('your database have wrong with',str(err))
    except Exception as err:
        print('something went wrong.:',str(err))
    
    # with UseDatabase(app.config['dbconfig'] ) as cursor: #返回一个游标，那我该如何获取我想要的数据并传输到前端呢？
    #     _sql="""select phrase,letters,ip,browser_string,results from log"""
    #     cursor.execute(_sql)
    #     contents=cursor.fetchall()
    #     titles=['Phrase','Letters','Remote_addr','User_agent','Results']
    # return render_template('viewlog.html',therowtitles=titles,thedata=contents)
#...............................................................................................................
app.secret_key='YouWillNeverGuess'

@app.route('/login')
def login() -> str :
    session['logged_in']=True
    return 'You are logged in'

@app.route('/logout')
def logout() -> str:
    session.pop('logged_in')
    return 'you are logged out'
#注销时可以将log_in健对应的值设置为False，也可以删除这个键值对，而删除是个好办法

if __name__=='__main__':
    app.run(debug=True)
