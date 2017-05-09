import tkinter as tk
from tkinter import messagebox
from functools import partial
from tkinter import ttk
import datetime


class MainWindow():
	def __init__(self):
		login = ""

		try:
			with open('accounts.txt', "r") as file:
				pass
		except IOError as e:
			file = open('accounts.txt', "w")
			file.close()

		try:
			with open('orders.txt', "r") as file:
				pass
		except IOError as e:
			file = open('orders.txt', "w")
			file.close()


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

		self.ButtonLogin = tk.Button(root, text="Login", width=10, height=1, command=lambda: self.login(self.EntryLogin.get(),self.EntryPassword.get(), root))
		# self.ButtonLogin.grid(row=2, column="1")
		self.ButtonLogin.place(x=170, y=50, height=28, width=85)

		self.ButtonRegister = tk.Button(root, text="Register", width=10, height=1, command=self.registerWindow)
		# self.ButtonRegister.grid(row=2, column="2")
		self.ButtonRegister.place(x=40, y=50, height=28, width=85)

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

		self.ButtonRegister = tk.Button(registerWindow, text="Register", width=10, height=1, command=lambda: self.registerAccount(self.EntryName.get(), self.EntryLogin.get(), self.EntryPassword.get(), registerWindow))
		self.ButtonRegister.grid(row=3, column="1")
		# self.ButtonRegister.place(x=40, y=80, height=28, width=85)

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
				accountFile = open("accounts.txt", "a+")
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

	def login(self, login, password, loginWindow):
		if login != "" and password != "":
			accountFile = open("accounts.txt", "r")

			correctData = False

			for line in accountFile:
				print(line)
				if(login == line.split(",")[1] and line.split(',')[2]):
					correctData = True

			if(correctData):
				self.login = login
				role = line.split(",")[3]
				role = role[:-1] #delete ; and \n characters
				print(role)

				if(role == "CLIENT"):
					self.laundryClientWindow()
					#loginWindow.withdraw()
				elif(role == "WORKER"):
					self.laundryWorkerWindow()
					#loginWindow.withdraw()
				else:
					messagebox.showerror("Error","There is a problem with role assigned to your account. Please contact with administrator.")
			else:
				messagebox.showerror("Error", "Login or password is not correct.")
		else:
			messagebox.showerror("Error", "Fields cannot be empty.")


	def laundryClientWindow(self):
		laundryClientWindow = tk.Toplevel()
		laundryClientWindow.title("Laundry System")
		self.center(laundryClientWindow)
		laundryClientWindow.geometry("890x250")
		laundryClientWindow.grab_set()

		tree = ttk.Treeview(laundryClientWindow)

		tree["columns"] = ("Collection method", "Address", "Status", "Weight", "Price", "Collection date", "Delivery date")
		# tree.column("ID", width=40)
		tree.column("Collection method", width=100)
		tree.column("Address", width=150)
		tree.column("Status", width=70)
		tree.column("Weight", width=50)
		tree.column("Price", width=50)
		tree.column("Collection date", width=100)
		tree.column("Delivery date", width=100)
		# tree.heading("ID", text="ID")
		tree.heading("Collection method", text="Collection method")
		tree.heading("Address", text="Address")
		tree.heading("Status", text="Status")
		tree.heading("Weight", text="Weight")
		tree.heading("Price", text="Price")
		tree.heading("Collection date", text="Collection date")
		tree.heading("Delivery date", text="Delivery date")

		tree.insert("", 0, values=("1A", "1b", "1b", "1b", "1b", "1b", "1b", "1b"))

		pending = tree.insert("", 1, "Pending orders", text="Pending orders")
		tree.insert(pending, 0,text="1245", values=("Locker", "Mall Luton LU1 HUJ", "In progress", "25kg", "25$", "12-10-2017", "13-10-2017"))
		tree.insert(pending, 0,text="1634", values=("Locker", "Mall Luton LU1 HUJ", "In progress", "25kg", "25$", "12-10-2017", "13-10-2017"))
		tree.insert(pending, 0,text="1733", values=("Locker", "Mall Luton LU1 HUJ", "In progress", "25kg", "25$", "12-10-2017", "13-10-2017"))
		tree.insert(pending, 0,text="2633", values=("Locker", "Mall Luton LU1 HUJ", "In progress", "25kg", "25$", "12-10-2017", "13-10-2017"))

		historyOrders = tree.insert("", 1, "Orders history", text="Orders history")
		tree.insert(historyOrders, 0, text="1245",values=("Locker", "Mall Luton LU1 HUJ", "In progress", "25kg", "25$", "12-10-2017", "13-10-2017"))
		tree.insert(historyOrders, 0, text="1634",values=("Locker", "Mall Luton LU1 HUJ", "In progress", "25kg", "25$", "12-10-2017", "13-10-2017"))
		tree.insert(historyOrders, 0, text="1733",values=("Locker", "Mall Luton LU1 HUJ", "In progress", "25kg", "25$", "12-10-2017", "13-10-2017"))
		tree.insert(historyOrders, 0, text="2633",values=("Locker", "Mall Luton LU1 HUJ", "In progress", "25kg", "25$", "12-10-2017", "13-10-2017"))

		##alternatively:
		# tree.insert("", 3, "dir3", text="Dir 3")
		# tree.insert("dir3", 3, text=" sub dir 3", values=("3A", " 3B"))


		self.refreshTree(tree)
		tree.grid(row=0, column="0")

		ButtonNewOrder = tk.Button(laundryClientWindow, text="New order", width=10, height=1,command=lambda: self.setCollectionMethod(tree))
		ButtonNewOrder.grid(row=3, column="0")

	def refreshTree(self, tree):
		ordersFile = open("orders.txt", "r")

		tree.delete(*tree.get_children())

		tree["columns"] = (
		"Collection method", "Address", "Status", "Weight", "Price", "Collection date", "Delivery date")

		tree.column("Collection method", width=100)
		tree.column("Address", width=150)
		tree.column("Status", width=140)
		tree.column("Weight", width=50)
		tree.column("Price", width=50)
		tree.column("Collection date", width=100)
		tree.column("Delivery date", width=100)

		tree.heading("Collection method", text="Collection method")
		tree.heading("Address", text="Address")
		tree.heading("Status", text="Status")
		tree.heading("Weight", text="Weight")
		tree.heading("Price", text="Price")
		tree.heading("Collection date", text="Collection date")
		tree.heading("Delivery date", text="Delivery date")

		pending = tree.insert("", 0, "Pending orders", text="Pending orders")
		historyOrders = tree.insert("", 1, "Orders history", text="Orders history")

		# indexHistory = 0
		# indexPending = 0
		for line in ordersFile:
			print(self.login + "  " + (line.split("|")[8])[:-2])
			if(self.login == (line.split("|")[8])[:-2]):
				print("jestem")
				if(line.split("|")[3] == "DONE"):
					tree.insert(historyOrders, 0, text=line.split("|")[0], values=(line.split("|")[1], line.split("|")[2], line.split("|")[3], line.split("|")[4], line.split("|")[5], line.split("|")[6], line.split("|")[7]))
					# indexHistory += 1
				else:
					tree.insert(pending, 0, text=line.split("|")[0], values=(line.split("|")[1], line.split("|")[2], line.split("|")[3], line.split("|")[4], line.split("|")[5], line.split("|")[6], line.split("|")[7]))
					# indexPending += 1




	def setCollectionMethod(self, tree):
		newOrderWindow = tk.Toplevel()
		newOrderWindow.title("New order")
		self.center(newOrderWindow)
		newOrderWindow.geometry("300x100")
		newOrderWindow.grab_set()

		self.LabelMethod = tk.Label(newOrderWindow, text="Choose collection method:")
		self.LabelMethod.grid(row=0, column="1")


		self.ButtonDriver = tk.Button(newOrderWindow, text="Book driver", width=10, height=1, command=lambda :self.setOrderAddress("DRIVER", newOrderWindow, tree))
		self.ButtonDriver.grid(row=1, column="0")

		self.ButtonLocker = tk.Button(newOrderWindow, text="Deliver to locker", width=10, height=1, command=lambda:self.setOrderAddress("LOCKER", newOrderWindow, tree))
		self.ButtonLocker.grid(row=1, column="2")

	def setOrderAddress(self, method, previousWindow, tree):
		previousWindow.destroy()

		orderAddressWindow = tk.Toplevel()
		orderAddressWindow.title("New order")
		self.center(orderAddressWindow)
		orderAddressWindow.geometry("300x100")
		orderAddressWindow.grab_set()

		if(method == "LOCKER"):
			temp = tk.StringVar()
			self.LabelLocker = tk.Label(orderAddressWindow, text="Choose locker:")
			self.LabelLocker.grid(row=0, column="0")
			rb1 = ttk.Radiobutton(orderAddressWindow, text='189 Marsh Rd, Luton LU3 2QQ, UK', variable=temp, value="189 Marsh Rd, Luton LU3 2QQ, UK")
			rb2 = ttk.Radiobutton(orderAddressWindow, text='146 Park St, Luton LU1 3EY, UK', variable=temp, value="146 Park St, Luton LU1 3EY, UK")
			rb3 = ttk.Radiobutton(orderAddressWindow, text='152 Dallow Rd, Luton LU4 2EW, UK', variable=temp, value="152 Dallow Rd, Luton LU4 2EW, UK")
			rb1.grid(row=1, column="0")
			rb2.grid(row=2, column="0")
			rb3.grid(row=3, column="0")

			self.ButtonNext = tk.Button(orderAddressWindow, text="Next", width=10, height=1, command=lambda: self.setOrderDates("LOCKER",temp.get(),orderAddressWindow, tree))
			self.ButtonNext.grid(row=4, column="0")
		elif(method == "DRIVER"):
			self.LabelAddress = tk.Label(orderAddressWindow, text="Address: ")
			self.LabelAddress.grid(row=0, column="0")

			self.EntryAddress = tk.Entry(orderAddressWindow, width="100")
			self.EntryAddress.grid(row=0, column="1")

			self.ButtonNext = tk.Button(orderAddressWindow, text="Next", width=10, height=1,command=lambda: self.setOrderDates("DRIVER", self.EntryAddress.get(), orderAddressWindow, tree))
			self.ButtonNext.grid(row=4, column="0")

	def setOrderDates(self, method, address, previousWindow, tree):
		previousWindow.destroy()

		orderDatesWindow = tk.Toplevel()
		orderDatesWindow.title("New order")
		self.center(orderDatesWindow)
		orderDatesWindow.geometry("300x100")
		orderDatesWindow.grab_set()

		self.LabelCollectionDate = tk.Label(orderDatesWindow, text="Collection date: ")
		self.LabelCollectionDate.grid(row=0, column="0")

		self.EntryColDate = tk.Entry(orderDatesWindow, width="100")
		self.EntryColDate.grid(row=0, column="1")

		self.LabelDeliveryDate = tk.Label(orderDatesWindow, text="Delivery date: ")
		self.LabelDeliveryDate.grid(row=1, column="0")

		self.EntryDelDate = tk.Entry(orderDatesWindow, width="100")
		self.EntryDelDate.grid(row=1, column="1")


		# ZABEZPIECZYC DATE!!!!!
		# userdatestring = '2013-05-10'
		# thedate = datetime.datetime.strptime(userdatestring, '%Y-%m-%d')

		self.ButtonFinish = tk.Button(orderDatesWindow, text="Finish", width=10, height=1,command=lambda: self.newOrder(method,address, self.EntryColDate.get(), self.EntryDelDate.get(), orderDatesWindow, tree))
		self.ButtonFinish.grid(row=2, column="0")

	def newOrder(self,method, address, dateCollection, dateDelivery, previousWindow, tree):
		previousWindow.destroy()

		ordersFile = open("orders.txt", "r")
		tempData = ordersFile.readlines()
		ordersFile.close()

		tempData += str(len(tempData)+1) +"|"+ method +"|"+ address +"|Waiting for collection|||" + dateCollection +"|"+ dateDelivery + "|" + self.login + ";\n"

		ordersFile = open("orders.txt", "w")
		ordersFile.writelines(tempData)
		ordersFile.close()

		self.refreshTree(tree)
		messagebox.showinfo("Success", "Your order has been accepted.")





	def laundryWorkerWindow(self):
		laundryWorkerWindow = tk.Toplevel()
		laundryWorkerWindow.title("Laundry System")
		self.center(laundryWorkerWindow)
		laundryWorkerWindow.geometry("400x400")
		laundryWorkerWindow.grab_set()




app = MainWindow()


