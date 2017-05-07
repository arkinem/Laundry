import tkinter as tk
from tkinter import messagebox
from functools import partial


class MainWindow():
	def __init__(self):
		try:
			with open('accounts.txt', "r") as file:
				pass
		except IOError as e:
			open('accounts.txt', "w")

		root = tk.Tk()
		# root.geometry("300x200")
		root.title("Login")
		self.center(root)
		root.geometry("275x90")

		self.LabelLogin = tk.Label(text="Login: ")
		self.LabelLogin.grid(row=0, column="0")

		self.EntryLogin = tk.Entry(width="30")
		self.EntryLogin.grid(row=0, column="1")

		self.LabelPassword = tk.Label(text="Password : ")
		self.LabelPassword.grid(row=1, column="0")

		self.EntryPassword = tk.Entry(width="30", show="*")
		self.EntryPassword.grid(row=1, column="1")

		self.ButtonLogin = tk.Button(root, text="Login", width=10, height=1, command=lambda: self.login(self.EntryLogin.get(),self.EntryPassword.get()))
		self.ButtonLogin.grid(row=2, column="1")

		self.ButtonRegister = tk.Button(root, text="Register", width=10, height=1, command=self.registerWindow)
		self.ButtonRegister.grid(row=2, column="0")

		root.bind('<Return>', self.func())

		root.mainloop()

	def func(event):
		print("You hit return.")

	def registerWindow(self):
		registerWindow = tk.Toplevel()
		registerWindow.title("Register")
		self.center(registerWindow)
		registerWindow.geometry("255x90")
		registerWindow.grab_set()

		self.LabelName = tk.Label(registerWindow, text="Name: ")
		self.LabelName.grid(row=0, column="0")

		self.EntryName = tk.Entry(registerWindow, width="30")
		self.EntryName.grid(row=0, column="1")

		self.LabelLogin = tk.Label(registerWindow, text="Login : ")
		self.LabelLogin.grid(row=1, column="0")

		self.EntryLogin = tk.Entry(registerWindow, width="30")
		self.EntryLogin.grid(row=1, column="1")

		self.LabelPassword = tk.Label(registerWindow, text="Password : ")
		self.LabelPassword.grid(row=2, column="0")

		self.EntryPassword = tk.Entry(registerWindow, width="30", show="*")
		self.EntryPassword.grid(row=2, column="1")

		self.ButtonRegister1 = tk.Button(registerWindow, text="Register", width=10, height=1, command=lambda: self.registerAccount(self.EntryName.get(), self.EntryLogin.get(), self.EntryPassword.get(), registerWindow))
		self.ButtonRegister1.grid(row=3, column="1")

	def registerAccount(self, name, login, password, registerWindow):
		if name != "" and login != "" and password != "":
			accountFile = open("accounts.txt", "r")

			loginAvailability = True

			for line in accountFile:
				if(line.split(",")[1] == login):
					loginAvailability = False

			if(loginAvailability):
				data = accountFile.readlines()
				accountFile.close()
				data += name + "," + login + "," + password + ",CLIENT;\n"
				accountFile = open("accounts.txt", "w")
				accountFile.writelines(data)
				accountFile.close()
				messagebox.showinfo("Success", "Your account has been created.")
				registerWindow.destroy()
			else:
				messagebox.showerror("Error", "The login you choose is not available. Please try again.")
		else:
			messagebox.showerror("Error", "Fields cannot be empty.")

	def center(self, window):
		window.update_idletasks()
		width = window.winfo_width()
		height = window.winfo_height()
		x = (window.winfo_screenwidth() // 2) - (width // 2)
		y = (window.winfo_screenheight() // 2) - (height // 2)
		window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

	def login(self, login, password):
		if login != "" and password != "":
			accountFile = open("accounts.txt", "r")

			correctData = False

			for line in accountFile:
				if(login == line.split(",")[1] and line.split(',')[2]):
					correctData = True

			if(correctData):
				role = line.split(",")[3]
				role = role[:-2] #delete ; and \n characters

				if(role == "CLIENT"):
					self.laundryClientWindow()
				elif(role == "WORKER"):
					self.laundryWorkerWindow()
				else:
					messagebox.showerror("Error","There is a problem with role assigned to your account. Please contact with administrator.")
			else:
				messagebox.showerror("Error", "Login or password is not correct.")
		else:
			messagebox.showerror("Error", "Fields cannot be empty.")



	def laundryClientWindow(self):
		print("client")
	def laundryWorkerWindow(self):
		print("worker")




app = MainWindow()


