import math
class Add(Exception):
    def add(a,b):
        def init(self,*args: object):
         super().init(*args)
        try:
            if a == None or b == None:
                raise Add('insufficient arguments')
            print(a + b)
        except Add as a:
           print(a.args[0])

class Sub(Exception):
    def sub(a,b):
        def init(self,*args: object):
         super().init(*args)
        try:
            if a == None or b == None:
                pass 
            elif a == None and b == None:
                raise Sub('insufficient arguments')
            print(a - b)
        except Sub as b:
           print(b.args[0])
