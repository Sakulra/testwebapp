"""The UseDatabase context manager for working with MySQL/MariaDB.

Simple example usage:

    from DBcm import UseDatabase, SQLError

    config = { 'host': '127.0.0.1',
               'user': 'myUserid',
               'password': 'myPassword',
               'database': 'myDB' }

    with UseDatabase(config) as cursor:
        _SQL = "select * from log"
        cursor.execute(_SQL)
        data = cursor.fetchall()

Enjoy, and have fun.  (Sorry: Python 3 only, due to type hints and new syntax).
"""
import mariadb

class ConnErr(Exception):
    pass

class CredErr(Exception):
    pass

class UseDatabase:
    def __init__(self,config: dict) -> None:
        self.configuration=config   #相当于为对象定义了一个属性并赋值
    def __enter__(self) -> 'cursor':
        # self.conn = mariadb.connect(**self.configuration)
        # self.cursor = self.conn.cursor()
        # return self.cursor
#*********************************************************************
        try:
            self.conn = mariadb.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mariadb.OperationalError as err:
            raise ConnErr(err)#为什么还要加err？是因为自定义错误继承了Exception类，就可以在raise自定义错误时，
                              #将捕获的具体错误传递给自定义异常，这样就可以在其他捕获自定义异常的时候得到原始错误信息
        except mariadb.ProgrammingError as err:
            raise CredErr(err)
    def __exit__(self,exc_type,exc_value,exc_trace) -> None:
    #通过sys.exc_info我们知道它会得到一个包含三个对象的元组，即(类型，值，回溯跟踪对象)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
#如果__enter__出错了，那么__exit__就不会执行了，所以要在__enter__中定制异常处理，而不是__exit__。
