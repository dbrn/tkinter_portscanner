import tkinter as tk
import tkinter.scrolledtext as scrtxt
from tkinter import END
import socket

# Function that scans the server, it takes a range as an input
def scan(hostname, ports, output):
    ports_array = list(map(lambda x: int(x), str(ports.get()).split("-")))
    if len(ports_array) == 1:
        ports_array.append(ports_array[0])
    output.insert(END, "Port-scan on  " + hostname.get() + " ports: "
                  + str(ports_array[0]) + "-" + str(ports_array[1]))
    for i in range(ports_array[0], ports_array[1] + 1):
        timeout_flag = False
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(0.5)
        try:
            conn.connect((str(hostname.get()), i))
        except socket.timeout:
            timeout_flag = True
        conn.close()
        if timeout_flag is False:
            output.insert(END, "\nport " + str(i) + " OPEN")

def clear_text(entry1_, entry2_, text_):
    entry1_.delete(0, END)
    entry2_.delete(0, END)
    text_.delete(1.0, END)


# GUI 
root = tk.Tk()
root.title("Tcl/Tk Python port-scanner")
root.resizable(False, False)
panel = tk.PanedWindow(height=300, width= 300,)
panel.pack(padx=6, pady=6)
label1 = tk.Label(panel, text="Hostname: ")
label2 = tk.Label(panel, text="Ports range: ")
entry1 = tk.Entry(panel, width=15, bd=1)
entry2 = tk.Entry(panel, width=15, bd=1)
button1 = tk.Button(panel, text="Scan", width=5, command=lambda: scan(entry1, entry2, text1))
button2 = tk.Button(panel, text="Clear", width=5, command=lambda: clear_text(entry1, entry2, text1))
text1 = scrtxt.ScrolledText(panel, width=34, height=12, wrap="word")
label1.place(x=0, y=3)
label2.place(x=0, y=43)
entry1.place(y=3, x=90)
entry2.place(y=43, x=90)
button1.place(y=0, x=230)
button2.place(y=40, x=230)
text1.place(y=80, x=2)
root.mainloop()
