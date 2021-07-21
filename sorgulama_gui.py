from tkinter import *
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
from threading import Thread
from time import sleep


def scanner():

    if var.get():
        if var.get() == 1:

            domain = e1.get()
            url1 = 'https://who.is/whois/{}'.format(domain)

            def whois():

                istek = requests.get(url1)
                sleep(3)
                soup = BeautifulSoup(istek.content,'lxml')
                bilgi = soup.find_all('div',attrs={'class':'col-md-12 queryResponseBodyValue'})

                for bilgiler in bilgi:

                    veri = bilgiler.text
                    veriler = veri
                    metin = '{}'.format(veriler)
                    terminal.tag_configure('style',foreground='green',font=('Verdana',10,'bold'))

                    terminal.insert(END,metin,'style')

            t1 = Thread(target=whois)
            t1.start()

        elif var.get() == 2:

            domain = e1.get()
            url1 = 'https://who.is/dns/{}'.format(domain)

            def dns():

                istek = requests.get(url1)
                sleep(3)
                soup = BeautifulSoup(istek.content,'lxml')
                bilgi = soup.find_all('div',attrs={'class':'col-md-12 queryResponseBodyKey'})

                for bilgiler in bilgi:

                    veri = bilgiler.text
                    veriler = veri
                    metin = '{}'.format(veriler)
                    terminal.tag_configure('style',foreground='green',font=('Verdana',10,'bold'))

                    terminal.insert(END,metin,'style')

            t2 = Thread(target=dns)
            t2.start()


        elif var.get() == 3:

            domain = e1.get()
            url1 = 'https://check-host.net/ip-info?host={}'.format(domain)

            def ip_scan():

                istek = requests.get(url1)
                sleep(3)
                soup = BeautifulSoup(istek.content,'lxml')
                bilgi = soup.find_all('div',attrs={'class':'ipinfo-item'})

                for bilgiler in bilgi:

                    veri = bilgiler.text
                    veriler = veri
                    metin = '{}'.format(veriler)
                    terminal.tag_configure('style',foreground='green',font=('Verdana',10,'bold'))

                    terminal.insert(END,metin,'style')

            t3 = Thread(target=ip_scan)
            t3.start()

  
  




master = Tk()
master.geometry('500x400+200+200')
master.title('DomainScan')

#------------------------------#
#------------------------------#
frame1 = Frame(master,bg='#bdb76b')
frame1.place(relx=0,rely=0,relwidth=1.0,relheight=0.1)
Label(frame1,text='DomainScanner',bg='#bdb76b',fg='white',font='Arial 12 bold').pack(padx=5,pady=10,anchor=S)
#-------------------------------#
#-------------------------------#
frame2 = Frame(master,bg='#bdb76b')
frame2.place(relx=0,rely=0.1,relwidth=1.0,relheight=0.2)
Label(frame2,text='DOMAİN GİRİNİZ: ',bg='#bdb76b',fg='white',font='Arial 12 bold').pack(padx=5,pady=10,side=LEFT)
e1 = Entry(frame2,bd=4,relief=FLAT)
e1.pack(padx=5,pady=10,side=LEFT)
btn = Button(frame2,text='SCANNER START',bg='green',fg='white',font='Arial 10 bold',command=scanner)
btn.pack(padx=25,pady=10,side=LEFT)

#-------------------------#
#-------------------------#
frame3 = Frame(master,bg='#bdb76b')
frame3.place(relx=0,rely=0.3,relwidth=0.4,relheight=0.7)

var = IntVar()

r1 = Radiobutton(frame3,text='WHOİS SCANNER',bg='#bdb76b',fg='black',font='Arial 12 bold',value=1,variable=var)
r1.pack(padx=5,pady=10,anchor=NW)

r2 = Radiobutton(frame3,text='DNS SCANNER',bg='#bdb76b',fg='black',font='Arial 12 bold',value=2,variable=var)
r2.pack(padx=5,pady=10,anchor=NW)

r3 = Radiobutton(frame3,text='IP SCANNER',bg='#bdb76b',fg='black',font='Arial 12 bold',value=3,variable=var)
r3.pack(padx=5,pady=10,anchor=NW)

Label(frame3,text='Youtube OlcaySoftware',bg='#bdb76b',fg='#333',font='Arial 10 bold').pack(padx=5,pady=30,anchor=NW)

#------------------------#
#------------------------#
frame4 = Frame(master,bg='#bdb76b')
frame4.place(relx=0.4,rely=0.3,relwidth=0.6,relheight=0.7)

Label(frame4,text='CONTENT TERMİNAL',bg='#bdb76b',fg='white',font='Arial 12 bold').pack(pady=10,anchor=S)
terminal = Text(frame4,height=14,width=30,bg='black')
terminal.tag_configure('style',foreground='#bfbfbf',font=('Verdana',8,'bold'))
terminal.pack()

metin = '[ROOT💀ROOT]>>>'
terminal.insert(END,metin,'style')




master.mainloop()

