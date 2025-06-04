"""
[ ]
[ ]
[ ]
[ ]	AP_edit_credit_memo.py
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




class AP_EDIT_CREDIT_MEMO_WINDOW(tk.Toplevel):

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
		self.config(width=600,height=550)
		self.title("Edit Vendor Credit Memo")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.credit_memo_name_label = ttk.Label(self,text="Vendor Name")
		self.credit_memo_name_label.place(x=20,y=15)

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
		self.clear_credit_memos_button.place(x=145,y=510)

		self.edit_credit_memo_button = ttk.Button(self,text="Edit Credit Memo",command=self.edit_credit_memo)
		self.edit_credit_memo_button.place(x=20,y=510)

		self.credit_memo_issue_date_label = ttk.Label(self,text="Credit Memo Issue Date: *")
		self.credit_memo_issue_date_label.place(x=400,y=15)
		self.credit_memo_issue_date_entry_text = tk.StringVar()
		self.credit_memo_issue_date_entry = ttk.Entry(self,textvariable=self.credit_memo_issue_date_entry_text,state=tk.DISABLED)
		self.credit_memo_issue_date_entry.place(x=400,y=45)

		self.credit_memo_due_date_label = ttk.Label(self,text="Credit Memo Due Date: *")
		self.credit_memo_due_date_label.place(x=400,y=85)
		self.credit_memo_due_date_entry_text = tk.StringVar()
		self.credit_memo_due_date_entry = ttk.Entry(self,textvariable=self.credit_memo_due_date_entry_text,state=tk.DISABLED)
		self.credit_memo_due_date_entry.place(x=400,y=115)

		self.credit_memo_number_label = ttk.Label(self,text="Credit Memo Number: *")
		self.credit_memo_number_label.place(x=400,y=155)
		self.credit_memo_number_entry_text = tk.StringVar()
		self.credit_memo_number_entry = ttk.Entry(self,textvariable=self.credit_memo_number_entry_text,state=tk.DISABLED)
		self.credit_memo_number_entry.place(x=400,y=185)

		self.credit_memo_liability_GL_label = ttk.Label(self,text="Credit Memo Liability GL: *")
		self.credit_memo_liability_GL_label.place(x=400,y=225)
		self.credit_memo_liability_GL_entry_text = tk.StringVar()
		self.credit_memo_liability_GL_entry = ttk.Entry(self,textvariable=self.credit_memo_liability_GL_entry_text,state=tk.DISABLED)
		self.credit_memo_liability_GL_entry.place(x=400,y=255)

		self.credit_memo_expense_GL_label = ttk.Label(self,text="Credit Memo Expense GL: *")
		self.credit_memo_expense_GL_label.place(x=400,y=295)
		self.credit_memo_expense_GL_entry_text = tk.StringVar()
		self.credit_memo_expense_GL_entry = ttk.Entry(self,textvariable=self.credit_memo_expense_GL_entry_text,state=tk.DISABLED)
		self.credit_memo_expense_GL_entry.place(x=400,y=325)

		self.credit_memo_amount_label = ttk.Label(self,text="Credit Memo Amount: *")
		self.credit_memo_amount_label.place(x=400,y=365)
		self.credit_memo_amount_entry_text = tk.StringVar()
		self.credit_memo_amount_entry = ttk.Entry(self,textvariable=self.credit_memo_amount_entry_text)
		self.credit_memo_amount_entry.place(x=400,y=395)

		self.credit_memo_notes_label = ttk.Label(self,text="Credit Memo Notes:")
		self.credit_memo_notes_label.place(x=400,y=435)
		self.credit_memo_notes_entry_text = tk.StringVar()
		self.credit_memo_notes_entry = ttk.Entry(self,textvariable=self.credit_memo_notes_entry_text)
		self.credit_memo_notes_entry.place(x=400,y=465)

		self.cancel_credit_memo_changes_button = ttk.Button(self,text="Close",command=self.cancel_changes)
		self.cancel_credit_memo_changes_button.place(x=490,y=510)

		self.submit_credit_memo_changes_button = ttk.Button(self,text="Save",command=self.submit_changes)
		self.submit_credit_memo_changes_button.place(x=400,y=510)


	def search_credit_memos(self):

		search_vendor_sql_script = '''SELECT CREDIT_MEMO_NUMBER FROM vendor_credit_memos WHERE CREDIT_MEMO_NAME=? AND CREDIT_MEMO_STATUS="Open";'''

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

			search_credit_memos_error_message_1 = tk.messagebox.showinfo(title="Edit Vendor Credit Memo",message=f"{error}")


	def clear_credit_memos(self):

		try:

			self.listbox.delete(0,tk.END)

		except Exception as error:

			clear_credit_memos_error_message_1 = tk.messagebox.showinfo(title="Edit Vendor Credit Memo",message=f"{error}")


	def edit_credit_memo(self):

		query_credit_memo_sql_script = '''SELECT * FROM vendor_credit_memos WHERE CREDIT_MEMO_NUMBER=?'''

		try:

			for item in self.listbox.curselection():

				select_credit_memo = self.listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				collect = []

				cursor = connection.cursor()

				cursor.execute(query_credit_memo_sql_script,select_credit_memo)

				for item in cursor:

					collect.append(item)

				self.credit_memo_issue_date_entry_text.set(f"{collect[0][1]}")
				self.credit_memo_due_date_entry_text.set(f"{collect[0][2]}")
				self.credit_memo_number_entry_text.set(f"{collect[0][3]}")
				self.credit_memo_liability_GL_entry_text.set(f"{collect[0][4]}")
				self.credit_memo_expense_GL_entry_text.set(f"{collect[0][5]}")
				self.credit_memo_amount_entry_text.set(f"{collect[0][6]}")
				self.credit_memo_notes_entry_text.set(f"{collect[0][7]}")

				connection.commit()

				cursor.close()

		except Exception as error:

			edit_credit_memo_error_message_1 = tk.messagebox.showinfo(title="Edit Vendor Credit Memo",message=f"{error}")


	def submit_changes(self):

		retrieve_credit_memo_sql_script = '''SELECT * FROM vendor_credit_memos WHERE CREDIT_MEMO_NUMBER=?;'''
		edit_credit_memo_issue_date_sql_script = '''UPDATE vendor_credit_memos SET CREDIT_MEMO_ISSUE_DATE=? WHERE CREDIT_MEMO_NUMBER=?;'''
		edit_credit_memo_due_date_sql_script = '''UPDATE vendor_credit_memos SET CREDIT_MEMO_DUE_DATE=? WHERE CREDIT_MEMO_NUMBER=?;'''
		edit_credit_memo_amount_sql_script = '''UPDATE vendor_credit_memos SET CREDIT_MEMO_AMOUNT=? WHERE CREDIT_MEMO_NUMBER=?;'''
		edit_credit_memo_notes_sql_script = '''UPDATE vendor_credit_memos SET CREDIT_MEMO_NOTES=? WHERE CREDIT_MEMO_NUMBER=?;'''

		retrieve_journal_entry_sql_script = '''SELECT * FROM journal_entries WHERE VENDOR_CREDIT_MEMO_NUMBER=?;'''
		edit_JE_date_sql_script = '''UPDATE journal_entries SET JOURNAL_ENTRY_DATE=? WHERE VENDOR_CREDIT_MEMO_NUMBER=?;'''
		edit_JE_debit_amount_sql_script = '''UPDATE journal_entries SET JOURNAL_ENTRY_DEBIT_AMOUNT=? WHERE VENDOR_CREDIT_MEMO_NUMBER=?'''
		edit_JE_credit_amount_sql_script = '''UPDATE journal_entries SET JOURNAL_ENTRY_CREDIT_AMOUNT=? WHERE VENDOR_CREDIT_MEMO_NUMBER=?'''
		edit_JE_notes_sql_script = '''UPDATE journal_entries SET JOURNAL_ENTRY_NOTES=? WHERE VENDOR_CREDIT_MEMO_NUMBER=?'''

		try:

			reference_credit_memo_number = self.credit_memo_number_entry_text.get()
			new_credit_memo_issue_date = self.credit_memo_issue_date_entry_text.get()
			new_credit_memo_due_date = self.credit_memo_due_date_entry_text.get()
			new_credit_memo_number = self.credit_memo_number_entry_text.get()
			new_credit_memo_liability_GL = self.credit_memo_liability_GL_entry_text.get()
			new_credit_memo_expense_GL = self.credit_memo_expense_GL_entry_text.get()
			new_credit_memo_amount = self.credit_memo_amount_entry_text.get()
			new_credit_memo_notes = self.credit_memo_notes_entry_text.get()

			if new_credit_memo_issue_date == "":

				submit_changes_error_message_1 = tk.messagebox.showinfo(title="Edit Vendor Credit Memo",message="Please enter credit memo issue date.")

			elif new_credit_memo_due_date == "":

				submit_changes_error_message_2 = tk.messagebox.showinfo(title="Edit Vendor Credit Memo",message="Please enter credit memo due date.")

			elif new_credit_memo_number  == "":

				submit_changes_error_message_3 = tk.messagebox.showinfo(title="Edit Vendor Credit Memo",message="Please enter credit memo number.")

			elif new_credit_memo_liability_GL == "":

				submit_changes_error_message_4 = tk.messagebox.showinfo(title="Edit Vendor Credit Memo",message="Please enter credit memo liability GL.")

			elif new_credit_memo_expense_GL == "":

				submit_changes_error_message_5 = tk.messagebox.showinfo(title="Edit Vendor Credit Memo",message="Please enter credit memo expense GL.")

			elif new_credit_memo_amount == "":

				submit_changes_error_message_6 = tk.messagebox.showinfo(title="Edit Vendor Credit Memo",message="Please enter credit memo amount.")

			else:

				with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

					cursor = connection.cursor()

					cursor.execute(edit_credit_memo_issue_date_sql_script,(new_credit_memo_issue_date,reference_credit_memo_number))
					cursor.execute(edit_credit_memo_due_date_sql_script,(new_credit_memo_due_date,reference_credit_memo_number))
					cursor.execute(edit_credit_memo_amount_sql_script,(new_credit_memo_amount,reference_credit_memo_number))
					cursor.execute(edit_credit_memo_notes_sql_script,(new_credit_memo_notes,reference_credit_memo_number))

					cursor.execute(edit_JE_date_sql_script,(new_credit_memo_issue_date,reference_credit_memo_number))
					cursor.execute(edit_JE_debit_amount_sql_script,(new_credit_memo_amount,reference_credit_memo_number))
					cursor.execute(edit_JE_credit_amount_sql_script,(new_credit_memo_amount,reference_credit_memo_number))
					cursor.execute(edit_JE_notes_sql_script,(new_credit_memo_notes,reference_credit_memo_number))

					connection.commit()

					cursor.close()

					edit_credit_memo_confirmation_message = tk.messagebox.showinfo("Edit Vendor Credit Memo",message="Credit Memo successfully edited.")

		except Exception as error:

			edit_credit_memo_error_message_2 = tk.messagebox.showinfo(title="Edit Vendor Credit Memo",message=f"{error}")


	def cancel_changes(self):

		try:

			self.credit_memo_issue_date_entry_text.set("")
			self.credit_memo_due_date_entry_text.set("")
			self.credit_memo_number_entry_text.set("")
			self.credit_memo_liability_GL_entry_text.set("")
			self.credit_memo_expense_GL_entry_text.set("")
			self.credit_memo_amount_entry_text.set("")
			self.credit_memo_notes_entry_text.set("")

		except Exception as error:

			cancel_changes_error_message_1 = tk.messagebox.showinfo(title="Edit Vendor Credit Memo",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
