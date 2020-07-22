class Stack:
    def __init__(self,size=5):
        self.data = []
        self.size = size


    def push(self,data):
        if len(self.data) == self.size: #Full
            return
        self.data.append(data)


    def pop(self):
        if len(self.data) == 0:  #Empty
            return
        return self.data.pop()

    def clear(self):
        self.data =[]

    def __str__(self):  #print() 호출시에 발생되는 함수
        return f"<Stack size: {self.size} data={self.data}"

def main():


    stack =Stack()
    stack.push(4)
    stack.push(2)
    stack.push(5)
    print(stack)  # 스택의 힙주소가 출력된다.
    #print 시에 __str__() 가 호출된다

    print(stack.pop())
    stack.clear()
    print(stack.pop())



main()