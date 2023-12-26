
import time 

#__author: greg
#date: 2017/9/19 23:52
from multiprocessing import Process
import time
 

 

class myClass:
    def __init__(self, objName):
        self.objName = objName
        print("对象 '%s' 已经创建" % self.objName)
        self.p = Process(target=self.st)

    def pp(self):
        # self.p.daemon = True
        self.p.start()
    
    def terminal(self):
        self.p.terminate()

    def update(self,msg):
        self.objName=msg
        
    def st(self):
       while True:
            time.sleep(1)
            print(self.objName)

    def get(self):
        return self.objName

    def __del__(self):
        print("对象 '%s' 已经删除" % self.objName)

# myList=[]

# myObj2 = myClass('Obj2')
# myObj3 = myClass('Obj3')
# myList.append(myObj2)
# myList.append(myObj3)

# # myObj1.pp()
# myObj2.pp()
# myObj3.pp()
# print("s"*100)
# # myObj2.update("objx")
# # 从列表中删除对象
# time.sleep(5)
# print(myList)
# # myList.remove(myObj2)
# myList[1].terminal()
# del myObj2


# print(myObj2.get(),)
# 删除对象引用， Python会自动调用析构方法

def solve():
    
    res = []        
    for i in range(5):
        name = str(i)
        print(name)
        myobj =  myClass(name)
        myobj.pp()

        res.append({name:myobj})
        print(res)
        if len(res)>5:
            break
        time.sleep(5)
    print(res)
    # res[0].teminal()
p = Process(target=solve)
p.start()