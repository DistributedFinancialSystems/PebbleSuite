#Python Standard Library dependencies
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class DELETE_VENDOR_ENTRY:


	#Define required class entries:
	def __init__(self,vendor_name):

		self.vendor_name = vendor_name


	def delete_data(self):

		#Define SQL database scripts:
		query_vendor_sql_script = '''SELECT * FROM vendors WHERE VENDOR_NAME=?;'''
		delete_vendor_sql_script = '''DELETE FROM vendors WHERE VENDOR_NAME=?;'''
		query_vendor_invoices_sql_script = '''SELECT * FROM vendor_invoices WHERE INVOICE_NAME=?;'''
		delete_vendor_invoices_sql_script = '''DELETE FROM vendor_invoices WHERE INVOICE_NAME=?;'''
		query_vendor_credit_memos_sql_script = '''SELECT * FROM vendor_credit_memos WHERE CREDIT_MEMO_NAME=?;'''
		delete_vendor_credit_memos_sql_script = '''DELETE FROM vendor_credit_memos WHERE CREDIT_MEMO_NAME=?;'''
		query_vendor_journal_entries_sql_script = '''SELECT * FROM journal_entries WHERE JOURNAL_ENTRY_VENDOR_NAME=?;'''
		delete_vendor_journal_entries_sql_script = '''DELETE FROM journal_entries WHERE JOURNAL_ENTRY_VENDOR_NAME=?;'''


		#Initialize SQL database connection:
		with sqlite3.connect("SQL.db") as connection:

			try:

				cursor = connection.cursor()
				cursor.execute(query_vendor_sql_script,[self.vendor_name])
				cursor.execute(delete_vendor_sql_script,[self.vendor_name])
				connection.commit()
				cursor.close()
				delete_vendor_confirmation_message = tk.messagebox.showinfo(title="Delete Vendor",message="Vendor contact data successfully deleted.")

			except sqlite3.Error as error:

				delete_vendor_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")

			try:
				cursor = connection.cursor()
				cursor.execute(query_vendor_invoices_sql_script,[self.vendor_name])
				cursor.execute(delete_vendor_invoices_sql_script,[self.vendor_name])
				connection.commit()
				cursor.close()
				delete_vendor_invoices_confirmation_message = tk.messagebox.showinfo(title="Delete Vendor",message="Vendor invoice data deleted")

			except sqlite3.Error as error:

				delete_vendor_invoices_error_message = tk.messagebox.showinfo(title="Delete Vendor",message=f"{error}")

			try:

				cursor = connection.cursor()
				cursor.execute(query_vendor_credit_memos_sql_script,[self.vendor_name])
				cursor.execute(delete_vendor_credit_memos_sql_script,[self.vendor_name])
				connection.commit()
				cursor.close()
				delete_vendor_credit_memos_confirmation_message = tk.messagebox.showinfo(title="Delete Vendor",message="Vendor credit memos deleted")

			except sqlite3.Error as error:

				delete_vendor_credit_memos_error_message = tk.messagebox.showinfo(title="Delete Vendor",message=f"{error}")

			try:

				cursor = connection.cursor()
				cursor.execute(query_vendor_journal_entries_sql_script,[self.vendor_name])
				cursor.execute(delete_vendor_journal_entries_sql_script,[self.vendor_name])
				connection.commit()
				cursor.close()
				delete_vendor_journal_entries_confirmation_message = tk.messagebox.showinfo(title="Delete Vendor",message="Vendor journal entries deleted")

			except sqlite3.Error as error:

				delete_vendor_journal_entries_error_message = tk.messagebox.showinfo(title="Delete Vendor",message=f"{error}")




class DELETE_VENDOR_WINDOW(tk.Toplevel):


	#Define SQL database scripts:
	vendor_sql_script = '''SELECT VENDOR_NAME FROM vendors;'''


	#Define class variables:
	alive = False


	def __init__(self,*args,**kwargs):

		vendor_data = []

		options = ["Select Vendor","Select Vendor"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(self.vendor_sql_script)

			for item in cursor:
				options.append(" ".join(item))

			connection.commit()
			cursor.close()


		#Set up DELETE_VENDOR_WINDOW tkinter widgets
		super().__init__(*args,**kwargs)
		self.config(width=390,height=150)
		self.title("Delete Vendor")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")
		self.vendor_name_label = ttk.Label(self,text="Vendor Name")
		self.vendor_name_label.place(x=20,y=40)
		self.vendor_option_menu = ttk.OptionMenu(self,self.clicked,*options)
		self.vendor_option_menu.place(x=200,y=40)
		self.delete_vendor_button = ttk.Button(self,text="Delete Vendor",command=self.delete_vendor)
		self.delete_vendor_button.place(x=20,y=110)


	def delete_vendor(self):

		#Define function variables:
		vendor_data = self.clicked.get()

		#Define delete_vendor function:

		if vendor_data == "Select Vendor":

			delete_vendor_error_message = tk.messagebox.showinfo(title="Error",message="Select a vendor to delete.")

		else:

			delete_object = DELETE_VENDOR_ENTRY(vendor_data)
			delete_object.delete_data()


	def destroy(self):

		self.__class__.alive = False
		return super().destroy()
