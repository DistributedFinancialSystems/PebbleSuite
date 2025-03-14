"""
[ ]
[ ]
[ ]
[ ]	AP_new_credit_memo.py
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




class NEW_VENDOR_CREDIT_MEMO_ENTRY:

	def __init__(self,new_credit_memo_entry):

		self.new_credit_memo_entry = new_credit_memo_entry

	def enter_credit_memo(self):

		new_credit_memo_sql_script = '''INSERT INTO vendor_credit_memos(
					CREDIT_MEMO_NAME,
					CREDIT_MEMO_ISSUE_DATE,
					CREDIT_MEMO_DUE_DATE,
					CREDIT_MEMO_NUMBER,
					CREDIT_MEMO_ASSET_ACCOUNT,
					CREDIT_MEMO_INCOME_ACCOUNT,
					CREDIT_MEMO_AMOUNT,
					CREDIT_MEMO_NOTES,
					CREDIT_MEMO_STATUS)
					VALUES(?,?,?,?,?,?,?,?,?);'''

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
						VENDOR_CREDIT_MEMO_NUMBER,
						GENERAL_LEDGER_NAME,
						GENERAL_LEDGER_NUMBER,
						GENERAL_LEDGER_TYPE,
						OFFSET_GENERAL_LEDGER_NAME,
						OFFSET_GENERAL_LEDGER_NUMBER,
						OFFSET_GENERAL_LEDGER_TYPE,
						JOURNAL_ENTRY_DEBIT_AMOUNT,
						JOURNAL_ENTRY_CREDIT_AMOUNT,
						JOURNAL_ENTRY_VENDOR_NAME,
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
						VENDOR_CREDIT_MEMO_NUMBER,
						GENERAL_LEDGER_NAME,
						GENERAL_LEDGER_NUMBER,
						GENERAL_LEDGER_TYPE,
						OFFSET_GENERAL_LEDGER_NAME,
						OFFSET_GENERAL_LEDGER_NUMBER,
						OFFSET_GENERAL_LEDGER_TYPE,
						JOURNAL_ENTRY_DEBIT_AMOUNT,
						JOURNAL_ENTRY_CREDIT_AMOUNT,
						JOURNAL_ENTRY_VENDOR_NAME,
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

class NEW_VENDOR_CREDIT_MEMO_WINDOW(tk.Toplevel):

	#Define SQL.db scripts:
	vendor_sql_script = '''SELECT VENDOR_NAME FROM vendors;'''
	asset_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers WHERE GENERAL_LEDGER_TYPE="Asset";'''
	income_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers WHERE GENERAL_LEDGER_TYPE="Income";'''


	#Define class variables:
	alive = False


	#Define __init__ tkinter widgets:
	def __init__(self,*args,**kwargs):


		#Retrieve Vendor data from SQL.db:
		options = ["Select Vendor"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(self.vendor_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()
			cursor.close()


		#Retrieve asset GL data from SQL.db:
		asset_GL_options = ["Select Asset GL"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(self.asset_GL_sql_script)

			for item in cursor:

				asset_GL_options.append(" ".join(item))

			connection.commit()
			cursor.close()


		#Retrieve income GL data from SQL.db:
		income_GL_options = ["Select Income GL"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(self.income_GL_sql_script)

			for item in cursor:

				income_GL_options.append(" ".join(item))

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
		self.clicked.set("Select Vendor")

		self.vendor_name_label = ttk.Label(self,text="Select Vendor:")
		self.vendor_name_label.place(x=20,y=20)
		self.vendor_option_menu = ttk.OptionMenu(self,self.clicked,options[0],*options)
		self.vendor_option_menu.place(x=200,y=20)

		self.vendor_credit_memo_issue_date_label = ttk.Label(self,text="Credit Memo Issue Date:")
		self.vendor_credit_memo_issue_date_label.place(x=20,y=60)
		self.vendor_credit_memo_issue_date_entry = ttk.Entry(self)
		self.vendor_credit_memo_issue_date_entry.place(x=200,y=60)

		self.vendor_credit_memo_due_date_label = ttk.Label(self,text="Credit Memo Due Date:")
		self.vendor_credit_memo_due_date_label.place(x=20,y=100)
		self.vendor_credit_memo_due_date_entry = ttk.Entry(self)
		self.vendor_credit_memo_due_date_entry.place(x=200,y=100)

		self.vendor_credit_memo_number_label = ttk.Label(self,text="Credit Memo Number")
		self.vendor_credit_memo_number_label.place(x=20,y=140)
		self.vendor_credit_memo_number_entry = ttk.Entry(self)
		self.vendor_credit_memo_number_entry.place(x=200,y=140)

		self.asset_GL_label = ttk.Label(self,text="Credit Memo Asset GL:")
		self.asset_GL_label.place(x=20,y=180)
		self.asset_GL_text = tk.StringVar()
		self.asset_GL_text.set("Select Asset GL")
		self.asset_GL_option_menu = ttk.OptionMenu(self,self.asset_GL_text,asset_GL_options[0],*asset_GL_options)
		self.asset_GL_option_menu.place(x=200,y=180)

		self.income_GL_label = tk.Label(self,text="Credit Memo Income GL:")
		self.income_GL_label.place(x=20,y=220)
		self.income_GL_text = tk.StringVar()
		self.income_GL_text.set("Select Income GL")
		self.income_GL_option_menu = ttk.OptionMenu(self,self.income_GL_text,income_GL_options[0],*income_GL_options)
		self.income_GL_option_menu.place(x=200,y=220)

		self.vendor_credit_memo_amount_label = ttk.Label(self,text="Credit Memo Amount")
		self.vendor_credit_memo_amount_label.place(x=20,y=260)
		self.vendor_credit_memo_amount_entry = ttk.Entry(self)
		self.vendor_credit_memo_amount_entry.place(x=200,y=260)

		self.vendor_credit_memo_notes_label = ttk.Label(self,text="Credit Memo Notes")
		self.vendor_credit_memo_notes_label.place(x=20,y=300)
		self.vendor_credit_memo_notes_entry = ttk.Entry(self)
		self.vendor_credit_memo_notes_entry.place(x=200,y=300)

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

		#Select Vendor error messages:
		if self.clicked.get() == "Select Vendor":

			select_vendor_error_message_1 = tk.messagebox.showinfo(title="Error",message="Select a vendor for new credit memo.")

		#credit_memo issue date error messages:
		elif self.vendor_credit_memo_issue_date_entry.get() == "":

			credit_memo_issue_date_error_message_1 = tk.messagebox.showinfo(title="Error",message="Issue date cannot be blank.")

		#credit_memo due date error messges:
		elif self.vendor_credit_memo_due_date_entry.get() == "":

			credit_memo_due_date_error_message_1 = tk.messagebox.showinfo(title="Error",message="Due date cannot be blank.")

		#credit_memo number errorm messages:
		elif self.vendor_credit_memo_number_entry.get() == "":

			credit_memo_number_entry_error_message_1 = tk.messagebox.showinfo(title="Error",message="credit_memo number cannot be blank.")

		#credit_memo asset GL error messages:
		elif self.asset_GL_text.get() == "Select Asset GL":

			asset_GL_error_message_1 = tk.messagebox.showinfo(title="Error",message="Select a asset GL.")

		#credit_memo income GL error messages:
		elif self.income_GL_text.get() == "Select Income GL":

			income_GL_error_message_1 = tk.messagebox.showinfo(title="Error",message="Select an income GL.")

		#credit_memo amount error messages:
		elif self.vendor_credit_memo_amount_entry.get() == "":

			credit_memo_amount_entry_error_message_1 = tk.messagebox.showinfo(title="Error",message="credit_memo amount cannot be blank.")

		else:

			#Enter credit_memo data using NEW_credit_memo_ENTRY class (from above):
			new_credit_memo_data = []

			new_credit_memo_name = self.clicked.get()
			new_credit_memo_issue_date = self.vendor_credit_memo_issue_date_entry.get()
			new_credit_memo_due_date = self.vendor_credit_memo_due_date_entry.get()
			new_credit_memo_number = self.vendor_credit_memo_number_entry.get()
			new_asset_GL = self.asset_GL_text.get()
			new_income_GL = self.income_GL_text.get()
			new_credit_memo_amount = self.vendor_credit_memo_amount_entry.get()
			new_credit_memo_notes = self.vendor_credit_memo_notes_entry.get()
			new_credit_memo_status = "Open"

			new_credit_memo_data.append(new_credit_memo_name)
			new_credit_memo_data.append(new_credit_memo_issue_date)
			new_credit_memo_data.append(new_credit_memo_due_date)
			new_credit_memo_data.append(new_credit_memo_number)
			new_credit_memo_data.append(new_asset_GL)
			new_credit_memo_data.append(new_income_GL)
			new_credit_memo_data.append(new_credit_memo_amount)
			new_credit_memo_data.append(new_credit_memo_notes)
			new_credit_memo_data.append(new_credit_memo_status)

			new_credit_memo = NEW_VENDOR_CREDIT_MEMO_ENTRY(new_credit_memo_data)
			new_credit_memo.enter_credit_memo()


			#NEW_JOURNAL_ENTRY admin variables:

			journal_entry_timestamp = datetime.datetime.now()


			#Enter debit data using NEW_JOURNAL_ENTRY class (from above):
			new_debit_data = []

			new_journal_entry_timestamp = journal_entry_timestamp
			new_journal_entry_number = 0
			new_journal_entry_date = self.vendor_credit_memo_issue_date_entry.get()
			new_credit_memo_number = self.vendor_credit_memo_number_entry.get()
			new_general_ledger_name = self.asset_GL_text.get()
			new_general_ledger_number = "INSERT GL NUMBER"
			new_general_ledger_type = "Asset"
			new_offset_general_ledger_name = self.income_GL_text.get()
			new_offset_general_ledger_number = "INSERT GL NUMBER"
			new_offset_general_ledger_type = "Income"
			new_journal_entry_debit_amount = self.vendor_credit_memo_amount_entry.get()
			new_journal_entry_credit_amount = 0
			new_journal_entry_name = self.clicked.get()
			new_journal_entry_notes = self.vendor_credit_memo_notes_entry.get()

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
			new_journal_entry_date = self.vendor_credit_memo_issue_date_entry.get()
			new_credit_memo_number = self.vendor_credit_memo_number_entry.get()
			new_general_ledger_name = self.income_GL_text.get()
			new_general_ledger_number = "INSERT GL NUMBER"
			new_general_ledger_type = "Income"
			new_offset_general_ledger_name = self.asset_GL_text.get()
			new_offset_general_ledger_number = "INSERT GL NUMBER"
			new_offset_general_ledger_type = "Asset"
			new_journal_entry_debit_amount = 0
			new_journal_entry_credit_amount = self.vendor_credit_memo_amount_entry.get()
			new_journal_entry_name = self.clicked.get()
			new_journal_entry_notes = self.vendor_credit_memo_notes_entry.get()

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

		credit_memo_report_sql_script = '''SELECT * FROM vendor_credit_memos;'''

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
