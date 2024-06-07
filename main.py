from tkinter import *
import os
import psutil
import socket
import subprocess


VERDE = "#47B448"
AZUL = "#04528a"


cpu = psutil.cpu_percent(interval=1)
# print(cpu)
memoria = psutil.virtual_memory()
memoria_p = memoria.percent
# print(memoria.percent)
usertag = str(os.getlogin())
# print(usertag)
hostname = socket.gethostname()
hostname = hostname.strip()
# print(hostname)

resume_wlan = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], encoding="latin-1", capture_output=True, text=True)
output = resume_wlan.stdout


# try:
#     with open("teste.txt", "r", encoding='latin-1') as file:
#         resumo = file.read()
#         print(resumo)
# except UnicodeDecodeError:
#         with open("teste.txt", "r", encoding='utf-8') as file:
#             resumo = file.read()
#             print(resumo)


    



screen = Tk()
screen.title("Pinpoint - Network Checker")
screen.geometry("700x600")
screen.config(padx=20, pady=20, bg=AZUL)
screen.resizable(False, False)
screen.iconbitmap("logo.ico")


tela_um = Frame(bg=VERDE)
tela_um.pack(fill="both", expand=True)

usuario = Label(tela_um, text="Usuário", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
usuario.place(x=10, y=10)
usuario_label = Label(tela_um, width=15)
usuario_label.place(x=10, y=38)

hostname_l = Label(tela_um, text="Hostname", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
hostname_l.place(x=10, y=66)
hostname_label = Label(tela_um, width=15)
hostname_label.place(x=10, y=94)

memoria_l = Label(tela_um, text="Memória %", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
memoria_l.place(x=10, y=122)
memoria_label = Label(tela_um, width=15)
memoria_label.place(x=10, y=148)

cpu_l = Label(tela_um, text="CPU %", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
cpu_l.place(x=10, y=176)
cpu_label = Label(tela_um, width=15)
cpu_label.place(x=10, y=204)

timestamp_l = Label(tela_um, text="Timestamp", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
timestamp_l.place(x=10, y=232)
tslabel = Label(tela_um, width=15)
tslabel.place(x=10, y=260)

net_label = Label(text="Informações de Rede", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
net_label.place(x=318, y=10)
net_interfaces = Text(tela_um, width=50, height=25)
net_interfaces.place(x=225, y=38)



def diagnosticar():
    usuario = Label(tela_um, text="Usuário", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
    usuario.place(x=10, y=10)
    usuario_label = Label(tela_um, text=usertag, width=15)
    usuario_label.place(x=10, y=38)

    hostname_l = Label(tela_um, text="Hostname", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
    hostname_l.place(x=10, y=66)
    hostname_label = Label(tela_um, text=hostname, width=15)
    hostname_label.place(x=10, y=94)

    memoria_l = Label(tela_um, text="Memória %", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
    memoria_l.place(x=10, y=122)
    memoria_label = Label(tela_um, text=memoria_p, width=15)
    memoria_label.place(x=10, y=148)

    cpu_l = Label(tela_um, text="CPU %", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
    cpu_l.place(x=10, y=176)
    cpu_label = Label(tela_um, text=cpu, width=15)
    cpu_label.place(x=10, y=204)

    timestamp_l = Label(tela_um, text="Timestamp", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
    timestamp_l.place(x=10, y=232)
    tslabel = Label(tela_um, width=15)
    tslabel.place(x=10, y=260)

    net_interfaces = Text(tela_um, width=50, height=25)
    net_interfaces.place(x=220, y=38)
    net_interfaces.insert(END, output)


diagnose_button = Button(tela_um, bg=AZUL, fg="#ffffff", text="DIAGNOSTICAR", width=15, font=("Consolas", 10), command=diagnosticar)
diagnose_button.place(x=280, y=500)


screen.mainloop()



#ipconfig | findstr "IPv4 IPv6"