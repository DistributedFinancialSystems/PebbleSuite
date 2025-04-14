"""
[ ]
[ ]
[ ]
[ ]	AP_delete_invoice.py
[ ]
[ ]
[ ]
"""

import datetime
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class DELETE_INVOICE_WINDOW(tk.Toplevel):

	alive = False

	vendor_sql_script = '''SELECT VENDOR_NAME FROM vendors;'''

	def __init__(self,*args,**kwargs):

		options = ["Select Vendor"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.vendor_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()

		super().__init__(*args,**kwargs)
		self.config(width=390,height=550)
		self.title("Delete Invoice")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.invoice_name_label = ttk.Label(self,text="Vendor Name")
		self.invoice_name_label.place(x=20,y=15)

		self.select_vendor_scrollbar = ttk.Scrollbar(self)
		self.select_vendor_scrollbar.place(x=353,y=45,width=20,height=200)
		self.select_vendor_listbox = tk.Listbox(self,yscrollcommand=self.select_vendor_scrollbar.set)
		self.select_vendor_listbox.place(x=20,y=45,width=333,height=200)
		self.select_vendor_scrollbar.config(command=self.select_vendor_listbox.yview)

		search_vendor_name_sql_script = '''SELECT VENDOR_NAME FROM vendors;'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(search_vendor_name_sql_script)

			connection.commit()

			for item in cursor:

				self.select_vendor_listbox.insert(0," ".join(item))

			cursor.close()

		self.scrollbar = ttk.Scrollbar(self)
		self.scrollbar.place(x=353,y=300,width=20,height=200)
		self.listbox = tk.Listbox(self,yscrollcommand=self.scrollbar.set)
		self.listbox.place(x=20,y=300,width=333,height=200)
		self.scrollbar.config(command=self.listbox.yview)

		self.search_invoices_button = ttk.Button(self,text="Search Invoices",command=self.search_invoices)
		self.search_invoices_button.place(x=20,y=255)

		self.clear_invoices_button = ttk.Button(self,text="Clear All Invoices",command=self.clear_invoices)
		self.clear_invoices_button.place(x=20,y=510)

		self.delete_invoice_button = ttk.Button(self,text="Delete Invoice",command=self.delete_invoice)
		self.delete_invoice_button.place(x=200,y=510)


	def search_invoices(self):

		search_vendor_sql_script = '''SELECT INVOICE_NUMBER FROM vendor_invoices WHERE INVOICE_NAME=?'''

		try:

			for item in self.select_vendor_listbox.curselection():

				select_vendor = self.select_vendor_listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(search_vendor_sql_script,[select_vendor])

				for item in cursor:

					self.listbox.insert(0,item)

				connection.commit()

				cursor.close()

		except Exception as error:

			search_invoices_error_message = tk.messagebox.showinfo(title="Delete Vendor Invoice",message=f"{error}")


	def clear_invoices(self):

		try:

			self.listbox.delete(0,tk.END)

		except Exception as error:

			clear_invoices_error_message_1 = tk.messagebox.showinfo(title="")


	def delete_invoice(self):

		query_invoice_sql_script = '''SELECT * FROM vendor_invoices WHERE INVOICE_NUMBER=?'''
		delete_invoice_sql_script = '''DELETE FROM vendor_invoices WHERE INVOICE_NUMBER=?'''
		query_journal_entries_sql_script = '''SELECT * FROM journal_entries WHERE VENDOR_INVOICE_NUMBER=?'''
		delete_journal_entries_sql_script = '''DELETE FROM journal_entries WHERE VENDOR_INVOICE_NUMBER=?'''

		try:

			for item in self.listbox.curselection():

				select_invoice = self.listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()
				cursor.execute(query_invoice_sql_script,select_invoice)
				cursor.execute(delete_invoice_sql_script,select_invoice)
				cursor.execute(query_journal_entries_sql_script,select_invoice)
				cursor.execute(delete_journal_entries_sql_script,select_invoice)
				connection.commit()
				cursor.close()
				delete_invoice_confirmation_message = tk.messagebox.showinfo(title="Delete Vendor Invoice",message="Invoice successfully deleted.")

		except Exception as error:

			delete_invoice_error_message = tk.messagebox.showinfo(title="Delete Vendor Invoice",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
