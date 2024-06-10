from tkinter import *
from tkinter import messagebox
import datetime
import os
import psutil
import re
import socket
import subprocess


#Cores do Programa
VERDE = "#47B448"
AZUL = "#04528a"

#USO DA CPU
cpu = psutil.cpu_percent(interval=1)

#USO DA MEMÓRIA
memoria = psutil.virtual_memory()
memoria_p = memoria.percent

#Nome do Usuária
usertag = str(os.getlogin())

#Hostname da Máquina
hostname = socket.gethostname()
hostname = hostname.strip()

#Levantamento de Data e Hora
current_datetime = datetime.datetime.now()
current_date = current_datetime.date()
current_time = current_datetime.time()
f_data = current_date.strftime("%d-%m-%Y")
f_time = current_time.strftime("%H:%M:%S")


#Output dos Pings
pingations = []


try:
    resume_wlan = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], encoding="latin-1", capture_output=True, text=True)
    output_wlan = resume_wlan.stdout
except UnicodeEncodeError:
    resume_wlan = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], encoding="uft-8", capture_output=True, text=True)
    output_wlan = resume_wlan.stdout


def all_pings():
    try:
        dft_g = subprocess.check_output("ipconfig | findstr \"Default Gateway\"", shell=True, encoding="latin-1")
        default_gateway = re.findall(r'\d+\.\d+\.\d+\.\d+', dft_g)
        gateway_ping = subprocess.run(["ping", "-n", "30", f"{default_gateway[0]}"], capture_output=True, text=True, encoding="latin-1")
        gateway_ping = gateway_ping.stdout
        pingations.append(f"\n{gateway_ping}\n")
    except UnicodeEncodeError:
        dft_g = subprocess.check_output("ipconfig | findstr \"Default Gateway\"", shell=True, encoding="utf-8")
        default_gateway = re.findall(r'\d+\.\d+\.\d+\.\d+', dft_g)
        gateway_ping = subprocess.run(["ping", "-n", "30", f"{default_gateway[0]}"], capture_output=True, text=True, encoding="utf-8")
        gateway_ping = gateway_ping.stdout
        pingations.append(f"\n{gateway_ping}\n")


    try:
        pingar = subprocess.run(["ping", "-n", "30", f"{default_gateway[0]}"], capture_output=True, text=True, encoding="latin-1")
        pingar = pingar.stdout
    except UnicodeEncodeError:
        pingar = subprocess.run(["ping", "-n", "30", f"{default_gateway[0]}"], capture_output=True, text=True, encoding="utf-8")
        pingar = pingar.stdout


    #Sites a serem pingados
    top5_pings = ['8.8.8.8', 'uol.com.br', 'aws.com', 'zoom.us', "microsoft.com"]


    for ping in top5_pings:
        pingados = subprocess.run(["ping", "-n", "30", f"{ping}"], capture_output=True, text=True, encoding="latin-1")
        pingados = pingados.stdout
        pingations.append(f"\n{pingados}\n")

    
    try:
        with open(f"Relatorio({usertag})_Networkchecker.txt", "a", encoding="latin-1") as relat:
            relat.write(f"""Usuario: {usertag}\nHostname: {hostname}\nCPU %: {cpu}\nMemoria %: {memoria_p}\nData do Teste: {f_data}\nHora do Teste: {f_time}\n\nInfo de WLAN:\n{output_wlan}\nPing para o Default Gateway:\n{pingations[0]}\n\nPing para os 5 sites:\n\n{pingations[1]}\n\n{pingations[2]}\n\n{pingations[3]}\n\n{pingations[4]}\n\n{pingations[5]}\n\n""")
    except UnicodeEncodeError:
        with open(f"Relatorio({usertag})_Networkchecker.txt", "a", encoding="utf-8") as relat:
            relat.write(f"""Usuario: {usertag}\nHostname: {hostname}\nCPU %: {cpu}\nMemoria %: {memoria_p}\nData do Teste: {f_data}\nHora do Teste: {f_time}\n\nInfo de WLAN:\n{output_wlan}\nPing para o Default Gateway:\n{pingations[0]}\n\nPing para os 5 sites:\n\n{pingations[1]}\n\n{pingations[2]}\n\n{pingations[3]}\n\n{pingations[4]}\n\n{pingations[5]}\n\n""")



#Tela - GUI
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

datestamp_l = Label(tela_um, text="Data", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
datestamp_l.place(x=10, y=232)
dtlabel = Label(tela_um, width=15)
dtlabel.place(x=10, y=260)

timestamp_l = Label(tela_um, text="Hora", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
timestamp_l.place(x=10, y=288)
tslabel = Label(tela_um, width=15)
tslabel.place(x=10, y=316)

progresso_l = Label(tela_um, text="Progresso", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
progresso_l.place(x=10, y=344)
progresso = Label(tela_um, text="0%", width=15)
progresso.place(x=10, y=372)


net_label = Label(text="Informações de Rede", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
net_label.place(x=318, y=10)
net_interfaces = Text(tela_um, width=50, height=25)
net_interfaces.place(x=225, y=38)



def diagnosticar():
    usuario_label = Label(tela_um, text=usertag, width=15)
    usuario_label.place(x=10, y=38)

    hostname_label = Label(tela_um, text=hostname, width=15)
    hostname_label.place(x=10, y=94)

    memoria_label = Label(tela_um, text=memoria_p, width=15)
    memoria_label.place(x=10, y=148)

    cpu_label = Label(tela_um, text=cpu, width=15)
    cpu_label.place(x=10, y=204)

    dtlabel = Label(tela_um, text=f_data, width=15)
    dtlabel.place(x=10, y=260)

    tslabel = Label(tela_um, text=f_time, width=15)
    tslabel.place(x=10, y=316)

    net_interfaces.place(x=220, y=38)
    net_interfaces.insert(END, output_wlan)
    messagebox.showerror("Atenção", "Os testes demoram cerca de 3:30 minutos para serem finalizados.\nApós o término, salve o arquivo e direcione ao seu TI para avaliação.\nUma janela será aberta para salvamento do arquivo txt.\nEssa janela pode ser fechada, aguarde o encerramento dos testes!")

    progresso = Label(tela_um, text="20%", width=15)
    progresso.place(x=10, y=372)



diagnose_button = Button(tela_um, bg=AZUL, fg="#ffffff", text="DIAGNOSTICAR", width=15, font=("Consolas", 10), command=diagnosticar)
diagnose_button.place(x=280, y=500)


screen.mainloop()


