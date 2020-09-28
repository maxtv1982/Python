from Stack_file import Stack

if __name__ == '__main__':
    braces = input('введите данные: ')
    err = 0
    my_stack = Stack()
    in_brace = "<({["
    out_brace = ">)}]"
    for brace in braces:
        if brace in in_brace:
            my_stack.push(brace)
        elif brace in out_brace:
            if my_stack.isEmpty():
                err += 1
            else:
                stack_last = my_stack.pop()
                # проверка на соответсвие открывающей и закрывающей скобок
                brace_first = in_brace[out_brace.index(brace)]
                if stack_last != brace_first:
                    err += 1
        else:
            err += 1

    if err == 0:
        print('Сбалансированно')
    else:
        print('Небалансированно')

