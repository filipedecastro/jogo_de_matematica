import customtkinter as ctk
import random

#varíaveis iniciais
points = 0

#funções
def facil():
    #função para a dificuldade de jogo "fácil"
    global points

    def getvalue():
        global points
        nonlocal number1, number2, result

        #pegando o valor do lentry
        try:
            value = int(lentry.get())
            print(value)
        except ValueError:
            laviso.pack()
            return "entrada inválida"

        #eventos para certo e errado
        if value == result:
            points += 1
            print("acerto")

            number1 = random.randint(1, 10)
            number2 = random.randint(1, 10)
            result = number1 * number2

            pointsl.configure(text=f"Sua pontuação atual é: {points}")
            llabel.configure(text=f"Próxima questão: {number1} multiplicado por {number2} = ")
            laviso.pack_forget()
            lentry.delete(0, "end")
        else:
            print("erro")
            print(result)

            lentry.destroy()
            lbutton.destroy()

            llabel.configure(text="Poxa, errou... mas você pode recomeçar!")
            pointsl.configure(text=f"Sua pontuação final foi: {points}")     
            laviso.pack_forget()
            points = 0
    
    #nova janela    
    new_window = ctk.CTkToplevel(app)
    new_window.title("modo de jogo: fácil")
    new_window.geometry("400x300")
    
    #varíaveis da função
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    result = number1 * number2
    print(result)

    #estrutura da new_window
    pointsl = ctk.CTkLabel(new_window, text=f"Sua pontuação atual é: {points}")
    llabel = ctk.CTkLabel(new_window, text=f"{number1} multiplicado por {number2} = ")
    lentry = ctk.CTkEntry(new_window)
    lbutton = ctk.CTkButton(new_window, text="Enviar Resposta", command=getvalue)
    laviso = ctk.CTkLabel(new_window, text="digite somente um valor numérico")
    
    pointsl.pack(pady=10)
    llabel.pack(pady=10)
    lentry.pack(pady=10)
    lbutton.pack(pady=10)

def medio():
    #função para a dificuldade de jogo "médio"
    global points

    def getvalue():
        global points
        nonlocal number1, number2, number3, result

        #pegando o valor do lentry
        try:
            value = int(lentry.get())
            print(value)
        except ValueError:
            laviso.pack()
            return "entrada inválida"

        #eventos para certo e errado
        if value == result:
            points += 1
            print("acerto")

            number1 = random.randint(1, 10)
            number2 = random.randint(1, 10)
            number3 = random.randint(1, 10)
            result = number1 * number2 * number3

            pointsl.configure(text=f"Sua pontuação atual é: {points}")
            llabel.configure(text=f"Próxima questão: {number1} multiplicado por {number2} multiplicado por {number3} = ")
            laviso.pack_forget()
            lentry.delete(0, "end")
        else:
            print("erro")
            print(result)

            lentry.destroy()
            lbutton.destroy()

            llabel.configure(text="Poxa, errou... mas você pode recomeçar!")
            pointsl.configure(text=f"Sua pontuação final foi: {points}")     
            laviso.pack_forget()
            points = 0

    #nova janela
    new_window2 = ctk.CTkToplevel(app)
    new_window2.title("Modo de Jogo: Médio")
    new_window2.geometry("400x300")
   
    #varíaveis da função
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    number3 = random.randint(1 ,10)
    result = number1 * number2 * number3

    #estrutura da nova janela
    pointsl = ctk.CTkLabel(new_window2, text=f"Sua pontuação atual é {points}")
    llabel = ctk.CTkLabel(new_window2, text=f"{number1} multiplicado por {number2} multiplicado por {number3} = ")
    lentry = ctk.CTkEntry(new_window2)
    lbutton = ctk.CTkButton(new_window2, text="enviar resposta", command=getvalue)
    laviso = ctk.CTkLabel(new_window2, text="digite somente um valor numérico.")

    pointsl.pack(pady=10)
    llabel.pack(pady=10)
    lentry.pack(pady=10)
    lbutton.pack(pady=10)

def dificil():
    #função para a dificuldade de jogo "difícil"
    global points

    def get_value():
      global points
      nonlocal raiz, radiente, multiplicacao, soma, expoente, resultado
      
      #pegando o valor do lentry
      try:
          value = int(lentry.get())
          print(value)
      except ValueError:
          laviso.pack()
          return "entrada inválida"
      
      #eventos para certo ou errado
      if value == resultado:
            points += 1
            print("acerto")

            raiz = random.randint(2, 12)
            radiente = raiz * raiz
            multiplicacao = random.randint(4, 15)
            soma = random.randint(13, 23)
            expoente = random.randint(2, 3)
            resultado = raiz*multiplicacao+soma**expoente

            pointsl.configure(text=f"Sua pontuação atual é: {points}")
            llabel.configure(text=f"raiz quadrada de {radiente} multiplicado por {multiplicacao} somado por {soma} elevado a {expoente}")
            lexpression.configure(text=f"√{radiente}.{multiplicacao}+{soma}^{expoente} = ")
            laviso.pack_forget()
            lentry.delete(0, "end")
      else:
            print("erro")
            print(resultado)

            lentry.destroy()
            lbutton.destroy()
            lexpression.destroy()

            llabel.configure(text="Poxa, errou... mas você pode recomeçar!")
            pointsl.configure(text=f"Sua pontuação final foi: {points}")     
            laviso.pack_forget()
            points = 0

    
    #criando nova janela
    new_window3 = ctk.CTkToplevel(app)
    new_window3.title("Modo de jogo: Difícil")
    new_window3.geometry("400x300")

    #varíaveis da função
    raiz = random.randint(2, 12)
    radiente = raiz * raiz
    multiplicacao = random.randint(4, 15)
    soma = random.randint(13, 23)
    expoente = random.randint(2, 3)
    resultado = raiz*multiplicacao+soma**expoente

    #estrutura da nova janela
    pointsl = ctk.CTkLabel(new_window3, text=f"Sua pontuação atual é {points}")
    llabel = ctk.CTkLabel(new_window3, text=f"raiz quadrada de {radiente} multiplicado por {multiplicacao} somado por {soma} elevado a {expoente}")
    lexpression = ctk.CTkLabel(new_window3, text=f"√{radiente}.{multiplicacao}+{soma}^{expoente} = ")
    lentry = ctk.CTkEntry(new_window3)
    lbutton = ctk.CTkButton(new_window3, text="enviar resposta", command=get_value)
    laviso = ctk.CTkLabel(new_window3, text="digite somente um valor numérico.")

    pointsl.pack(pady=10)
    llabel.pack(pady=10)
    lexpression.pack(pady=10)
    lentry.pack(pady=10)
    lbutton.pack(pady=10)
    print(resultado)




#definindo a janela principal
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Jogo de matematica")
app.geometry("550x300")

#estrutura da janela principal
label = ctk.CTkLabel(app, text="Seja bem vindo ao jogo de matemática")
label.pack(pady=10)
label2 = ctk.CTkLabel(app, text="selecione uma dificuldade dentre as listadas abaixo (essa será a dificuldade dos cálculos):")
label2.pack()

button_easy = ctk.CTkButton(app, text="Fácil", command=facil)
button_easy.pack(pady=10)
button_med = ctk.CTkButton(app, text="Médio", command=medio)
button_med.pack(pady=10)
button_hard = ctk.CTkButton(app, text="Difícil", command=dificil)
button_hard.pack(pady = 10)

app.mainloop()