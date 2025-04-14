import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class CUSTOMER_SUMMARY_WINDOW(tk.Toplevel):

	alive = False

	def __init__(self,*args,**kwargs):

		super().__init__(*args,**kwargs)
		self.config(width=220,height=120)
		self.title("Customer Summary")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.print_customers_button = ttk.Button(self,text="Print Customers",command=self.print_customers)
		self.print_customers_button.place(x=20,y=20)

		self.export_customers_button = ttk.Button(self,text="Export Customers",command=self.export_customers)
		self.export_customers_button.place(x=20,y=60)


	def print_customers(self):

		try:

			print_customers_sql_script = '''SELECT * FROM customers;'''

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(print_customers_sql_script)

				for item in cursor:

					print(item)

				connection.commit()

				cursor.close()

		except Exception as error:

			print_customers_error_message_1 = tk.messagebox.showinfo(title="Customer Summary",message=f"{error}")


	def export_customers(self):

		try:
			pass

		except Exception as error:

			export_customers_error_message_1 = tk.messagebox.showinfo(title="Customer Summary",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
