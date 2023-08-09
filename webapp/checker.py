from flask import session
from functools import wraps

def check_log_in(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if 'logged_in' in session:
            return func(*args,**kwargs)
        else:
            return 'you are NOT logged in'
    return wrapper
#return 的wrapper函数因为在主程序中没有主动调用所以并不会被执行，那它是怎么判断的？？？就很迷
# @app.route('/page3')
# @check_log_in
# def page3() ->str :
#     return 'this is page3'

#类似于执行pag3(),实际执行check_log_in(page3())
#wrapper中的参数其实就是page3()里面的参数
#如果func真的有参数，它是怎么传递到wrapper中的？