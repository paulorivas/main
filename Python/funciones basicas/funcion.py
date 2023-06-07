#funcion sin retorno, sin parametro
def hola():
    print('Hola mundo')
hola()
hola()
hola()
hola()
hola()
hola()
hola()
hola()

#funcion sin retorno y con parametros
def sumar(num1, num2):
    total = num1 + num2
    print(total)
sumar(2,2)

#funcion con retorno y parametro
def retorno(num1, num2):
    total = num1 + num2
    return total
resultado = retorno(2,3)
print(resultado)


#funcion sin parametros y con retorno
def func():
    return 'Hola mundo'
string = func()
print(string)
