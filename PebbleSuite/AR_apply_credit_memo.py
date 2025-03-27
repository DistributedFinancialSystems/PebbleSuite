"""
[ ]
[ ]
[ ]
[ ]	AR_apply_credit_memo.py
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




class PAY_CREDIT_MEMO_UPDATE_STATUS:

	def __init__(self,pay_credit_memo_status):

		self.pay_credit_memo_status = pay_credit_memo_status

	def pay_credit_memo(self):

		credit_memo_payment_status_sql_script = '''UPDATE client_credit_memos SET CREDIT_MEMO_STATUS="Paid" WHERE CREDIT_MEMO_NAME=? AND CREDIT_MEMO_NUMBER=?;'''

		with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

			cursor = connection.cursor()
			cursor.execute(credit_memo_payment_status_sql_script,self.pay_credit_memo_status)
			connection.commit()
			cursor.close()




class PAY_CREDIT_MEMO_UPDATE_PAYMENT_DATE:

	def __init__(self,pay_credit_memo_date):

		self.pay_credit_memo_date = pay_credit_memo_date

	def pay_credit_memo(self):

		credit_memo_payment_date_sql_script = '''UPDATE client_credit_memos SET CREDIT_MEMO_PAID_DATE=? WHERE CREDIT_MEMO_NAME=? AND CREDIT_MEMO_NUMBER=?;'''

		with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

			cursor = connection.cursor()
			cursor.execute(credit_memo_payment_date_sql_script,self.pay_credit_memo_date)
			connection.commit()
			cursor.close()




class PAY_CREDIT_MEMO_JOURNAL_ENTRY:

	def __init__(self,pay_credit_memo_entry):

		self.pay_credit_memo_entry = pay_credit_memo_entry

	def pay_credit_memo(self):

		new_payment_JE_sql_script = '''INSERT INTO journal_entries(
						JOURNAL_ENTRY_TIMESTAMP,
						JOURNAL_ENTRY_NUMBER,
						JOURNAL_ENTRY_DATE,
						CLIENT_CREDIT_MEMO_NUMBER,
						DEBIT_GENERAL_LEDGER_NAME,
						DEBIT_GENERAL_LEDGER_NUMBER,
						DEBIT_GENERAL_LEDGER_TYPE,
						CREDIT_GENERAL_LEDGER_NAME,
						CREDIT_GENERAL_LEDGER_NUMBER,
						CREDIT_GENERAL_LEDGER_TYPE,
						JOURNAL_ENTRY_DEBIT_AMOUNT,
						JOURNAL_ENTRY_CREDIT_AMOUNT,
						JOURNAL_ENTRY_CLIENT_NAME,
						JOURNAL_ENTRY_NOTES)
						VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''

		with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

			cursor = connection.cursor()
			cursor.execute(new_payment_JE_sql_script,self.pay_credit_memo_entry)
			connection.commit()
			cursor.close()




class AR_PAY_CREDIT_MEMO_WINDOW(tk.Toplevel):

	#Define class variables
	alive = False

	client_sql_script = '''SELECT CLIENT_NAME FROM clients;'''

	asset_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME from general_ledgers WHERE GENERAL_LEDGER_TYPE="Asset - Bank Account";'''


	#Define class functions
	def __init__(self,*args,**kwargs):

		options = ["Select Client"]

		payment_GL_options = ["Select Bank Account"]


		#Retrieve client names from SQL.db, add them into options list:
		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(self.client_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()
			cursor.close()

		#Retrieve asset general ledger names from SQL.db, add them into payment_GL_options list:
		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(self.asset_GL_sql_script)

			for item in cursor:

				payment_GL_options.append(" ".join(item))

			connection.commit()
			cursor.close()


		#Define class tkinter widgets:
		super().__init__(*args,**kwargs)
		self.config(width=600,height=775)
		self.title("Pay Client Credit Memo")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.credit_memo_name_label = ttk.Label(self,text="Client Name")
		self.credit_memo_name_label.place(x=20,y=15)


		#Search for client names in SQL.db.
		#Insert client names into client search listbox widget.
		self.select_client_scrollbar = ttk.Scrollbar(self)
		self.select_client_scrollbar.place(x=353,y=45,width=20,height=200)
		self.select_client_listbox = tk.Listbox(self,yscrollcommand=self.select_client_scrollbar.set)
		self.select_client_listbox.place(x=20,y=45,width=333,height=200)
		self.select_client_scrollbar.config(command=self.select_client_listbox.yview)


		search_client_name_sql_script = '''SELECT CLIENT_NAME FROM clients;'''


		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(search_client_name_sql_script)
			connection.commit()

			for item in cursor:

				self.select_client_listbox.insert(0," ".join(item))

			cursor.close()


		#Credit Memo selection listbox widget:
		self.scrollbar = ttk.Scrollbar(self)
		self.scrollbar.place(x=353,y=300,width=20,height=405)
		self.listbox = tk.Listbox(self,yscrollcommand=self.scrollbar.set)
		self.listbox.place(x=20,y=300,width=333,height=405)
		self.scrollbar.config(command=self.listbox.yview)

		self.search_credit_memos_button = ttk.Button(self,text="Search Credit Memos",command=self.search_credit_memos)
		self.search_credit_memos_button.place(x=20,y=255)

		self.clear_credit_memos_button = ttk.Button(self,text="Clear All Credit Memos",command=self.clear_credit_memos)
		self.clear_credit_memos_button.place(x=160,y=725)

		self.pay_credit_memo_button = ttk.Button(self,text="Select Credit Memo",command=self.select_credit_memo)
		self.pay_credit_memo_button.place(x=20,y=725)

		self.credit_memo_name_label = ttk.Label(self,text="Client Credit Memo Name")
		self.credit_memo_name_label.place(x=400,y=15)
		self.credit_memo_name_entry_text = tk.StringVar()
		self.credit_memo_name_entry = ttk.Entry(self,textvariable=self.credit_memo_name_entry_text,state=tk.DISABLED)
		self.credit_memo_name_entry.place(x=400,y=45)

		self.credit_memo_issue_date_label = ttk.Label(self,text="Credit Memo Issue Date:")
		self.credit_memo_issue_date_label.place(x=400,y=85)
		self.credit_memo_issue_date_entry_text = tk.StringVar()
		self.credit_memo_issue_date_entry = ttk.Entry(self,textvariable=self.credit_memo_issue_date_entry_text,state=tk.DISABLED)
		self.credit_memo_issue_date_entry.place(x=400,y=115)

		self.credit_memo_due_date_label = ttk.Label(self,text="Credit Memo Due Date:")
		self.credit_memo_due_date_label.place(x=400,y=155)
		self.credit_memo_due_date_entry_text = tk.StringVar()
		self.credit_memo_due_date_entry = ttk.Entry(self,textvariable=self.credit_memo_due_date_entry_text,state=tk.DISABLED)
		self.credit_memo_due_date_entry.place(x=400,y=185)

		self.credit_memo_number_label = ttk.Label(self,text="Credit Memo Number:")
		self.credit_memo_number_label.place(x=400,y=225)
		self.credit_memo_number_entry_text = tk.StringVar()
		self.credit_memo_number_entry = ttk.Entry(self,textvariable=self.credit_memo_number_entry_text,state=tk.DISABLED)
		self.credit_memo_number_entry.place(x=400,y=255)

		self.credit_memo_asset_GL_label = ttk.Label(self,text="Credit Memo Asset GL:")
		self.credit_memo_asset_GL_label.place(x=400,y=295)
		self.credit_memo_asset_GL_entry_text = tk.StringVar()
		self.credit_memo_asset_GL_entry = ttk.Entry(self,textvariable=self.credit_memo_asset_GL_entry_text,state=tk.DISABLED)
		self.credit_memo_asset_GL_entry.place(x=400,y=325)

		self.credit_memo_expense_GL_label = ttk.Label(self,text="Credit Memo Expense GL:")
		self.credit_memo_expense_GL_label.place(x=400,y=365)
		self.credit_memo_expense_GL_entry_text = tk.StringVar()
		self.credit_memo_expense_GL_entry = ttk.Entry(self,textvariable=self.credit_memo_expense_GL_entry_text,state=tk.DISABLED)
		self.credit_memo_expense_GL_entry.place(x=400,y=395)

		self.credit_memo_amount_label = ttk.Label(self,text="Credit Memo Amount:")
		self.credit_memo_amount_label.place(x=400,y=435)
		self.credit_memo_amount_entry_text = tk.StringVar()
		self.credit_memo_amount_entry = ttk.Entry(self,textvariable=self.credit_memo_amount_entry_text,state=tk.DISABLED)
		self.credit_memo_amount_entry.place(x=400,y=465)

		self.credit_memo_notes_label = ttk.Label(self,text="Credit Memo Notes:")
		self.credit_memo_notes_label.place(x=400,y=505)
		self.credit_memo_notes_entry_text = tk.StringVar()
		self.credit_memo_notes_entry = ttk.Entry(self,textvariable=self.credit_memo_notes_entry_text,state=tk.DISABLED)
		self.credit_memo_notes_entry.place(x=400,y=535)

		self.pay_credit_memo_date_label = ttk.Label(self,text="Payment Date:")
		self.pay_credit_memo_date_label.place(x=400,y=575)
		self.pay_credit_memo_date_entry_text = tk.StringVar()
		self.pay_credit_memo_date_entry = ttk.Entry(self,textvariable=self.pay_credit_memo_date_entry_text)
		self.pay_credit_memo_date_entry.place(x=400,y=605)

		self.pay_credit_memo_payment_account_label = ttk.Label(self,text="Payment Account")
		self.pay_credit_memo_payment_account_label.place(x=400,y=645)
		self.pay_credit_memo_payment_account_text = tk.StringVar()
		self.pay_credit_memo_payment_account_text.set(f"{payment_GL_options[0]}")
		self.pay_credit_memo_payment_account_option_menu = ttk.OptionMenu(self,self.pay_credit_memo_payment_account_text,payment_GL_options[0],*payment_GL_options)
		self.pay_credit_memo_payment_account_option_menu.place(x=400,y=675)

		self.cancel_credit_memo_changes_button = ttk.Button(self,text="Cancel",command=self.cancel_changes)
		self.cancel_credit_memo_changes_button.place(x=490,y=725)

		self.submit_credit_memo_changes_button = ttk.Button(self,text="Submit",command=self.submit_payment)
		self.submit_credit_memo_changes_button.place(x=400,y=725)


	def search_credit_memos(self):

		search_client_sql_script = '''SELECT CREDIT_MEMO_NUMBER FROM client_credit_memos WHERE CREDIT_MEMO_NAME=? AND CREDIT_MEMO_STATUS=?;'''

		for item in self.select_client_listbox.curselection():

			select_client = self.select_client_listbox.get(item)

		credit_memo_status = "Open"

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()
				cursor.execute(search_client_sql_script,(select_client,credit_memo_status))

				for item in cursor:

					self.listbox.insert(0,item)

				connection.commit()
				cursor.close()

		except sqlite3.Error as error:

			search_credit_memos_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")


	def clear_credit_memos(self):

		self.listbox.delete(0,tk.END)


	def select_credit_memo(self):

		#Define SQL.db scripts:
		query_credit_memo_sql_script = '''SELECT * FROM client_credit_memos WHERE CREDIT_MEMO_NUMBER=?;'''

		for item in self.listbox.curselection():

			select_credit_memo = self.listbox.get(item)

		#select_client = self.select_client_listbox.get(item)

		try:

			with sqlite3.connect("SQL.db") as connection:

				collect = []

				cursor = connection.cursor()
				cursor.execute(query_credit_memo_sql_script,select_credit_memo)

				for item in cursor:
					collect.append(item)

				self.credit_memo_name_entry_text.set(f"{collect[0][0]}")
				self.credit_memo_issue_date_entry_text.set(f"{collect[0][1]}")
				self.credit_memo_due_date_entry_text.set(f"{collect[0][2]}")
				self.credit_memo_number_entry_text.set(f"{collect[0][3]}")
				self.credit_memo_asset_GL_entry_text.set(f"{collect[0][4]}")
				self.credit_memo_expense_GL_entry_text.set(f"{collect[0][5]}")
				self.credit_memo_amount_entry_text.set(f"{collect[0][6]}")
				self.credit_memo_notes_entry_text.set(f"{collect[0][7]}")

				connection.commit()
				cursor.close()

		except sqlite3.Error as error:

			pay_credit_memo_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")


	def submit_payment(self):

		#Define update credit memo status variables:
		pay_credit_memo_update_status_data = []
		pay_credit_memo_update_payment_data = []
		pay_credit_memo_journal_entry_data = []

		reference_client_name = self.credit_memo_name_entry_text.get()
		reference_credit_memo_number = self.credit_memo_number_entry_text.get()
		reference_credit_memo_paid_date = self.pay_credit_memo_date_entry_text.get()

		#Define journal entry variables:
		reference_JE_timestamp = datetime.datetime.now()
		reference_JE_number = None
		reference_JE_entry_date = self.pay_credit_memo_date_entry_text.get()
		reference_client_credit_memo_number = self.credit_memo_number_entry_text.get()
		reference_debit_GL_name = self.credit_memo_asset_GL_entry_text.get()
		reference_debit_GL_number = None
		reference_debit_GL_type = None
		reference_credit_GL_name = self.pay_credit_memo_payment_account_text.get()
		reference_credit_GL_number = None
		reference_credit_GL_type = None
		reference_debit_GL_amount = self.credit_memo_amount_entry_text.get()
		reference_credit_GL_amount = self.credit_memo_amount_entry_text.get()
		reference_JE_client_name = self.credit_memo_name_entry_text.get()
		reference_JE_notes = self.credit_memo_notes_entry_text.get()

		try:

			pay_credit_memo_update_status_data.append(reference_client_name)
			pay_credit_memo_update_status_data.append(reference_credit_memo_number)

		except:

			print("Error:  could not add data into pay_credit_memo_update_status_data list.")


		#Update client credit memo data:

		try:

			#PAY_CREDIT_MEMO_UPDATE_STATUS class (from above):

			update_payment_status = PAY_CREDIT_MEMO_UPDATE_STATUS(pay_credit_memo_update_status_data)
			update_payment_status.pay_credit_memo()

		except sqlite3.Error as error:

			update_payment_status_error_message = tk.messagebox.showinfo(title="Pay Client Credit Memo",message=f"Credit Memo Status Error:  {error}")


		#Update client payment date data:

		try:

			pay_credit_memo_update_payment_data.append(reference_credit_memo_paid_date)
			pay_credit_memo_update_payment_data.append(reference_client_name)
			pay_credit_memo_update_payment_data.append(reference_credit_memo_number)

		except:

			print("Error:  could not add data into pay_credit_memo_update_payment_data list.")

		try:

			update_payment_date = PAY_CREDIT_MEMO_UPDATE_PAYMENT_DATE(pay_credit_memo_update_payment_data)
			update_payment_date.pay_credit_memo()

		except sqlite3.Error as error:

			update_payment_date_error_message = tk.messagebox.showinfo(title="Pay Client Credit Memo",message=f"Credit Memo Date Error:  {error}")


		#Create new journal entries:

		try:

			#Continue working here:

			pay_credit_memo_journal_entry_data.append(reference_JE_timestamp)
			pay_credit_memo_journal_entry_data.append(reference_JE_number)
			pay_credit_memo_journal_entry_data.append(reference_JE_entry_date)
			pay_credit_memo_journal_entry_data.append(reference_client_credit_memo_number)
			pay_credit_memo_journal_entry_data.append(reference_debit_GL_name)
			pay_credit_memo_journal_entry_data.append(reference_debit_GL_number)
			pay_credit_memo_journal_entry_data.append(reference_debit_GL_type)
			pay_credit_memo_journal_entry_data.append(reference_credit_GL_name)
			pay_credit_memo_journal_entry_data.append(reference_credit_GL_number)
			pay_credit_memo_journal_entry_data.append(reference_credit_GL_type)
			pay_credit_memo_journal_entry_data.append(reference_debit_GL_amount)
			pay_credit_memo_journal_entry_data.append(reference_credit_GL_amount)
			pay_credit_memo_journal_entry_data.append(reference_JE_client_name)
			pay_credit_memo_journal_entry_data.append(reference_JE_notes)

			new_credit_memo_payment_journal_entry = PAY_CREDIT_MEMO_JOURNAL_ENTRY(pay_credit_memo_journal_entry_data)
			new_credit_memo_payment_journal_entry.pay_credit_memo()
			pay_credit_memo_confirmation_message = tk.messagebox.showinfo("Pay Client Credit Memo",message="Credit Memo payment successfully recorded.")

		except sqlite3.Error as error:

			pay_credit_memo_error_message_3 = tk.messagebox.showinfo(title="Error",message=f"{error}")




	def cancel_changes(self):

		try:

			self.credit_memo_name_entry_text.set("")
			self.credit_memo_issue_date_entry_text.set("")
			self.credit_memo_due_date_entry_text.set("")
			self.credit_memo_number_entry_text.set("")
			self.credit_memo_asset_GL_entry_text.set("")
			self.credit_memo_expense_GL_entry_text.set("")
			self.credit_memo_amount_entry_text.set("")
			self.credit_memo_notes_entry_text.set("")

		except:

			cancel_changes_error_message = tk.messagebox.showinfo(title="Error",message="Unable to clear data entries.")


	def destroy(self):
		self.__class__.alive = False
		return super().destroy()
