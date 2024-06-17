from tkinter import *
from tkinter import messagebox, filedialog
import datetime
import os
import psutil
import re
import socket
import subprocess
import sys
import time
import webbrowser



print("DO NOT CLOSE THIS WINDOW!\n\nThe tests are running in the background processes.\nAfter saving the report file, the program can be terminated!")

#Cores do Programa
PURPLE = "#ad83be"
BLACK = "#080808"

#USO DA CPU
cpu = psutil.cpu_percent(interval=1)

#USO DA MEMÓRIA
memoria = psutil.virtual_memory()
memoria_p = memoria.percent

#Nome do Usuário
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
    resume_wlan = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], encoding="utf-8", capture_output=True, text=True)
    output_wlan = resume_wlan.stdout


base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
icone = os.path.join(base_path, 'images', 'network.ico')


screen = Tk()
screen.title("Last Dreamer - Network Checker")
screen.geometry("700x600")
screen.config(padx=20, pady=20, bg=BLACK)
screen.resizable(False, False)
screen.iconbitmap(icone)

tela_um = Frame(bg=PURPLE)
tela_um.pack(fill="both", expand=True)

User = Label(tela_um, text="User", justify="center", bg=PURPLE, fg="white", font=("Consolas", 15))
User.place(x=10, y=10)
User_label = Label(tela_um, width=15)
User_label.place(x=10, y=38)

hostname_l = Label(tela_um, text="Hostname", justify="center", bg=PURPLE, fg="white", font=("Consolas", 15))
hostname_l.place(x=10, y=66)
hostname_label = Label(tela_um, width=15)
hostname_label.place(x=10, y=94)

IP_l = Label(tela_um, text="IPv4", justify="center", bg=PURPLE, fg="white", font=("Consolas", 15))
IP_l.place(x=10, y=122)
IPv4 = Label(tela_um, text="", width=15)
IPv4.place(x=10, y=148)

memoria_l = Label(tela_um, text="Memory %", justify="center", bg=PURPLE, fg="white", font=("Consolas", 15))
memoria_l.place(x=10, y=176)
memoria_label = Label(tela_um, width=15)
memoria_label.place(x=10, y=204)

cpu_l = Label(tela_um, text="CPU %", justify="center", bg=PURPLE, fg="white", font=("Consolas", 15))
cpu_l.place(x=10, y=232)
cpu_label = Label(tela_um, width=15)
cpu_label.place(x=10, y=260)

datestamp_l = Label(tela_um, text="Date", justify="center", bg=PURPLE, fg="white", font=("Consolas", 15))
datestamp_l.place(x=10, y=288)
dtlabel = Label(tela_um, width=15)
dtlabel.place(x=10, y=316)

timestamp_l = Label(tela_um, text="Time", justify="center", bg=PURPLE, fg="white", font=("Consolas", 15))
timestamp_l.place(x=10, y=344)
tslabel = Label(tela_um, width=15)
tslabel.place(x=10, y=372)


net_label = Label(text="Network Information", justify="center", bg=PURPLE, fg="white", font=("Consolas", 15))
net_label.place(x=318, y=10)
net_interfaces = Text(tela_um, width=50, height=25)
net_interfaces.place(x=225, y=38)



def diagnosticar():
    User_label.config(text=usertag)
    hostname_label.config(text=hostname)
    IPv4.config(text=ipv4_clean[0])
    memoria_label.config(text=memoria_p)
    cpu_label.config(text=cpu)
    dtlabel.config(text=f_data)
    tslabel.config(text=f_time)

    net_interfaces.place(x=220, y=38)
    net_interfaces.delete(1.0, END)
    net_interfaces.insert(END, output_wlan)

    messagebox.showwarning("WARNING!: - After reading, this box can be closed!", """1 - Keep the Network Checker and CMD (Black Screen) open during the test.\n2- In case of program not responding, wait until it does.\n3- The tests last for about 2:35 minutes to be completed.\n4- After completion , a window will pop up to save the report.\n5- Don't rename the file.\n6- Send the file to your network analyst for evaluation.\n7- After all of the previous steps, the program can be terminated.\n""")

    
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


    time.sleep(1)
    while True:

        caminho =  filedialog.askdirectory(title="Where Do You Want to Save the Report?")
        if caminho:
            file_path = os.path.join(caminho, f"Report({usertag})_NetworkChecker.txt")
            try:
                with open(file_path, "w", encoding="utf-8") as relat:
                    relat.write(f"""User: {usertag}\nHostname: {hostname}\nSource IP:\n{ipv4}\nCPU %: {cpu}\nMemory %: {memoria_p}\nDate of the Test: {f_data}\nTime of the Test: {f_time}\n\nWlan INFO:\n{output_wlan}\nPing to Default Gateway:\n{pingations[0]}\n\nPing to 5 Sites:\n\n{pingations[1]}\n\n{pingations[2]}\n\n{pingations[3]}\n\n{pingations[4]}\n\n{pingations[5]}\n\n""")
                    break
            except UnicodeEncodeError:
                with open(file_path, "w", encoding=encoding_geral) as relat:
                    relat.write(f"""User: {usertag}\nHostname: {hostname}\nSource IP:\n{ipv4}\nCPU %: {cpu}\nMemory %: {memoria_p}\nDate of the Test: {f_data}\nTime of the Test: {f_time}\n\nWlan INFO:\n{output_wlan}\nPing to Default Gateway:\n{pingations[0]}\n\nPing to 5 Sites:\n\n{pingations[1]}\n\n{pingations[2]}\n\n{pingations[3]}\n\n{pingations[4]}\n\n{pingations[5]}\n\n""")
                    break

diagnose_button = Button(tela_um, bg=BLACK, fg="#ffffff", text="DIAGNOSE", width=15, highlightthickness=0, font=("Consolas", 10), command=diagnosticar) #all_pings()))
diagnose_button.place(x=268, y=470)



def lastdreamer():
    webbrowser.open("lastdreamer.com")


devop = Label(screen, height=1, bg=BLACK, fg="#ffffff", highlightthickness=0, text="DEVELOPED BY:", font=("Consolas", 8 ))
devop.place(x=482, y=563)


last_dreamer = Button(screen, relief=FLAT, height=1, command=lastdreamer, bg=BLACK, fg="#ffffff", highlightthickness=0, text="LASTDREAMER.COM", font=("Consolas", 8 ))
last_dreamer.place(x=565, y=562)


screen.mainloop()


