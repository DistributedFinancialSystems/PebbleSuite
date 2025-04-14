"""
[ ]
[ ]
[ ]
[ ]	AP_delete_credit_memo.py
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
		self.title("Delete Vendor Credit Memo")
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

		self.search_credit_memos_button = ttk.Button(self,text="Search Credit Memos",command=self.search_credit_memos)
		self.search_credit_memos_button.place(x=20,y=255)

		self.clear_credit_memos_button = ttk.Button(self,text="Clear All Credit Memos",command=self.clear_credit_memos)
		self.clear_credit_memos_button.place(x=20,y=510)

		self.delete_credit_memo_button = ttk.Button(self,text="Delete Credit Memo",command=self.delete_credit_memo)
		self.delete_credit_memo_button.place(x=200,y=510)


	def search_credit_memos(self):

		search_vendor_sql_script = '''SELECT CREDIT_MEMO_NUMBER FROM vendor_credit_memos WHERE CREDIT_MEMO_NAME=?'''

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

			search_credit_memos_error_message = tk.messagebox.showinfo(title="Delete Vendor Credit Memo",message=f"{error}")


	def clear_credit_memos(self):

		try:

			self.listbox.delete(0,tk.END)

		except Exception as error:

			clear_credit_memos_error_message_1 = tk.messagebox.showinfo(title="Delete Vendor Credit Memo",message=f"{error}")


	def delete_credit_memo(self):

		query_credit_memo_sql_script = '''SELECT * FROM vendor_credit_memos WHERE CREDIT_MEMO_NUMBER=?'''
		delete_credit_memo_sql_script = '''DELETE FROM vendor_credit_memos WHERE CREDIT_MEMO_NUMBER=?'''
		query_journal_entries_sql_script = '''SELECT * FROM journal_entries WHERE VENDOR_CREDIT_MEMO_NUMBER=?'''
		delete_journal_entries_sql_script = '''DELETE FROM journal_entries WHERE VENDOR_CREDIT_MEMO_NUMBER=?'''

		try:

			for item in self.listbox.curselection():

				select_credit_memo = self.listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(query_credit_memo_sql_script,select_credit_memo)
				cursor.execute(delete_credit_memo_sql_script,select_credit_memo)
				cursor.execute(query_journal_entries_sql_script,select_credit_memo)
				cursor.execute(delete_journal_entries_sql_script,select_credit_memo)

				connection.commit()

				cursor.close()

				delete_credit_memo_confirmation_message = tk.messagebox.showinfo(title="Delete Vendor Credit Memo",message="Credit memo successfully deleted.")

		except Exception as error:

			delete_credit_memo_error_message = tk.messagebox.showinfo(title="Delete Vendor Credit Memo",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
