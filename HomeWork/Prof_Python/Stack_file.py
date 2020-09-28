class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        # проверка стека на пустоту
        return len(self.stack) == 0

    def push(self, element):
        # добавляет новый элемент на вершину стека
        self.stack.append(element)

    def pop(self):
        # удаляет верхний элемент стека
        return self.stack.pop()


    def peek(self):
        # возвращает верхний элемент стека, но не удаляет его
        return self.stack[len(self.stack)-1]

    def size(self):
        # возвращает количество элементов в стеке
        return len(self.stack)

# my_stack = Stack()
# my_stack.push(876)
# my_stack.push(8)
#
# print(my_stack.__dict__)
# print(my_stack.isEmpty())
# print(my_stack.peek())
# print(my_stack.size())

