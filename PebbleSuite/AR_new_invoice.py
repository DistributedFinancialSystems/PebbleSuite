#Python Standard Library dependencies

import datetime
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class AR_NEW_INVOICE_ENTRY:

	def __init__(self,new_invoice_entry):

		self.new_invoice_entry = new_invoice_entry

	def enter_invoice(self):

		new_invoice_sql_script = '''INSERT INTO client_invoices(
					INVOICE_NAME,
					INVOICE_ISSUE_DATE,
					INVOICE_DUE_DATE,
					INVOICE_NUMBER,
					INVOICE_ASSET_ACCOUNT,
					INVOICE_INCOME_ACCOUNT,
					INVOICE_AMOUNT,
					INVOICE_NOTES)
					VALUES(?,?,?,?,?,?,?,?);'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(new_invoice_sql_script,self.new_invoice_entry)
			connection.commit()
			cursor.close()




class NEW_JOURNAL_ENTRY:

	def __init__(self,new_journal_entry):
		self.new_journal_entry = new_journal_entry

	def debit_entry(self):

		new_debit_JE_sql_script = '''INSERT INTO journal_entries(
						JOURNAL_ENTRY_TIMESTAMP,
						JOURNAL_ENTRY_NUMBER,
						JOURNAL_ENTRY_DATE,
						INVOICE_NUMBER,
						GENERAL_LEDGER_NAME,
						GENERAL_LEDGER_NUMBER,
						GENERAL_LEDGER_TYPE,
						JOURNAL_ENTRY_DEBIT_AMOUNT,
						JOURNAL_ENTRY_CREDIT_AMOUNT,
						JOURNAL_ENTRY_NOTES)
						VALUES(?,?,?,?,?,?,?,?,?,?);'''

		with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

			try:

				cursor = connection.cursor()
				cursor.execute(new_debit_JE_sql_script,self.new_journal_entry)
				connection.commit()
				cursor.close()

			except sqlite3.Error as error:

				debit_entry_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")


	def credit_entry(self):

		new_credit_JE_sql_script = '''INSERT INTO journal_entries(
						JOURNAL_ENTRY_TIMESTAMP,
						JOURNAL_ENTRY_NUMBER,
						JOURNAL_ENTRY_DATE,
						INVOICE_NUMBER,
						GENERAL_LEDGER_NAME,
						GENERAL_LEDGER_NUMBER,
						GENERAL_LEDGER_TYPE,
						JOURNAL_ENTRY_DEBIT_AMOUNT,
						JOURNAL_ENTRY_CREDIT_AMOUNT,
						JOURNAL_ENTRY_NOTES)
						VALUES(?,?,?,?,?,?,?,?,?,?);'''

		with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

			try:

				cursor = connection.cursor()
				cursor.execute(new_credit_JE_sql_script,self.new_journal_entry)
				connection.commit()
				cursor.close()

			except sqlite3.Error as error:

				credit_entry_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")




class AR_NEW_INVOICE_WINDOW(tk.Toplevel):

	#Define SQL.db scripts:
	client_sql_script = '''SELECT CLIENT_NAME FROM clients;'''
	asset_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers WHERE GENERAL_LEDGER_TYPE="Asset";'''
	income_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers WHERE GENERAL_LEDGER_TYPE="Income";'''


	#Define class variables:
	alive = False


	#Define __init__ tkinter widgets:
	#Initialize SQL.db connection:
	def __init__(self,*args,**kwargs):


		#Retrieve Vendor data from SQL.db:
		options = ["Select Vendor"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(self.client_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()
			cursor.close()


		#Retrieve liability GL data from SQL.db:
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
		self.title("New Invoice")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set("Select Vendor")

		self.client_name_label = ttk.Label(self,text="Select Vendor:")
		self.client_name_label.place(x=20,y=20)
		self.client_option_menu = ttk.OptionMenu(self,self.clicked,options[0],*options)
		self.client_option_menu.place(x=200,y=20)

		self.client_invoice_issue_date_label = ttk.Label(self,text="Invoice Issue Date:")
		self.client_invoice_issue_date_label.place(x=20,y=60)
		self.client_invoice_issue_date_entry = ttk.Entry(self)
		self.client_invoice_issue_date_entry.place(x=200,y=60)

		self.client_invoice_due_date_label = ttk.Label(self,text="Invoice Due Date:")
		self.client_invoice_due_date_label.place(x=20,y=100)
		self.client_invoice_due_date_entry = ttk.Entry(self)
		self.client_invoice_due_date_entry.place(x=200,y=100)

		self.client_invoice_number_label = ttk.Label(self,text="Invoice Number")
		self.client_invoice_number_label.place(x=20,y=140)
		self.client_invoice_number_entry = ttk.Entry(self)
		self.client_invoice_number_entry.place(x=200,y=140)

		self.asset_GL_label = ttk.Label(self,text="Invoice Asset GL:")
		self.asset_GL_label.place(x=20,y=180)
		self.asset_GL_text = tk.StringVar()
		self.asset_GL_text.set("Select Asset GL")
		self.asset_GL_option_menu = ttk.OptionMenu(self,self.asset_GL_text,asset_GL_options[0],*asset_GL_options)
		self.asset_GL_option_menu.place(x=200,y=180)

		self.income_GL_label = tk.Label(self,text="Invoice Income GL:")
		self.income_GL_label.place(x=20,y=220)
		self.income_GL_text = tk.StringVar()
		self.income_GL_text.set("Select Income GL")
		self.income_GL_option_menu = ttk.OptionMenu(self,self.income_GL_text,income_GL_options[0],*income_GL_options)
		self.income_GL_option_menu.place(x=200,y=220)

		self.client_invoice_amount_label = ttk.Label(self,text="Invoice Amount")
		self.client_invoice_amount_label.place(x=20,y=260)
		self.client_invoice_amount_entry = ttk.Entry(self)
		self.client_invoice_amount_entry.place(x=200,y=260)

		self.client_invoice_notes_label = ttk.Label(self,text="Invoice Notes")
		self.client_invoice_notes_label.place(x=20,y=300)
		self.client_invoice_notes_entry = ttk.Entry(self)
		self.client_invoice_notes_entry.place(x=200,y=300)

		self.enter_invoice_button = ttk.Button(self,text="Enter Invoice",command=self.create_new_invoice)
		self.enter_invoice_button.place(x=200,y=340)

		self.invoice_report_button = ttk.Button(self,text="Print Invoices",command=self.invoice_report)
		self.invoice_report_button.place(x=20,y=340)


	def create_new_invoice(self):

		#Select client error messages:
		if self.clicked.get() == "Select Client":

			select_client_error_message_1 = tk.messagebox.showinfo(title="Error",message="Select a client for new invoice.")

		#Invoice issue date error messages:
		elif self.client_invoice_issue_date_entry.get() == "":

			invoice_issue_date_error_message_1 = tk.messagebox.showinfo(title="Error",message="Issue date cannot be blank.")

		#Invoice due date error messges:
		elif self.client_invoice_due_date_entry.get() == "":

			invoice_due_date_error_message_1 = tk.messagebox.showinfo(title="Error",message="Due date cannot be blank.")

		#Invoice number errorm messages:
		elif self.client_invoice_number_entry.get() == "":

			invoice_number_entry_error_message_1 = tk.messagebox.showinfo(title="Error",message="Invoice number cannot be blank.")

		#Invoice asset GL error messages:
		elif self.asset_GL_text.get() == "Select Asset GL":

			asset_GL_error_message_1 = tk.messagebox.showinfo(title="Error",message="Select an Asset GL.")

		#Invoice income GL error messages:
		elif self.income_GL_text.get() == "Select Income GL":

			expense_GL_error_message_1 = tk.messagebox.showinfo(title="Error",message="Select an income GL.")

		#Invoice amount error messages:
		elif self.client_invoice_amount_entry.get() == "":

			invoice_amount_entry_error_message_1 = tk.messagebox.showinfo(title="Error",message="Invoice amount cannot be blank.")

		else:

			#Enter invoice data using NEW_INVOICE_ENTRY class (from above):
			new_invoice_data = []

			new_invoice_name = self.clicked.get()
			new_invoice_issue_date = self.client_invoice_issue_date_entry.get()
			new_invoice_due_date = self.client_invoice_due_date_entry.get()
			new_invoice_number = self.client_invoice_number_entry.get()
			new_asset_GL = self.asset_GL_text.get()
			new_income_GL = self.income_GL_text.get()
			new_invoice_amount = self.client_invoice_amount_entry.get()
			new_invoice_notes = self.client_invoice_notes_entry.get()

			new_invoice_data.append(new_invoice_name)
			new_invoice_data.append(new_invoice_issue_date)
			new_invoice_data.append(new_invoice_due_date)
			new_invoice_data.append(new_invoice_number)
			new_invoice_data.append(new_asset_GL)
			new_invoice_data.append(new_income_GL)
			new_invoice_data.append(new_invoice_amount)
			new_invoice_data.append(new_invoice_notes)

			new_invoice = AR_NEW_INVOICE_ENTRY(new_invoice_data)
			new_invoice.enter_invoice()


			#NEW_JOURNAL_ENTRY admin variables:

			journal_entry_timestamp = datetime.datetime.now()


			#Enter debit data using NEW_JOURNAL_ENTRY class (from above):
			new_debit_data = []

			new_journal_entry_timestamp = journal_entry_timestamp
			new_journal_entry_number = 0
			new_journal_entry_date = self.client_invoice_issue_date_entry.get()
			new_invoice_number = self.client_invoice_number_entry.get()
			new_general_ledger_name = self.asset_GL_text.get()
			new_general_ledger_number = self.client_invoice_number_entry.get()
			new_general_ledger_type = "Asset"
			new_journal_entry_debit_amount = self.client_invoice_amount_entry.get()
			new_journal_entry_credit_amount = 0
			new_journal_entry_notes = self.client_invoice_notes_entry.get()

			new_debit_data.append(new_journal_entry_timestamp)
			new_debit_data.append(new_journal_entry_number)
			new_debit_data.append(new_journal_entry_date)
			new_debit_data.append(new_invoice_number)
			new_debit_data.append(new_general_ledger_name)
			new_debit_data.append(new_general_ledger_number)
			new_debit_data.append(new_general_ledger_type)
			new_debit_data.append(new_journal_entry_debit_amount)
			new_debit_data.append(new_journal_entry_credit_amount)
			new_debit_data.append(new_journal_entry_notes)

			debit_entry = NEW_JOURNAL_ENTRY(new_debit_data)
			debit_entry.debit_entry()


			#Enter credit data using NEW_JOURNAL_ENTRY class (from above):
			new_credit_data = []

			new_journal_entry_timestamp = journal_entry_timestamp
			new_journal_entry_number = 0
			new_journal_entry_date = self.client_invoice_issue_date_entry.get()
			new_invoice_number = self.client_invoice_number_entry.get()
			new_general_ledger_name = self.income_GL_text.get()
			new_general_ledger_number = self.client_invoice_number_entry.get()
			new_general_ledger_type = "Income"
			new_journal_entry_debit_amount = 0
			new_journal_entry_credit_amount = self.client_invoice_amount_entry.get()
			new_journal_entry_notes = self.client_invoice_notes_entry.get()

			new_credit_data.append(new_journal_entry_timestamp)
			new_credit_data.append(new_journal_entry_number)
			new_credit_data.append(new_journal_entry_date)
			new_credit_data.append(new_invoice_number)
			new_credit_data.append(new_general_ledger_name)
			new_credit_data.append(new_general_ledger_number)
			new_credit_data.append(new_general_ledger_type)
			new_credit_data.append(new_journal_entry_debit_amount)
			new_credit_data.append(new_journal_entry_credit_amount)
			new_credit_data.append(new_journal_entry_notes)

			credit_entry = NEW_JOURNAL_ENTRY(new_credit_data)
			credit_entry.credit_entry()

			confirmation_message = tk.messagebox.showinfo(title="New Invoice",message="New Invoice Created.")


	def invoice_report(self):

		invoice_report_sql_script = '''SELECT * FROM client_invoices;'''

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
