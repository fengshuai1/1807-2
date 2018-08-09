import time
'''
烤地瓜
面向对象的思想
让地瓜自己烤
'''

class SweetTuDou():

    def __init__(self):#初始化属性
        self.status = "生的"#烤的状态
        self.time = 0#烤的时间
        self.list = []#装作料的东西
 
    def cook(self):#烹饪
        self.time+=1
        if self.time < 3:
            self.status = "生的"
        elif self.time >= 3 and self.time < 10:
            self.status = "半生不熟"
        elif self.time >= 10 and self.time <15:
            self.status = "熟了"
        elif self.time>15:
            self.status = "糊了"

    def tellStatus(self):#告诉状态
        print(self.status)
        print("作料有%s"%str(self.list))
        #for i in self.list:
        #    print() 

    def addZuoLiao(self,s):#加作料
        self.list.append(s)

digua = SweetTuDou()
for i in range(15):
    digua.cook()
    if i == 1:
        digua.addZuoLiao("盐")
    elif i == 3:
        digua.addZuoLiao("糖")
    elif i == 5:
        digua.addZuoLiao("麻油")
    digua.tellStatus()
    time.sleep(1)
