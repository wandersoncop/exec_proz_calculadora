num1 = float (input("Digite o primeiro numero: "))
num2 = float (input("Digite o segundo numero: "))
operacao = input("Operacao a realizar ? (+ , -, *, /)")
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2  
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    print ("Operação Invalida")  
    resultado = 0             
    print(resultado)    
