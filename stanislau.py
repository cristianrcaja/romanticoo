import tkinter as tk
import time
import os

class Mensagemozaopaula:
    def __init__(self, root):
        self.root = root
        self.root.title("Mensagem Pru meu amo")
        self.root.configure(bg='#ffe6e6')
        
        self.canvas = tk.Canvas(self.root, width=600, height=500, bg='#ffe6e6', highlightthickness=0)
        self.canvas.pack()
        
        self.text_frame = tk.Frame(self.canvas, bg='#ffe6e6')
        self.text_frame.pack()

        self.intro_text = tk.Label(self.text_frame, text="Gathusca,", font=('Cursive', 24), bg='#ffe6e6', fg='#ff0000')
        self.intro_text.pack()

        self.message_text = tk.Label(self.text_frame, text="", font=('Cursive', 16), bg='#ffe6e6', fg='#ff0000', wraplength=500)
        self.message_text.pack()

        self.name_text = tk.Label(self.text_frame, text="", font=('Cursive', 24, 'bold'), bg='#ffe6e6', fg='#ff0000')
        self.name_text.pack()

        self.final_text = tk.Label(self.text_frame, text="", font=('Cursive', 16), bg='#ffe6e6', fg='#ff0000', wraplength=500)
        self.final_text.pack()
        
        self.message = "Meu amor, quero dizer que sou muito grato por te ter comigo e que uce é a melhor coisa que podia ter me acontecido. Você sempre será minha ❤️❤️❤️❤️❤️❤️❤️❤️"
        self.name = "Paumonha"
        self.final_message = "Uce é a razão do meu sorriso e a dona do meu coração. ❤️\n\nPara sempre seu,\nNamoraduu"

        self.hearts_positions = [(50, 50), (550, 50), (50, 450), (550, 450), (300, 50), (300, 450), (50, 250), (550, 250)]
        self.hearts = []
        
        self.mostrar_mensagem()

    def criarcoracao(self, position):
        heart = self.canvas.create_text(position[0], position[1], text="❤️", font=('Helvetica', 30), fill='#ff0000')
        self.hearts.append(heart)

    def coracoesanimados(self):
        delay = 1000
        for i, pos in enumerate(self.hearts_positions):
            self.root.after(delay * (i + 1), lambda p=pos: self.criarcoracao(p))
    
    def digitando_texto(self, text, text_widget, delay=100):
        for i in range(len(text) + 1):
            snippet = text[:i]
            text_widget.config(text=snippet)
            self.root.update()
            time.sleep(delay / 1000)

    def mostrar_mensagem(self):
        self.digitando_texto(self.message, self.message_text, 50)
        time.sleep(1)
        self.digitando_texto(self.name, self.name_text, 700)
        time.sleep(1)
        self.digitando_texto(self.final_message, self.final_text, 50)
        self.coracoesanimados()
        self.display_images() 

    def display_images(self):
        relative_path1 = "amor1.png"
        relative_path2 = "amor2.png"

        absolute_path1 = os.path.abspath(relative_path1)
        absolute_path2 = os.path.abspath(relative_path2)
        
        self.image1 = tk.PhotoImage(file=absolute_path1).subsample(2, 2)  
        self.image2 = tk.PhotoImage(file=absolute_path2).subsample(2, 2)  
        
        frame1 = tk.Frame(self.canvas, width=150, height=150, bg='#ffe6e6', highlightthickness=0)
        frame1.pack(pady=20, side=tk.LEFT)
        label1 = tk.Label(frame1, image=self.image1, bg='#ffe6e6')
        label1.pack()

        frame2 = tk.Frame(self.canvas, width=150, height=150, bg='#ffe6e6', highlightthickness=0)
        frame2.pack(pady=20, side=tk.LEFT)
        label2 = tk.Label(frame2, image=self.image2, bg='#ffe6e6')
        label2.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Mensagemozaopaula(root)
    root.mainloop()
