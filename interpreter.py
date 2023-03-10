example = input ("Expression: ")
example = example.split()
x = float(example[0])
y = example[1]
z = float(example[2])
match y  :
    case  "-":
        print (x-z)
    case "+":
        print(x+z)
    case "*":
        print(x*z)
    case "/":
        print(x/z)
