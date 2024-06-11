from tkinter import *
from tkinter import messagebox, filedialog
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

#Encoding
encoding_geral = os.device_encoding(1)

#Retirada do IP
ipv4 = subprocess.run('ipconfig | findstr IPv4', capture_output=True, text=True, shell=True, encoding=encoding_geral)
ipv4 = ipv4.stdout
ipv4_clean = re.findall(r'\d+\.\d+\.\d+\.\d+', ipv4)

#Levantamento de Data e Hora
current_datetime = datetime.datetime.now()
current_date = current_datetime.date()
current_time = current_datetime.time()
f_data = current_date.strftime("%d-%m-%Y")
f_time = current_time.strftime("%H:%M:%S")



#Output dos Pings
pingations = []


try:
    resume_wlan = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], encoding=encoding_geral, capture_output=True, text=True)
    output_wlan = resume_wlan.stdout
except UnicodeEncodeError:
    resume_wlan = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], encoding="uft-8", capture_output=True, text=True)
    output_wlan = resume_wlan.stdout


def all_pings():
    messagebox.showwarning("Atenção", "Aguarde o programa responder, caso seja necessário.\nA janela para salvar o relatório será aberta ao final dos testes!\nEsta janela de aviso pode ser fechada.")
    try:
        dft_g = subprocess.check_output("ipconfig | findstr \"Default Gateway\"", shell=True, encoding=encoding_geral)
        default_gateway = re.findall(r'\d+\.\d+\.\d+\.\d+', dft_g)
        gateway_ping = subprocess.run(["ping", "-n", "20", f"{default_gateway[0]}"], capture_output=True, text=True, encoding=encoding_geral)
        gateway_ping = gateway_ping.stdout
        pingations.append(f"\n{gateway_ping}\n")
    except UnicodeEncodeError:
        dft_g = subprocess.check_output("ipconfig | findstr \"Default Gateway\"", shell=True, encoding="utf-8")
        default_gateway = re.findall(r'\d+\.\d+\.\d+\.\d+', dft_g)
        gateway_ping = subprocess.run(["ping", "-n", "20", f"{default_gateway[0]}"], capture_output=True, text=True, encoding="utf-8")
        gateway_ping = gateway_ping.stdout
        pingations.append(f"\n{gateway_ping}\n")


    try:
        pingar = subprocess.run(["ping", "-n", "20", f"{default_gateway[0]}"], capture_output=True, text=True, encoding=encoding_geral)
        pingar = pingar.stdout
    except UnicodeEncodeError:
        pingar = subprocess.run(["ping", "-n", "20", f"{default_gateway[0]}"], capture_output=True, text=True, encoding="utf-8")
        pingar = pingar.stdout


    #Sites a serem pingados
    top5_pings = ['8.8.8.8', '1.1.1.1', 'uol.com.br', 'zoom.us', 'microsoft.com']


    for ping in top5_pings:
        pingados = subprocess.run(["ping", "-n", "20", f"{ping}"], capture_output=True, text=True, encoding=encoding_geral)
        pingados = pingados.stdout
        pingations.append(f"\n{pingados}\n")

    
    caminho =  filedialog.askdirectory(title="Escolha Onde Deseja Salvar o Relatório:")
    if caminho:
        file_path = os.path.join(caminho, f"Relatorio({usertag})_NetworkChecker.txt")
    try:
        with open(file_path, "w", encoding="utf-8") as relat:
            relat.write(f"""Usuario: {usertag}\nHostname: {hostname}\nIP de Origem:\n{ipv4}\nCPU %: {cpu}\nMemoria %: {memoria_p}\nData do Teste: {f_data}\nHora do Teste: {f_time}\n\nInfo de WLAN:\n{output_wlan}\nPing para o Default Gateway:\n{pingations[0]}\n\nPing para os 5 Sites:\n\n{pingations[1]}\n\n{pingations[2]}\n\n{pingations[3]}\n\n{pingations[4]}\n\n{pingations[5]}\n\n""")
    except UnicodeEncodeError:
        with open(file_path, "w", encoding=encoding_geral) as relat:
            relat.write(f"""Usuario: {usertag}\nHostname: {hostname}\nIP de Origem:\n{ipv4}\nCPU %: {cpu}\nMemoria %: {memoria_p}\nData do Teste: {f_data}\nHora do Teste: {f_time}\n\nInfo de WLAN:\n{output_wlan}\nPing para o Default Gateway:\n{pingations[0]}\n\nPing para os 5 Sites:\n\n{pingations[1]}\n\n{pingations[2]}\n\n{pingations[3]}\n\n{pingations[4]}\n\n{pingations[5]}\n\n""")


    



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

