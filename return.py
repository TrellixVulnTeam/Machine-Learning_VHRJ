def sum(num1, num2):
   return num1 + num2
print(sum(4,5))

#function do one thing really well. Should return something

def sum2(Num1, Num2):
    def another_func(Num1, Num2):
        return Num1 + Num2
    return another_func(Num1, Num2)

total = sum2(10,20)
print(total)

#a return automatically exits the function and will not het ot the next line.