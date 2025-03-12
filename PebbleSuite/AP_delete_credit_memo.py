"""
[ ]
[ ]
[ ]
[ ]	AP_delete_credit_memo.py
[ ]
[ ]
[ ]
"""
"""
[ ]
[ ]
[ ]
[ ]	IMPORT PYTHON MODULES:
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




class DELETE_VENDOR_CREDIT_MEMO_WINDOW(tk.Toplevel):

	#Define class variables
	alive = False


	vendor_sql_script = '''SELECT VENDOR_NAME FROM vendors;'''


	#Define class functions
	def __init__(self,*args,**kwargs):

		options = ["Select Vendor"]


		#Initialize SQL.db connection:
		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(self.vendor_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()
			cursor.close()


		#Define class tkinter widgets:
		super().__init__(*args,**kwargs)
		self.config(width=390,height=550)
		self.title("Delete Vendor Credit Memo")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.invoice_name_label = ttk.Label(self,text="Vendor Name")
		self.invoice_name_label.place(x=20,y=15)


		#Search for vendor names in SQL.db.
		#Insert vendor names into vendor search listbox widget.
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


		#Credit memo selection listbox widget:
		self.scrollbar = ttk.Scrollbar(self)
		self.scrollbar.place(x=353,y=300,width=20,height=200)
		self.listbox = tk.Listbox(self,yscrollcommand=self.scrollbar.set)
		self.listbox.place(x=20,y=300,width=333,height=200)
		self.scrollbar.config(command=self.listbox.yview)

		self.search_credit_memos_button = ttk.Button(self,text="Search Credit Memos",command=self.search_credit_memos)
		self.search_credit_memos_button.place(x=20,y=255)

		self.clear_credit_memos_button = ttk.Button(self,text="Clear All Credit Memos",command=self.clear_credit_memos)
		self.clear_credit_memos_button.place(x=20,y=510)

		self.delete_credit_memo_button = ttk.Button(self,text="Delete Credit Memo",command=self.delete_credit_memo)
		self.delete_credit_memo_button.place(x=200,y=510)


	def search_credit_memos(self):

		search_vendor_sql_script = '''SELECT CREDIT_MEMO_NUMBER FROM vendor_credit_memos WHERE CREDIT_MEMO_NAME=?'''

		for item in self.select_vendor_listbox.curselection():

			select_vendor = self.select_vendor_listbox.get(item)

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()
				cursor.execute(search_vendor_sql_script,[select_vendor])

				for item in cursor:

					self.listbox.insert(0,item)

				connection.commit()
				cursor.close()

		except sqlite3.Error as error:

			search_credit_memos_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")


	def clear_credit_memos(self):

		self.listbox.delete(0,tk.END)


	def delete_credit_memo(self):

		#Define SQL.db scripts:
		query_credit_memo_sql_script = '''SELECT * FROM vendor_credit_memos WHERE CREDIT_MEMO_NUMBER=?'''
		delete_credit_memo_sql_script = '''DELETE FROM vendor_credit_memos WHERE CREDIT_MEMO_NUMBER=?'''
		query_journal_entries_sql_script = '''SELECT * FROM journal_entries WHERE VENDOR_CREDIT_MEMO_NUMBER=?'''
		delete_journal_entries_sql_script = '''DELETE FROM journal_entries WHERE VENDOR_CREDIT_MEMO_NUMBER=?'''


		for item in self.listbox.curselection():

			select_credit_memo = self.listbox.get(item)

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()
				cursor.execute(query_credit_memo_sql_script,select_credit_memo)
				cursor.execute(delete_credit_memo_sql_script,select_credit_memo)
				cursor.execute(query_journal_entries_sql_script,select_credit_memo)
				cursor.execute(delete_journal_entries_sql_script,select_credit_memo)
				connection.commit()
				cursor.close()
				delete_credit_memo_confirmation_message = tk.messagebox.showinfo(title="Delete Credit Memo",message="Credit memo successfully deleted.")

		except sqlite3.Error as error:

			delete_credit_memo_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")



	def destroy(self):
		self.__class__.alive = False
		return super().destroy()
