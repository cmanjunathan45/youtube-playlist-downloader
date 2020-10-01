from tkinter import *
from tkinter import messagebox,filedialog
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from pytube import *
import pafy 
import webbrowser
import requests

root=tk.Tk()
root.title("Youtube PlayList Downloader | Manjunathan C")
root.geometry("1100x600")
root.iconphoto(True,tk.PhotoImage(file="icon.png"))
root.config(bg="#181818")
label1=Label(root,text="Youtube PlayList Video Downloader",bg="#181818",fg="#E94B3C",font=("font awesome",15,"bold italic"))
label1.place(x=350,y=10)

label2=Label(root,text="Paste Your PlayList URL here ",bg="#181818",fg="#E94B3C",font=("font awesome",10,"bold italic"))
label2.place(x=150,y=80)

entry=Entry(root,font=("fontawesome",12,"bold italic"),bg="#E94B3C",fg="#181818",width=35,borderwidth=5)
entry.place(x=55,y=120)

def play():
	try:
		tex.delete("1.0",END)
		playlist = pafy.get_playlist(entry.get()) 
		items = playlist["items"] 
		path=filedialog.askdirectory()
		for i in range (0,9999999999999999999999999):
			try:
				item = items[i] 
				i_pafy = item['pafy'] 
				y_url = i_pafy.watchv_url 
				tex.insert(tk.END,y_url+"\n")	 
				
				yt=YouTube(y_url)
				y = yt.streams.get_highest_resolution()
				y.download(path)
				
			except:
				messagebox.showinfo("Finished",f"All {i} Videos in the Play list Are Downloaded")
				break
	except:
		messagebox.showerror("Failed","URL Error or Network Error")	
def save():
	root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
	if root.filename is None:
		return
	file_save =  str(tex.get(1.0,END))
	root.filename.write(file_save)
	root.filename.close()
def clear():
	entry.delete(0,END)
	tex.delete("1.0",END)
buttonVideo=Button(root,font=("fontawesome",12,"bold italic"),text="Download",bg="#E94B3C",fg="#181818",borderwidth=5,width=10,activebackground="#2D2926",command=play)
buttonVideo.place(x=180,y=170)

buttonClear=Button(root,text="Clear",font=("fontawesome",12,"bold italic"),bg="#E94B3C",fg="#181818",borderwidth=5,width=10,activebackground="#2D2926",command=clear)
buttonClear.place(x=180,y=230)

buttonExit=Button(root,text="Exit",font=("fontawesome",12,"bold italic"),bg="#E94B3C",fg="#181818",borderwidth=5,width=10,activebackground="#2D2926",command=root.quit)
buttonExit.place(x=180,y=290)

buttonContact=Button(root,text="Contact",font=("fontawesome",12,"bold italic"),bg="#E94B3C",fg="#181818",borderwidth=5,width=10,activebackground="#2D2926",command=lambda: webbrowser.open("https://github.com/cmanjunathan45/"))
buttonContact.place(x=180,y=350)

buttonYoutube=Button(root,text="Single Video Downloader",font=("fontawesome",12,"bold italic"),bg="#E94B3C",fg="#181818",borderwidth=5,width=20,activebackground="#2D2926",command=lambda: webbrowser.open("https://github.com/cmanjunathan45/Youtube-downloader"))
buttonYoutube.place(x=120,y=425)

tex=Text(root,font=("fontawesome",12,"bold italic"),bg="#E94B3C",fg="#181818",height=19,width=45,borderwidth=10)
tex.place(x=500,y=120)

buttonSave=Button(root,text="Save Links For Future Use",font=("fontawesome",12,"bold italic"),bg="#E94B3C",fg="#181818",borderwidth=5,width=25,activebackground="#2D2926",command=save)
buttonSave.place(x=610,y=500)

root.mainloop()