IP_l = Label(tela_um, text="IPv4", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
IP_l.place(x=10, y=122)
IPv4 = Label(tela_um, text="", width=15)
IPv4.place(x=10, y=148)

memoria_l = Label(tela_um, text="Memória %", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
memoria_l.place(x=10, y=176)
memoria_label = Label(tela_um, width=15)
memoria_label.place(x=10, y=204)

cpu_l = Label(tela_um, text="CPU %", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
cpu_l.place(x=10, y=232)
cpu_label = Label(tela_um, width=15)
cpu_label.place(x=10, y=260)

datestamp_l = Label(tela_um, text="Data", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
datestamp_l.place(x=10, y=288)
dtlabel = Label(tela_um, width=15)
dtlabel.place(x=10, y=316)

timestamp_l = Label(tela_um, text="Hora", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
timestamp_l.place(x=10, y=344)
tslabel = Label(tela_um, width=15)
tslabel.place(x=10, y=372)


net_label = Label(text="Informações de Rede", justify="center", bg=VERDE, fg="white", font=("Consolas", 15))
net_label.place(x=318, y=10)
net_interfaces = Text(tela_um, width=50, height=25)
net_interfaces.place(x=225, y=38)



def diagnosticar():
    usuario_label = Label(tela_um, text=usertag, width=15)
    usuario_label.place(x=10, y=38)

    hostname_label = Label(tela_um, text=hostname, width=15)
    hostname_label.place(x=10, y=94)

    IPv4 = Label(tela_um, text=ipv4_clean[0], width=15)
    IPv4.place(x=10, y=148)

    memoria_label = Label(tela_um, text=memoria_p, width=15)
    memoria_label.place(x=10, y=204)

    cpu_label = Label(tela_um, text=cpu, width=15)
    cpu_label.place(x=10, y=260)

    dtlabel = Label(tela_um, text=f_data, width=15)
    dtlabel.place(x=10, y=316)

    tslabel = Label(tela_um, text=f_time, width=15)
    tslabel.place(x=10, y=372)

    net_interfaces.place(x=220, y=38)
    net_interfaces.insert(END, output_wlan)
    messagebox.showwarning("Atenção", "Após diagnosticar, clique em 'Gerar Relatório'\nOs testes demoram cerca de 2:15 minutos para serem finalizados.\nApós o término, salve o arquivo e direcione ao seu TI para avaliação.\nUma janela será aberta para salvamento do arquivo txt.\nApós salvar o arquivo, o Network Checker pode ser encerrado!\nApós leitura, essa janela de aviso pode ser fechada.")



diagnose_button = Button(tela_um, bg=AZUL, fg="#ffffff", text="DIAGNOSTICAR", width=15, highlightthickness=0, font=("Consolas", 10), command=diagnosticar)
diagnose_button.place(x=268, y=460)

gerar_relatorio = Button(tela_um, bg=AZUL, fg="#ffffff", text="GERAR RELATÓRIO", width=15, highlightthickness=0, font=("Consolas", "10"), command=all_pings)
gerar_relatorio.place(x=268, y=500)


screen.mainloop()


