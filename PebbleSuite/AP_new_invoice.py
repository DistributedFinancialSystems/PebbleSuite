"""
[ ]
[ ]
[ ]
[ ]	AP_new_invoice.py
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




class NEW_INVOICE_ENTRY:

	def __init__(self,new_invoice_entry):

		self.new_invoice_entry = new_invoice_entry

	def enter_invoice(self):

		new_invoice_sql_script = '''INSERT INTO vendor_invoices(
					INVOICE_NAME,
					INVOICE_ISSUE_DATE,
					INVOICE_DUE_DATE,
					INVOICE_NUMBER,
					INVOICE_LIABILITY_ACCOUNT,
					INVOICE_EXPENSE_ACCOUNT,
					INVOICE_AMOUNT,
					INVOICE_NOTES,
					INVOICE_STATUS,
					INVOICE_PAID_DATE)
					VALUES(?,?,?,?,?,?,?,?,?,?);'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(new_invoice_sql_script,self.new_invoice_entry)
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
	[ ]	JOURNAL_ENTRY FUNCTION:
	[ ]
	[ ]
	[ ]
	"""

	def journal_entry(self):

		new_JE_sql_script = '''INSERT INTO journal_entries(
					JOURNAL_ENTRY_TIMESTAMP,
					JOURNAL_ENTRY_NUMBER,
					JOURNAL_ENTRY_DATE,
					VENDOR_INVOICE_NUMBER,
					DEBIT_GENERAL_LEDGER_NAME,
					DEBIT_GENERAL_LEDGER_NUMBER,
					DEBIT_GENERAL_LEDGER_TYPE,
					CREDIT_GENERAL_LEDGER_NAME,
					CREDIT_GENERAL_LEDGER_NUMBER,
					CREDIT_GENERAL_LEDGER_TYPE,
					JOURNAL_ENTRY_DEBIT_AMOUNT,
					JOURNAL_ENTRY_CREDIT_AMOUNT,
					JOURNAL_ENTRY_VENDOR_NAME,
					JOURNAL_ENTRY_NOTES)
					VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''

		with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

			try:

				cursor = connection.cursor()
				cursor.execute(new_JE_sql_script,self.new_journal_entry)
				connection.commit()
				cursor.close()

			except sqlite3.Error as error:

				journal_entry_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")




class NEW_INVOICE_WINDOW(tk.Toplevel):

	#Define SQL.db scripts:
	vendor_sql_script = '''SELECT VENDOR_NAME FROM vendors;'''
	liability_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers WHERE GENERAL_LEDGER_TYPE="Liability";'''
	expense_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers WHERE GENERAL_LEDGER_TYPE="Expense";'''


	#Define class variables:
	alive = False


	#Define __init__ tkinter widgets:
	#Initialize SQL.db connection:
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
		self.title("New Invoice")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set("Select Vendor")

		self.vendor_name_label = ttk.Label(self,text="Select Vendor:")
		self.vendor_name_label.place(x=20,y=20)
		self.vendor_option_menu = ttk.OptionMenu(self,self.clicked,options[0],*options)
		self.vendor_option_menu.place(x=200,y=20)

		self.vendor_invoice_issue_date_label = ttk.Label(self,text="Invoice Issue Date:")
		self.vendor_invoice_issue_date_label.place(x=20,y=60)
		self.vendor_invoice_issue_date_entry = ttk.Entry(self)
		self.vendor_invoice_issue_date_entry.place(x=200,y=60)

		self.vendor_invoice_due_date_label = ttk.Label(self,text="Invoice Due Date:")
		self.vendor_invoice_due_date_label.place(x=20,y=100)
		self.vendor_invoice_due_date_entry = ttk.Entry(self)
		self.vendor_invoice_due_date_entry.place(x=200,y=100)

		self.vendor_invoice_number_label = ttk.Label(self,text="Invoice Number")
		self.vendor_invoice_number_label.place(x=20,y=140)
		self.vendor_invoice_number_entry = ttk.Entry(self)
		self.vendor_invoice_number_entry.place(x=200,y=140)

		self.liability_GL_label = ttk.Label(self,text="Invoice Liability GL:")
		self.liability_GL_label.place(x=20,y=180)
		self.liability_GL_text = tk.StringVar()
		self.liability_GL_text.set("Select Liability GL")
		self.liability_GL_option_menu = ttk.OptionMenu(self,self.liability_GL_text,liability_GL_options[0],*liability_GL_options)
		self.liability_GL_option_menu.place(x=200,y=180)

		self.expense_GL_label = tk.Label(self,text="Invoice Expense GL:")
		self.expense_GL_label.place(x=20,y=220)
		self.expense_GL_text = tk.StringVar()
		self.expense_GL_text.set("Select Expense GL")
		self.expense_GL_option_menu = ttk.OptionMenu(self,self.expense_GL_text,expense_GL_options[0],*expense_GL_options)
		self.expense_GL_option_menu.place(x=200,y=220)

		self.vendor_invoice_amount_label = ttk.Label(self,text="Invoice Amount")
		self.vendor_invoice_amount_label.place(x=20,y=260)
		self.vendor_invoice_amount_entry = ttk.Entry(self)
		self.vendor_invoice_amount_entry.place(x=200,y=260)

		self.vendor_invoice_notes_label = ttk.Label(self,text="Invoice Notes")
		self.vendor_invoice_notes_label.place(x=20,y=300)
		self.vendor_invoice_notes_entry = ttk.Entry(self)
		self.vendor_invoice_notes_entry.place(x=200,y=300)

		self.enter_invoice_button = ttk.Button(self,text="Enter Invoice",command=self.create_new_invoice)
		self.enter_invoice_button.place(x=200,y=340)

		self.invoice_report_button = ttk.Button(self,text="Print Invoices",command=self.invoice_report)
		self.invoice_report_button.place(x=20,y=340)


	def create_new_invoice(self):

		#Select Vendor error messages:
		if self.clicked.get() == "Select Vendor":

			select_vendor_error_message_1 = tk.messagebox.showinfo(title="Error",message="Select a vendor for new invoice.")

		#Invoice issue date error messages:
		elif self.vendor_invoice_issue_date_entry.get() == "":

			invoice_issue_date_error_message_1 = tk.messagebox.showinfo(title="Error",message="Issue date cannot be blank.")

		#Invoice due date error messges:
		elif self.vendor_invoice_due_date_entry.get() == "":

			invoice_due_date_error_message_1 = tk.messagebox.showinfo(title="Error",message="Due date cannot be blank.")

		#Invoice number errorm messages:
		elif self.vendor_invoice_number_entry.get() == "":

			invoice_number_entry_error_message_1 = tk.messagebox.showinfo(title="Error",message="Invoice number cannot be blank.")

		#Invoice liability GL error messages:
		elif self.liability_GL_text.get() == "Select Liability GL":

			liability_GL_error_message_1 = tk.messagebox.showinfo(title="Error",message="Select a liability GL.")

		#Invoice expense GL error messages:
		elif self.expense_GL_text.get() == "Select Expense GL":

			expense_GL_error_message_1 = tk.messagebox.showinfo(title="Error",message="Select an expense GL.")

		#Invoice amount error messages:
		elif self.vendor_invoice_amount_entry.get() == "":

			invoice_amount_entry_error_message_1 = tk.messagebox.showinfo(title="Error",message="Invoice amount cannot be blank.")

		else:

			#Enter invoice data using NEW_INVOICE_ENTRY class (from above):
			new_invoice_data = []

			new_invoice_name = self.clicked.get()
			new_invoice_issue_date = self.vendor_invoice_issue_date_entry.get()
			new_invoice_due_date = self.vendor_invoice_due_date_entry.get()
			new_invoice_number = self.vendor_invoice_number_entry.get()
			new_liability_GL = self.liability_GL_text.get()
			new_expense_GL = self.expense_GL_text.get()
			new_invoice_amount = self.vendor_invoice_amount_entry.get()
			new_invoice_notes = self.vendor_invoice_notes_entry.get()
			new_invoice_status = "Open"
			new_invoice_paid_date = None

			new_invoice_data.append(new_invoice_name)
			new_invoice_data.append(new_invoice_issue_date)
			new_invoice_data.append(new_invoice_due_date)
			new_invoice_data.append(new_invoice_number)
			new_invoice_data.append(new_liability_GL)
			new_invoice_data.append(new_expense_GL)
			new_invoice_data.append(new_invoice_amount)
			new_invoice_data.append(new_invoice_notes)
			new_invoice_data.append(new_invoice_status)
			new_invoice_data.append(new_invoice_paid_date)

			new_invoice = NEW_INVOICE_ENTRY(new_invoice_data)
			new_invoice.enter_invoice()


			#NEW_JOURNAL_ENTRY admin variables:

			journal_entry_timestamp = datetime.datetime.now()


			#Enter debit data using NEW_JOURNAL_ENTRY class (from above):
			new_JE_data = []

			new_journal_entry_timestamp = journal_entry_timestamp
			new_journal_entry_number = None
			new_journal_entry_date = self.vendor_invoice_issue_date_entry.get()
			new_invoice_number = self.vendor_invoice_number_entry.get()
			new_debit_general_ledger_name = self.expense_GL_text.get()
			new_debit_general_ledger_number = None
			new_debit_general_ledger_type = None
			new_credit_general_ledger_name = self.liability_GL_text.get()
			new_credit_general_ledger_number = None
			new_credit_general_ledger_type = None
			new_journal_entry_debit_amount = self.vendor_invoice_amount_entry.get()
			new_journal_entry_credit_amount = self.vendor_invoice_amount_entry.get()
			new_journal_entry_name = self.clicked.get()
			new_journal_entry_notes = self.vendor_invoice_notes_entry.get()

			new_JE_data.append(new_journal_entry_timestamp)
			new_JE_data.append(new_journal_entry_number)
			new_JE_data.append(new_journal_entry_date)
			new_JE_data.append(new_invoice_number)
			new_JE_data.append(new_debit_general_ledger_name)
			new_JE_data.append(new_debit_general_ledger_number)
			new_JE_data.append(new_debit_general_ledger_type)
			new_JE_data.append(new_credit_general_ledger_name)
			new_JE_data.append(new_credit_general_ledger_number)
			new_JE_data.append(new_credit_general_ledger_type)
			new_JE_data.append(new_journal_entry_debit_amount)
			new_JE_data.append(new_journal_entry_credit_amount)
			new_JE_data.append(new_journal_entry_name)
			new_JE_data.append(new_journal_entry_notes)

			JE_entry = NEW_JOURNAL_ENTRY(new_JE_data)
			JE_entry.journal_entry()

			confirmation_message = tk.messagebox.showinfo(title="New Invoice",message="New Invoice Created.")


	def invoice_report(self):

		invoice_report_sql_script = '''SELECT * FROM vendor_invoices;'''

		try:
			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()
				cursor.execute(invoice_report_sql_script)

				for item in cursor:
					print(item)

				connection.commit()

				cursor.close()

		except sqlite3.Error as error:

			print(error)


	def destroy(self):
		self.__class__.alive = False
		return super().destroy()
