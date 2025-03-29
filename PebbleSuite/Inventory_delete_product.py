"""
[ ]
[ ]
[ ]
[ ]	GL_delete_GL.py:
[ ]
[ ]
[ ]
"""


"""
[ ]
[ ]
[ ]
[ ]	IMPORT PYTHON LIBRARIES:
[ ]
[ ]
[ ]
"""


#Python Standard Library dependencies

import datetime
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo


"""
[ ]
[ ]
[ ]
[ ]	DELETE_GL_WINDOW CLASS:
[ ]
[ ]
[ ]
"""


class DELETE_GL_WINDOW(tk.Toplevel):

	#Define class variables
	alive = False

	delete_selection_temporary_memory = []


	general_ledger_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers;'''


	#Define class functions
	def __init__(self,*args,**kwargs):

		options = ["Select General Ledger"]


		#Initialize SQL.db connection:
		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(self.general_ledger_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()
			cursor.close()

		"""
		[ ]
		[ ]
		[ ]
		[ ]	DEFINE DELETE_GL_WINDOW TKINTER WIDGETS:
		[ ]	DEFINE INITIAL SQL.db SCRIPTS:
		[ ]
		[ ]
		[ ]
		"""

			#Tkinter widgets here:

		super().__init__(*args,**kwargs)
		self.config(width=600,height=270)
		self.title("Delete General Ledger")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.general_ledger_name_label = ttk.Label(self,text="General Ledger Name:")
		self.general_ledger_name_label.place(x=20,y=15)

		self.select_general_ledger_scrollbar = ttk.Scrollbar(self)
		self.select_general_ledger_scrollbar.place(x=353,y=45,width=20,height=170)
		self.select_general_ledger_listbox = tk.Listbox(self,yscrollcommand=self.select_general_ledger_scrollbar.set)
		self.select_general_ledger_listbox.place(x=20,y=45,width=333,height=170)
		self.select_general_ledger_scrollbar.config(command=self.select_general_ledger_listbox.yview)


			#SQL.db scripts:

		search_general_ledger_name_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers;'''

		"""
		[ ]
		[ ]
		[ ]
		[ ]	CONNECT TO SQL.db, RETRIEVE NAMES OF ALL GENERAL LEDGERS:
		[ ]
		[ ]
		[ ]
		"""

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(search_general_ledger_name_sql_script)
			connection.commit()

			for item in cursor:

				self.select_general_ledger_listbox.insert(0," ".join(item))

			cursor.close()

		"""
		[ ]
		[ ]
		[ ]
		[ ]	DEFINE 'DELETE_GL_WINDOW' TKINTER WIDGETS:
		[ ]
		[ ]
		[ ]
		"""

		self.delete_general_ledger_button = ttk.Button(self,text="Select General Ledger",command=self.delete_general_ledger)
		self.delete_general_ledger_button.place(x=20,y=230)

		self.general_ledger_name_label = ttk.Label(self,text="General Ledger Name:")
		self.general_ledger_name_label.place(x=400,y=15)
		self.general_ledger_name_entry_text = tk.StringVar()
		self.general_ledger_name_entry = ttk.Entry(self,textvariable=self.general_ledger_name_entry_text,width=21)
		self.general_ledger_name_entry.place(x=400,y=45)

		self.general_ledger_number_label = ttk.Label(self,text="General Ledger Number:")
		self.general_ledger_number_label.place(x=400,y=85)
		self.general_ledger_number_entry_text = tk.StringVar()
		self.general_ledger_number_entry = ttk.Entry(self,textvariable=self.general_ledger_number_entry_text,state=tk.DISABLED,width=21)
		self.general_ledger_number_entry.place(x=400,y=115)

		self.general_ledger_type_label = ttk.Label(self,text="General Ledger Type:")
		self.general_ledger_type_label.place(x=400,y=155)
		self.general_ledger_type_entry_text = tk.StringVar()
		self.general_ledger_type_entry = ttk.Entry(self,textvariable=self.general_ledger_type_entry_text,state=tk.DISABLED,width=21)
		self.general_ledger_type_entry.place(x=400,y=185)

		self.cancel_general_ledger_changes_button = ttk.Button(self,text="Cancel",command=self.cancel_changes)
		self.cancel_general_ledger_changes_button.place(x=490,y=230)

		self.submit_general_ledger_changes_button = ttk.Button(self,text="Delete",command=self.submit_changes)
		self.submit_general_ledger_changes_button.place(x=400,y=230)


	def delete_general_ledger(self):

		"""
		[ ]
		[ ]
		[ ]
		[ ]	DEFINE SQL.db SCRIPTS, RETRIEVE SELECTED GENERAL LEDGER FROM TKINTER LISTBOX.
		[ ]
		[ ]
		[ ]
		"""

		query_general_ledger_sql_script = '''SELECT * FROM general_ledgers WHERE GENERAL_LEDGER_NAME=?'''


		for item in self.select_general_ledger_listbox.curselection():

			select_general_ledger = self.select_general_ledger_listbox.get(item)

		"""
		[ ]
		[ ]
		[ ]
		[ ]	CONNECT TO SQL.db, RETRIEVE DATA FOR SELECTED GENERAL LEDGER:
		[ ]
		[ ]
		[ ]
		"""

		try:

			with sqlite3.connect("SQL.db") as connection:

				collect = []

				cursor = connection.cursor()
				cursor.execute(query_general_ledger_sql_script,[select_general_ledger])

				for item in cursor:
					collect.append(item)
					self.delete_selection_temporary_memory.append(item)

				self.general_ledger_name_entry_text.set(f"{collect[0][0]}")
				self.general_ledger_number_entry_text.set(f"{collect[0][1]}")
				self.general_ledger_type_entry_text.set(f"{collect[0][2]}")

				connection.commit()
				cursor.close()

		except sqlite3.Error as error:

			delete_general_ledger_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")


	def submit_changes(self):

		"""
		[ ]
		[ ]
		[ ]
		[ ]	DEFINE 'SUBMIT_CHANGES' SQL SCRIPTS:
		[ ]
		[ ]
		[ ]
		"""

		#Search general_ledgers table:
		retrieve_general_ledger_sql_script = '''SELECT * FROM general_ledgers WHERE GENERAL_LEDGER_NAME=?;'''
		delete_general_ledger_name_sql_script = '''DELETE FROM general_ledgers WHERE GENERAL_LEDGER_NAME=?;'''

		#Search vendor_invoices_table:
		retrieve_vendor_invoices_sql_script_1 = '''SELECT * FROM vendor_invoices WHERE INVOICE_LIABILITY_ACCOUNT=?;'''
		retrieve_vendor_invoices_sql_script_2 = '''SELECT * FROM vendor_invoices WHERE INVOICE_EXPENSE_ACCOUNT=?;'''
		delete_vendor_invoices_sql_script_1 = '''DELETE FROM vendor_invoices WHERE INVOICE_LIABILITY_ACCOUNT=?;'''
		delete_vendor_invoices_sql_script_2 = '''DELETE FROM vendor_invoices WHERE INVOICE_EXPENSE_ACCOUNT=?;'''

		#Search client_invoices_table:
		retrieve_client_invoices_sql_script_1 = '''SELECT * FROM client_invoices WHERE INVOICE_ASSET_ACCOUNT=?;'''
		retrieve_client_invoices_sql_script_2 = '''SELECT * FROM client_invoices WHERE INVOICE_INCOME_ACCOUNT=?;'''
		delete_client_invoices_sql_script_1 = '''DELETE FROM client_invoices WHERE INVOICE_ASSET_ACCOUNT=?;'''
		delete_client_invoices_sql_script_2 = '''DELETE FROM client_invoices WHERE INVOICE_INCOME_ACCOUNT=?;'''

		#Search journal_entries table:
		retrieve_journal_entries_sql_script = '''SELECT * FROM journal_entries WHERE GENERAL_LEDGER_NAME=?;'''
		delete_JE_GL_name_sql_script = '''DELETE FROM journal_entries WHERE GENERAL_LEDGER_NAME=?;'''
		delete_JE_offset_GL_name_sql_script = '''DELETE FROM journal_entries WHERE OFFSET_GENERAL_LEDGER_NAME=?;'''

		"""
		[ ]
		[ ]
		[ ]
		[ ]	DEFINE TEMPORARY MEMORY VARIABLES:
		[ ]
		[ ]
		[ ]
		"""

		#Define function variables:
		prev_general_ledger_name = self.delete_selection_temporary_memory[0][0]
		prev_general_ledger_number = self.delete_selection_temporary_memory[0][1]

		"""
		[ ]
		[ ]
		[ ]
		[ ]	CONNECT TO SQL.db, DELETE GENERAL LEDGER DATA:
		[ ]
		[ ]
		[ ]
		"""

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()
				cursor.execute(retrieve_general_ledger_sql_script,[prev_general_ledger_name])
				cursor.execute(delete_general_ledger_name_sql_script,[prev_general_ledger_name])
				connection.commit()
				cursor.close()
				delete_general_ledger_confirmation_message_1 = tk.messagebox.showinfo(title="Delete General Ledger",message="General Ledger data deleted")

		except sqlite3.Error as error:

			delete_general_ledger_error_message_1 = tk.messagebox.showinfo(title="Error",message=f"{error}")

		"""
		[ ]
		[ ]
		[ ]
		[ ]	CONNECT TO SQL.db, DELETE JOURNAL ENTRY DATA:
		[ ]
		[ ]
		[ ]
		"""

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()
				cursor.execute(retrieve_general_ledger_sql_script,[prev_general_ledger_name])
				cursor.execute(delete_JE_GL_name_sql_script,[prev_general_ledger_name])
				cursor.execute(delete_JE_offset_GL_name_sql_script,[prev_general_ledger_name])
				connection.commit()
				cursor.close()
				delete_journal_entries_confirmation_message = tk.messagebox.showinfo(title="Delete General Ledger",message="Journal Entries successfully deleted")

		except sqlite3.Error as error:

			delete_general_ledger_error_message_3 = tk.messagebox.showinfo(title="Error",message=f"{error}")

		"""
		[ ]
		[ ]
		[ ]
		[ ]	CONNECT TO SQL.db, DELETE VENDOR INVOICE DATA:
		[ ]
		[ ]
		[ ]
		"""

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()
				cursor.execute(retrieve_vendor_invoices_sql_script_1,[prev_general_ledger_name])
				cursor.execute(delete_vendor_invoices_sql_script_1,[prev_general_ledger_name])
				cursor.execute(retrieve_vendor_invoices_sql_script_2,[prev_general_ledger_name])
				cursor.execute(delete_vendor_invoices_sql_script_2,[prev_general_ledger_name])
				connection.commit()
				cursor.close()
				delete_vendor_invoices_confirmation_message_1 = tk.messagebox.showinfo(title="Delete General Ledger",message="Vendor Invoice data successfully deleted")

		except sqlite3.Error as error:

			delete_vendor_invoices_error_message_2 = tk.messagebox.showinfo(title="Error",message=f"{error}")

		"""
		[ ]
		[ ]
		[ ]
		[ ]	CONNECT TO SQL.db, DELETE CLIENT INVOICE DATA:
		[ ]
		[ ]
		[ ]
		"""

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()
				cursor.execute(retrieve_client_invoices_sql_script_1,[prev_general_ledger_name])
				cursor.execute(delete_client_invoices_sql_script_1,[prev_general_ledger_name])
				cursor.execute(retrieve_client_invoices_sql_script_2,[prev_general_ledger_name])
				cursor.execute(delete_client_invoices_sql_script_2,[prev_general_ledger_name])
				connection.commit()
				cursor.close()
				delete_client_invoices_confirmation_message_1 = tk.messagebox.showinfo(title="Delete General Ledger",message="Client Invoice data successfully deleted")

		except sqlite3.Error as error:

			delete_client_invoices_error_message_1 = tk.messagebox.showinfo(title="Error",message=f"{error}")

		"""
		[ ]
		[ ]
		[ ]
		[ ]	DELETE MEMORY DATA FROM FUNCTION'S TEMPORARY MEMORY VARIABLES:
		[ ]
		[ ]
		[ ]
		"""

		try:

			self.delete_selection_temporary_memory.clear()
			self.general_ledger_name_entry_text.set("")
			self.general_ledger_number_entry_text.set("")
			self.general_ledger_type_entry_text.set("")

		except:

			temporary_memory_error_message_1 = tk.messagebox.showinfo(title="Delete General Ledger",message="Cannot clear General Ledger entries")


	def cancel_changes(self):

		try:

			self.general_ledger_name_entry_text.set("")
			self.general_ledger_number_entry_text.set("")
			self.general_ledger_type_entry_text.set("")

		except:

			cancel_changes_error_message = tk.messagebox.showinfo(title="Error",message="Unable to clear data entries.")


	def destroy(self):
		self.__class__.alive = False
		return super().destroy()
