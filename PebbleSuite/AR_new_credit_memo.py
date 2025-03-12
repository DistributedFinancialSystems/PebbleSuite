"""
[ ]
[ ]
[ ]
[ ]	AR_new_credit_memo.py
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




class NEW_CLIENT_CREDIT_MEMO_ENTRY:

	def __init__(self,new_credit_memo_entry):

		self.new_credit_memo_entry = new_credit_memo_entry

	def enter_credit_memo(self):

		new_credit_memo_sql_script = '''INSERT INTO client_credit_memos(
					CREDIT_MEMO_NAME,
					CREDIT_MEMO_ISSUE_DATE,
					CREDIT_MEMO_DUE_DATE,
					CREDIT_MEMO_NUMBER,
					CREDIT_MEMO_LIABILITY_ACCOUNT,
					CREDIT_MEMO_EXPENSE_ACCOUNT,
					CREDIT_MEMO_AMOUNT,
					CREDIT_MEMO_NOTES)
					VALUES(?,?,?,?,?,?,?,?);'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(new_credit_memo_sql_script,self.new_credit_memo_entry)
			connection.commit()
			cursor.close()




class NEW_JOURNAL_ENTRY:

	"""
	[ ]
	[ ]
	[ ]
	[ ]	INITIALIZE CLASS VARIABLES:
	[ ]
	[ ]
	[ ]
	"""

	def __init__(self,new_journal_entry):
		self.new_journal_entry = new_journal_entry

	"""
	[ ]
	[ ]
	[ ]
	[ ]	DEBIT_ENTRY FUNCTION:
	[ ]
	[ ]
	[ ]
	"""

	def debit_entry(self):

		new_debit_JE_sql_script = '''INSERT INTO journal_entries(
						JOURNAL_ENTRY_TIMESTAMP,
						JOURNAL_ENTRY_NUMBER,
						JOURNAL_ENTRY_DATE,
						CLIENT_CREDIT_MEMO_NUMBER,
						GENERAL_LEDGER_NAME,
						GENERAL_LEDGER_NUMBER,
						GENERAL_LEDGER_TYPE,
						OFFSET_GENERAL_LEDGER_NAME,
						OFFSET_GENERAL_LEDGER_NUMBER,
						OFFSET_GENERAL_LEDGER_TYPE,
						JOURNAL_ENTRY_DEBIT_AMOUNT,
						JOURNAL_ENTRY_CREDIT_AMOUNT,
						JOURNAL_ENTRY_NAME,
						JOURNAL_ENTRY_NOTES)
						VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''

		with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

			try:

				cursor = connection.cursor()
				cursor.execute(new_debit_JE_sql_script,self.new_journal_entry)
				connection.commit()
				cursor.close()

			except sqlite3.Error as error:

				debit_entry_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")

	"""
	[ ]
	[ ]
	[ ]
	[ ]	CREDIT_ENTRY FUNCTION:
	[ ]
	[ ]
	[ ]
	"""

	def credit_entry(self):

		new_credit_JE_sql_script = '''INSERT INTO journal_entries(
						JOURNAL_ENTRY_TIMESTAMP,
						JOURNAL_ENTRY_NUMBER,
						JOURNAL_ENTRY_DATE,
						CLIENT_CREDIT_MEMO_NUMBER,
						GENERAL_LEDGER_NAME,
						GENERAL_LEDGER_NUMBER,
						GENERAL_LEDGER_TYPE,
						OFFSET_GENERAL_LEDGER_NAME,
						OFFSET_GENERAL_LEDGER_NUMBER,
						OFFSET_GENERAL_LEDGER_TYPE,
						JOURNAL_ENTRY_DEBIT_AMOUNT,
						JOURNAL_ENTRY_CREDIT_AMOUNT,
						JOURNAL_ENTRY_NAME,
						JOURNAL_ENTRY_NOTES)
						VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''

		with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

			try:

				cursor = connection.cursor()
				cursor.execute(new_credit_JE_sql_script,self.new_journal_entry)
				connection.commit()
				cursor.close()

			except sqlite3.Error as error:

				credit_entry_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")

"""
[ ]
[ ]
[ ]
[ ]	NEW_CREDIT_MEMO_WINDOW
[ ]
[ ]
[ ]
"""

class NEW_CLIENT_CREDIT_MEMO_WINDOW(tk.Toplevel):

	#Define SQL.db scripts:
	client_sql_script = '''SELECT CLIENT_NAME FROM clients;'''
	liability_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers WHERE GENERAL_LEDGER_TYPE="Liability";'''
	expense_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers WHERE GENERAL_LEDGER_TYPE="Expense";'''


	#Define class variables:
	alive = False


	#Define __init__ tkinter widgets:
	def __init__(self,*args,**kwargs):


		#Retrieve client data from SQL.db:
		options = ["Select client"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(self.client_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()
			cursor.close()


		#Retrieve liability GL data from SQL.db:
		liability_GL_options = ["Select Liability GL"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(self.liability_GL_sql_script)

			for item in cursor:

				liability_GL_options.append(" ".join(item))

			connection.commit()
			cursor.close()


		#Retrieve expense GL data from SQL.db:
		expense_GL_options = ["Select Expense GL"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(self.expense_GL_sql_script)

			for item in cursor:

				expense_GL_options.append(" ".join(item))

			connection.commit()
			cursor.close()


		#Define class tkinter widgets:
		super().__init__(*args,**kwargs)
		self.config(width=390,height=380)
		self.title("New Credit Memo")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set("Select Client")

		self.client_name_label = ttk.Label(self,text="Select Client:")
		self.client_name_label.place(x=20,y=20)
		self.client_option_menu = ttk.OptionMenu(self,self.clicked,options[0],*options)
		self.client_option_menu.place(x=200,y=20)

		self.client_credit_memo_issue_date_label = ttk.Label(self,text="Credit Memo Issue Date:")
		self.client_credit_memo_issue_date_label.place(x=20,y=60)
		self.client_credit_memo_issue_date_entry = ttk.Entry(self)
		self.client_credit_memo_issue_date_entry.place(x=200,y=60)

		self.client_credit_memo_due_date_label = ttk.Label(self,text="Credit Memo Due Date:")
		self.client_credit_memo_due_date_label.place(x=20,y=100)
		self.client_credit_memo_due_date_entry = ttk.Entry(self)
		self.client_credit_memo_due_date_entry.place(x=200,y=100)

		self.client_credit_memo_number_label = ttk.Label(self,text="Credit Memo Number:")
		self.client_credit_memo_number_label.place(x=20,y=140)
		self.client_credit_memo_number_entry = ttk.Entry(self)
		self.client_credit_memo_number_entry.place(x=200,y=140)

		self.liability_GL_label = ttk.Label(self,text="Credit Memo liability GL:")
		self.liability_GL_label.place(x=20,y=180)
		self.liability_GL_text = tk.StringVar()
		self.liability_GL_text.set("Select Liability GL")
		self.liability_GL_option_menu = ttk.OptionMenu(self,self.liability_GL_text,liability_GL_options[0],*liability_GL_options)
		self.liability_GL_option_menu.place(x=200,y=180)

		self.expense_GL_label = tk.Label(self,text="Credit Memo Expense GL:")
		self.expense_GL_label.place(x=20,y=220)
		self.expense_GL_text = tk.StringVar()
		self.expense_GL_text.set("Select Expense GL")
		self.expense_GL_option_menu = ttk.OptionMenu(self,self.expense_GL_text,expense_GL_options[0],*expense_GL_options)
		self.expense_GL_option_menu.place(x=200,y=220)

		self.client_credit_memo_amount_label = ttk.Label(self,text="Credit Memo Amount:")
		self.client_credit_memo_amount_label.place(x=20,y=260)
		self.client_credit_memo_amount_entry = ttk.Entry(self)
		self.client_credit_memo_amount_entry.place(x=200,y=260)

		self.client_credit_memo_notes_label = ttk.Label(self,text="Credit Memo Notes:")
		self.client_credit_memo_notes_label.place(x=20,y=300)
		self.client_credit_memo_notes_entry = ttk.Entry(self)
		self.client_credit_memo_notes_entry.place(x=200,y=300)

		self.enter_credit_memo_button = ttk.Button(self,text="Enter Credit Memos",command=self.create_new_credit_memo)
		self.enter_credit_memo_button.place(x=200,y=340)

		self.credit_memo_report_button = ttk.Button(self,text="Print Credit Memos",command=self.credit_memo_report)
		self.credit_memo_report_button.place(x=20,y=340)

	"""
	[ ]
	[ ]
	[ ]
	[ ]	create_new_credit_memo function:
	[ ]
	[ ]
	[ ]
	"""

	def create_new_credit_memo(self):

		#Select client error messages:
		if self.clicked.get() == "Select Client":

			select_client_error_message_1 = tk.messagebox.showinfo(title="Error",message="Select a client for new credit memo.")

		#credit_memo issue date error messages:
		elif self.client_credit_memo_issue_date_entry.get() == "":

			credit_memo_issue_date_error_message_1 = tk.messagebox.showinfo(title="Error",message="Issue date cannot be blank.")

		#credit_memo due date error messges:
		elif self.client_credit_memo_due_date_entry.get() == "":

			credit_memo_due_date_error_message_1 = tk.messagebox.showinfo(title="Error",message="Due date cannot be blank.")

		#credit_memo number errorm messages:
		elif self.client_credit_memo_number_entry.get() == "":

			credit_memo_number_entry_error_message_1 = tk.messagebox.showinfo(title="Error",message="credit_memo number cannot be blank.")

		#credit_memo liability GL error messages:
		elif self.liability_GL_text.get() == "Select Liability GL":

			liability_GL_error_message_1 = tk.messagebox.showinfo(title="Error",message="Select a liability GL.")

		#credit_memo expense GL error messages:
		elif self.expense_GL_text.get() == "Select Expense GL":

			expense_GL_error_message_1 = tk.messagebox.showinfo(title="Error",message="Select an expense GL.")

		#credit_memo amount error messages:
		elif self.client_credit_memo_amount_entry.get() == "":

			credit_memo_amount_entry_error_message_1 = tk.messagebox.showinfo(title="Error",message="credit_memo amount cannot be blank.")

		else:

			#Enter credit_memo data using NEW_credit_memo_ENTRY class (from above):
			new_credit_memo_data = []

			new_credit_memo_name = self.clicked.get()
			new_credit_memo_issue_date = self.client_credit_memo_issue_date_entry.get()
			new_credit_memo_due_date = self.client_credit_memo_due_date_entry.get()
			new_credit_memo_number = self.client_credit_memo_number_entry.get()
			new_liability_GL = self.liability_GL_text.get()
			new_expense_GL = self.expense_GL_text.get()
			new_credit_memo_amount = self.client_credit_memo_amount_entry.get()
			new_credit_memo_notes = self.client_credit_memo_notes_entry.get()

			new_credit_memo_data.append(new_credit_memo_name)
			new_credit_memo_data.append(new_credit_memo_issue_date)
			new_credit_memo_data.append(new_credit_memo_due_date)
			new_credit_memo_data.append(new_credit_memo_number)
			new_credit_memo_data.append(new_liability_GL)
			new_credit_memo_data.append(new_expense_GL)
			new_credit_memo_data.append(new_credit_memo_amount)
			new_credit_memo_data.append(new_credit_memo_notes)

			new_credit_memo = NEW_CLIENT_CREDIT_MEMO_ENTRY(new_credit_memo_data)
			new_credit_memo.enter_credit_memo()


			#NEW_JOURNAL_ENTRY admin variables:

			journal_entry_timestamp = datetime.datetime.now()


			#Enter debit data using NEW_JOURNAL_ENTRY class (from above):
			new_debit_data = []

			new_journal_entry_timestamp = journal_entry_timestamp
			new_journal_entry_number = 0
			new_journal_entry_date = self.client_credit_memo_issue_date_entry.get()
			new_credit_memo_number = self.client_credit_memo_number_entry.get()
			new_general_ledger_name = self.expense_GL_text.get()
			new_general_ledger_number = "INSERT GENERAL LEDGER NUMBER"
			new_general_ledger_type = "Expense"
			new_offset_general_ledger_name = self.liability_GL_text.get()
			new_offset_general_ledger_number = "INSERT GENERAL LEDGER NUMBER"
			new_offset_general_ledger_type = "Liability"
			new_journal_entry_debit_amount = self.client_credit_memo_amount_entry.get()
			new_journal_entry_credit_amount = 0
			new_journal_entry_name = self.clicked.get()
			new_journal_entry_notes = self.client_credit_memo_notes_entry.get()

			new_debit_data.append(new_journal_entry_timestamp)
			new_debit_data.append(new_journal_entry_number)
			new_debit_data.append(new_journal_entry_date)
			new_debit_data.append(new_credit_memo_number)
			new_debit_data.append(new_general_ledger_name)
			new_debit_data.append(new_general_ledger_number)
			new_debit_data.append(new_general_ledger_type)
			new_debit_data.append(new_offset_general_ledger_name)
			new_debit_data.append(new_offset_general_ledger_number)
			new_debit_data.append(new_offset_general_ledger_type)
			new_debit_data.append(new_journal_entry_debit_amount)
			new_debit_data.append(new_journal_entry_credit_amount)
			new_debit_data.append(new_journal_entry_name)
			new_debit_data.append(new_journal_entry_notes)

			debit_entry = NEW_JOURNAL_ENTRY(new_debit_data)
			debit_entry.debit_entry()


			#Enter credit data using NEW_JOURNAL_ENTRY class (from above):
			new_credit_data = []

			new_journal_entry_timestamp = journal_entry_timestamp
			new_journal_entry_number = 0
			new_journal_entry_date = self.client_credit_memo_issue_date_entry.get()
			new_credit_memo_number = self.client_credit_memo_number_entry.get()
			new_general_ledger_name = self.liability_GL_text.get()
			new_general_ledger_number = "INSERT GENERAL LEDGER NUMBER"
			new_general_ledger_type = "Liability"
			new_offset_general_ledger_name = self.expense_GL_text.get()
			new_offset_general_ledger_number = "INSERT GENERAL LEDGER NUMBER"
			new_offset_general_ledger_type = "Expense"
			new_journal_entry_debit_amount = 0
			new_journal_entry_credit_amount = self.client_credit_memo_amount_entry.get()
			new_journal_entry_name = self.clicked.get()
			new_journal_entry_notes = self.client_credit_memo_notes_entry.get()

			new_credit_data.append(new_journal_entry_timestamp)
			new_credit_data.append(new_journal_entry_number)
			new_credit_data.append(new_journal_entry_date)
			new_credit_data.append(new_credit_memo_number)
			new_credit_data.append(new_general_ledger_name)
			new_credit_data.append(new_general_ledger_number)
			new_credit_data.append(new_general_ledger_type)
			new_credit_data.append(new_offset_general_ledger_name)
			new_credit_data.append(new_offset_general_ledger_number)
			new_credit_data.append(new_offset_general_ledger_type)
			new_credit_data.append(new_journal_entry_debit_amount)
			new_credit_data.append(new_journal_entry_credit_amount)
			new_credit_data.append(new_journal_entry_name)
			new_credit_data.append(new_journal_entry_notes)

			credit_entry = NEW_JOURNAL_ENTRY(new_credit_data)
			credit_entry.credit_entry()

			confirmation_message = tk.messagebox.showinfo(title="New Credit Memo",message="New Credit Memo Created.")

	"""
	[ ]
	[ ]
	[ ]
	[ ]	credit_memo_report function:
	[ ]
	[ ]
	[ ]
	"""

	def credit_memo_report(self):

		credit_memo_report_sql_script = '''SELECT * FROM client_credit_memos;'''

		try:
			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()
				cursor.execute(credit_memo_report_sql_script)

				for item in cursor:
					print(item)

				connection.commit()

				cursor.close()

		except sqlite3.Error as error:

			print(error)

	"""
	[ ]
	[ ]
	[ ]
	[ ]	destroy function:
	[ ]
	[ ]
	[ ]
	"""

	def destroy(self):
		self.__class__.alive = False
		return super().destroy()
