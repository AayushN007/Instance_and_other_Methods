
class demo:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def instance_disp(self):
        print(self.a)
        x = 100
        y = 2
        print(x * y)
        
    def static_disp():
        print("Pyhon")
        
    def class_disp():
        print("Pytohon")
        
dl = demo()
dl.instance_disp()
demo.static_disp()
demo.class_disp()