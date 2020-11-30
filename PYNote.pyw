import tkinter as tk
#import tkinter.ttk as tk
from tkinter.scrolledtext import *
from tkinter.filedialog import *

fulltexthelp="""
Thank you for using PYNote Version 1.

There's one menu on the application's top, with intuitive names.

At the starting, the application open one new file, you can start instantly writing something!
Normally, saving and writing operations work perfectly, but it needs in some cases Admin rights.
(I've just tested on Windows PCs)

This application was created with the goal to create Lite and Nice Python apps, and of course for improving my programming skills.
You can check my github to get source code.
Else, if you're a genius or one hacker, just use Notepad ;)
Check paul-thorel.github.io for full documentation and my other projects!

All rights Reserved Paul Thorel© Alias CaptainLuigi 2020 """

class main(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		self.file=None
		self.version="1.0 Alpha"
		self.grid_columnconfigure(0,weight=1,pad=0)
		self.grid_rowconfigure(0,weight=1,pad=0)

		self.create_widgets()


	def helpdisplay(self):
		help=helpwindow()
		help.mainloop()

	def newfile(self):
		self.file=None
		self.inittext()
		self.configtitle()

	def openfile(self):

		data=askopenfilename(title="Select your file")

		if data:
			self.inittext()
			content=open(data)
			self.file=data
			self.configtitle(data)
			self.texteditor.insert("end",content.read())
			self.texteditor.edit_reset()
			content.close()

	def savefile(self):

		if not self.file:
			data=asksaveasfilename(title="Select your file")
			print("saving")
			self.file=data

		if self.file:
			data=self.file
			content=open(data,"w")
			content.write(self.texteditor.get(0.0,"end"))
			content.close()

		self.configtitle(data)

	def inittext(self):
		self.texteditor.delete(0.0,"end")
		self.texteditor.edit_reset()


	def configtitle(self,data="New File"):
		self.title("PYNote : "+data)




	def create_widgets(self):
		self.texteditor=ScrolledText(self,undo=True)
		self.filemenu=tk.Menu(self,tearoff=0)
		self.editmenu=tk.Menu(self,tearoff=0)
		self.helpmenu=tk.Menu(self,tearoff=0)
		self.mainmenu=tk.Menu(self)
		self.filemenu.add_command(label="New ",command=lambda :self.newfile())
		self.filemenu.add_command(label="Open",command=lambda :self.openfile())
		self.filemenu.add_command(label="Save",command=lambda :self.savefile())

		self.editmenu.add_command(label="Undo",command=lambda :self.texteditor.edit_undo())
		self.editmenu.add_command(label="Redo",command=lambda :self.texteditor.edit_redo())
		self.editmenu.add_command(label="Delete History",command=lambda :self.texteditor.edit_reset())

		self.helpmenu.add_command(label="About and Help",command=lambda :self.helpdisplay())



		self.mainmenu.add_cascade(menu=self.filemenu,label="File")
		self.mainmenu.add_cascade(menu=self.editmenu,label="Edit")
		self.mainmenu.add_cascade(menu=self.helpmenu,label="Help")
		self.texteditor.grid(row=0,column=0,sticky="NSEW")
		self.config(menu=self.mainmenu)




class helpwindow(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		self.title("PYNote Help")
		self.resizable(0,0)
		self.create_widgets()

	def create_widgets(self):
		self.textlabel=tk.Label(self,text=fulltexthelp,font=("system",10))
		self.closebutton=tk.Button(self,text="Close this help window",command=self.destroy)
		self.textlabel.pack()
		self.closebutton.pack(expand=1,fill="y")


root=main()
root.title('PYNote : New File')
root.mainloop()