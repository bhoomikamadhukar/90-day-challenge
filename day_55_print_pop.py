  N = int(input())
    array = []
    for i in range(N) :
        inputs = input().split()
        if len(inputs) == 3 :
            array.insert(int(inputs[1]),int(inputs[2]))
        elif len(inputs) == 2 :
            if inputs[0] == "append" :
                array.append(int(inputs[1]))
            else :
                array.remove(int(inputs[1]))
        else :
            if inputs[0] == "print" :
                print(array)
            elif inputs[0] == "sort" :
                array.sort()
            elif inputs[0] == "pop" :
                array.pop()
            else :
                array.reverse()