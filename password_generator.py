from tkinter import *
from tkinter import ttk
import random,string,pyperclip

special_characters=list(string.punctuation)
uppercase_letters=list(string.ascii_uppercase)
lowercase_letters=list(string.ascii_lowercase)
numbers=[0,1,2,3,4,5,6,7,8,9]
dicty={1:uppercase_letters,2:lowercase_letters,3:numbers}

class Password:
	def __init__(self,length):
		self.length=length
	def generate(self):
		my_password=""
		while len(my_password)<=self.length-1:
			my_password+=str(random.choice(dicty[random.randint(1,3)]))
		return my_password
class GUI:
	def __init__(self,master):
		self.master=master
		self.master.geometry("300x150")
		self.master.title("Password Generator")
		self.master.resizable(0,0)
	def start(self):
		self.pop_menu=Menu(tearoff=0)
		self.pop_menu.add_command(label="Copy",command=self.copy)
		self.frame1=Frame(self.master)
		self.frame1.grid(row=0,column=0,columnspan=2)	
		length_label=Label(self.frame1,text="Length of password:")
		length_label.grid(row=0,column=0,sticky="W")
		self.spin=Spinbox(self.frame1,width=15,from_=5,to=50)
		self.spin.set(10)
		self.spin.grid(row=0,column=1,sticky="W")
		self.main_entry=Entry(self.frame1,width=30,state="readonly")
		self.main_entry.grid(row=1,column=0,columnspan=2,pady=3)
		self.main_entry.bind("<Button-3>",self.pop_up)
		self.frame2=Frame(self.master)
		self.frame2.grid(row=2,column=0,columnspan=2)
		self.push_but=ttk.Button(self.frame2,text="Generate",command=self.go)
		self.push_but.grid(row=2,column=0,columnspan=2)
		self.master.bind("<Return>",self.go)
	def go(self,event=0):
		generated=Password(length=int(self.spin.get())).generate()
		self.main_entry["state"]="normal"
		self.main_entry.delete(0,END)
		self.main_entry.insert(0,str(generated))
		self.main_entry["state"]="readonly"
	def pop_up(self,event):
		try:
			self.pop_menu.tk_popup(event.x_root+37, event.y_root-15, 0)
		finally:
			self.pop_menu.grab_release()	
	def copy(self,event=0):
		pyperclip.copy(self.main_entry.get())			
class Spinbox(ttk.Entry):
	import tkinter as tk
	def __init__(self, master=None, **kw):
		ttk.Entry.__init__(self, master, "ttk::spinbox", **kw)
	def set(self, value):
		self.tk.call(self._w, "set", value)

if __name__=="__main__":
	root=Tk()
	interface=GUI(root).start()
	root.mainloop()
