import tkinter as tk
from tkinter import scrolledtext
from scapy.all import ARP, Ether, send, srp
import uuid

Mac_Atacante= ''.join(['{:02x}'.format((uuid.getnode()>>i)& 0xff) for i in range(0,8*6,8)][::-1])
print(Mac_Atacante)

ataque_encurso=False