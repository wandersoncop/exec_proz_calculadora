
continuar_usando = "SIM"

while continuar_usando == "SIM":
  
  print("SELECIONE A OPERAÇÃO DESEJADA")
  print("1: Soma")
  print("2: Subtração")
  print("3: Multiplicação")
  print("4: Divisão")

  
  operacao = (input("\nQual operação você deseja realizar? "))

  
  if operacao == "1":
    num1 = float(input("\nDigite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    adicao = num1 + num2
    print(adicao)
    print("*"*33,"\n")
    
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

  #Subtração
  if operacao == "2":
    b1 = float(input("\nDigite o primeiro valor: "))
    b2 = float(input("Digite o segundo valor: "))
    subtracao = b1 - b2
    print("\nA subtração entre",b1,"e",b2,"é:",subtracao,"\n")
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

  #Multiplicação
  if operacao == "3":
    c1 = float(input("\nDigite o primeiro valor: "))
    c2 = float(input("Digite o segundo valor: "))
    multiplicacao = c1 * c2
    print("\nA multiplicação entre",c1,"e",c2,"é:",multiplicacao,"\n")
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

  #Divisão
  if operacao == "4":
    d1 = float(input("\nDigite o primeiro valor: "))
    d2 = float(input("Digite o segundo valor: "))
    while d2 == 0:                  #Garantindo que d2 não seja zero!!
      print("O segundo valor não pode ser zero!")
      d2 = float(input("\nDigite o segundo valor (diferente de zero): "))
    divisao = d1 / d2
    print("\nA divisão entre",d1,"e",d2,"é:",divisao,"\n")
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")