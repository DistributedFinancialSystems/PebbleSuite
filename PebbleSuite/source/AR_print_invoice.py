import datetime
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class AR_PRINT_INVOICE_WINDOW(tk.Toplevel):

	alive = False

	def __init__(self,*args,**kwargs):

		super().__init__(*args,**kwargs)
		self.config(height=100,width=150)
		self.title("New Invoice")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.invoice_report_button = ttk.Button(self,text="Print Invoices",command=self.invoice_report)
		self.invoice_report_button.place(x=20,y=20)


	def invoice_report(self):

		invoice_report_sql_script = '''SELECT * FROM client_invoices;'''

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(invoice_report_sql_script)

				for item in cursor:

					print(item)

				connection.commit()

				cursor.close()

		except Exception as error:

			print(error)


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
