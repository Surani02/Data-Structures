

class Stack:
    arr_1 = []
    n = 0;
    top=-1;
    def __init__(self,n:int):
        self.n = n
    def push(self,value:int):
        if(self.top>self.n):
            return 
        self.top+=1
        self.arr_1.append(value)
    def pop(self):
        if(len(self.arr_1)==0):
            return 
        val = self.arr_1.pop()
        self.top-=1
        return val
    def get_size(self):
        return len(self.arr_1)
    def is_empty(self):
        return len(self.arr_1)==0
    def peek(self):
        if len(self.arr_1)==0:
            return 
        return self.arr_1[self.top]
    def get_elements(self):
         if len(self.arr_1)==0:
             print("No elements found.")
         else:
            for i in self.arr_1[::-1]:
                print(i)

if (__name__=="__main__"):
    stack_inst = Stack(10)
    print("Before inserting any elements : ")
    stack_inst.get_elements()
    print("Adding 10 as a value")
    stack_inst.push(10)
    print("Adding 20 as a value")
    stack_inst.push(20)
    print("Adding 30 as a value")
    stack_inst.push(30)
    print("After inserting the elements in the stack :")
    stack_inst.get_elements()
    print(f"Popping {stack_inst.pop()} from the stack")
    print(f"Popping {stack_inst.pop()} from the stack")
    print(f"Popping {stack_inst.pop()} from the stack")
    print("The stack after popping all the elements")
    stack_inst.get_elements()
    print("Adding 10 as a value")
    stack_inst.push(10)
    print("Displaying the number of elements in a stack : ",stack_inst.get_size())
    print("Displaying the top element in the stack :  ",stack_inst.peek())
    print("Checking if the stack is empty : ",stack_inst.is_empty())            
