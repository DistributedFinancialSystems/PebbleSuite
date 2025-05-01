#Python Standard Library dependencies
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class CLIENT_SUMMARY_WINDOW(tk.Toplevel):

	#Define class variables:
	alive = False


	#Define CLIENT_SUMMARY tkinter widgets:
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.config(width=220,height=120)
		self.title("Client Summary")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.print_clients_button = ttk.Button(self,text="Print Clients",command=self.print_clients)
		self.print_clients_button.place(x=20,y=20)

		self.export_clients_button = ttk.Button(self,text="Export Clients",command=self.export_clients)
		self.export_clients_button.place(x=20,y=60)


	def print_clients(self):

		#Define SQL database scripts:
		print_clients_sql_script = '''SELECT * FROM clients;'''


		#Initialize SQL database connection:
		try:
			with sqlite3.connect("SQL.db") as connection:
				cursor = connection.cursor()
				cursor.execute(print_clients_sql_script)

				for item in cursor:
					print(item)

				connection.commit()
				cursor.close()

		except sqlite3.Error as error:

			print_clients_error_message = tk.messagebox.showinfo(title="Error Message",message=f"{error}")

	def export_clients(self):

		#Define SQL.db scripts:

		#Initialize SQL.db connection:

		try:
			pass

		except sqlite3.Error as error:

			export_clients_error_message = tk.messagebox.showinfo(title="Export Clients",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False
		return super().destroy()
