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


	def __init__(self,new_journal_entry):

		self.new_journal_entry = new_journal_entry


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
					JOURNAL_ENTRY_NOTES,
					RECONCILIATION_STATUS)
					VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''

		with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

			cursor = connection.cursor()

			cursor.execute(new_JE_sql_script,self.new_journal_entry)

			connection.commit()

			cursor.close()


class UPDATE_JOURNAL_ENTRY_CHRONOLOGY:

	def __init__(self,journal_entry_chronology):

		self.journal_entry_chronology = journal_entry_chronology


	def update_JE_chronology(self):

		update_JE_chronology = '''UPDATE journal_entry_chronology SET JOURNAL_ENTRY_CHRONOLOGY=?;'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(update_JE_chronology,self.journal_entry_chronology)

			connection.commit()

			cursor.close()




class NEW_INVOICE_WINDOW(tk.Toplevel):

	vendor_sql_script = '''SELECT VENDOR_NAME FROM vendors;'''
	liability_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers WHERE GENERAL_LEDGER_TYPE="Liability - Accounts Payable";'''
	expense_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers WHERE GENERAL_LEDGER_TYPE="Expense - Indirect Expense";'''

	alive = False

	def __init__(self,*args,**kwargs):

		#Journal Entry Chronology code:

		journal_entry_chronology = []

		journal_entry_chronology_sql_script = '''SELECT * FROM journal_entry_chronology;'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(journal_entry_chronology_sql_script)

			for item in cursor:

				journal_entry_chronology.append(item)

			connection.commit()

			cursor.close()

		#Journal Entry Chronology code:

		options = ["Select Vendor"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.vendor_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()

		liability_GL_options = ["Select Liability GL"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.liability_GL_sql_script)

			for item in cursor:

				liability_GL_options.append(" ".join(item))

			connection.commit()

			cursor.close()

		expense_GL_options = ["Select Expense GL"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.expense_GL_sql_script)

			for item in cursor:

				expense_GL_options.append(" ".join(item))

			connection.commit()

			cursor.close()

		super().__init__(*args,**kwargs)
		self.config(width=390,height=420)
		self.title("New Vendor Invoice")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set("Select Vendor")

		self.vendor_name_label = ttk.Label(self,text="Select Vendor:")
		self.vendor_name_label.place(x=20,y=20)
		self.vendor_option_menu = ttk.OptionMenu(self,self.clicked,options[0],*options)
		self.vendor_option_menu.place(x=200,y=20)

		self.JE_number_label = ttk.Label(self,text="Journal Entry Number:")
		self.JE_number_label.place(x=20,y=60)
		self.JE_number_entry_text = tk.StringVar()
		self.JE_number_entry_text.set(journal_entry_chronology[0])
		self.JE_number_entry = ttk.Entry(self,textvariable=self.JE_number_entry_text,state=tk.DISABLED)
		self.JE_number_entry.place(x=200,y=60)

		self.vendor_invoice_issue_date_label = ttk.Label(self,text="Invoice Issue Date:")
		self.vendor_invoice_issue_date_label.place(x=20,y=100)
		self.vendor_invoice_issue_date_entry = ttk.Entry(self)
		self.vendor_invoice_issue_date_entry.place(x=200,y=100)

		self.vendor_invoice_due_date_label = ttk.Label(self,text="Invoice Due Date:")
		self.vendor_invoice_due_date_label.place(x=20,y=140)
		self.vendor_invoice_due_date_entry = ttk.Entry(self)
		self.vendor_invoice_due_date_entry.place(x=200,y=140)

		self.vendor_invoice_number_label = ttk.Label(self,text="Invoice Number")
		self.vendor_invoice_number_label.place(x=20,y=180)
		self.vendor_invoice_number_entry = ttk.Entry(self)
		self.vendor_invoice_number_entry.place(x=200,y=180)

		self.liability_GL_label = ttk.Label(self,text="Invoice Liability GL:")
		self.liability_GL_label.place(x=20,y=220)
		self.liability_GL_text = tk.StringVar()
		self.liability_GL_text.set("Select Liability GL")
		self.liability_GL_option_menu = ttk.OptionMenu(self,self.liability_GL_text,liability_GL_options[0],*liability_GL_options)
		self.liability_GL_option_menu.place(x=200,y=220)

		self.expense_GL_label = tk.Label(self,text="Invoice Expense GL:")
		self.expense_GL_label.place(x=20,y=260)
		self.expense_GL_text = tk.StringVar()
		self.expense_GL_text.set("Select Expense GL")
		self.expense_GL_option_menu = ttk.OptionMenu(self,self.expense_GL_text,expense_GL_options[0],*expense_GL_options)
		self.expense_GL_option_menu.place(x=200,y=260)

		self.vendor_invoice_amount_label = ttk.Label(self,text="Invoice Amount")
		self.vendor_invoice_amount_label.place(x=20,y=300)
		self.vendor_invoice_amount_entry = ttk.Entry(self)
		self.vendor_invoice_amount_entry.place(x=200,y=300)

		self.vendor_invoice_notes_label = ttk.Label(self,text="Invoice Notes")
		self.vendor_invoice_notes_label.place(x=20,y=340)
		self.vendor_invoice_notes_entry = ttk.Entry(self)
		self.vendor_invoice_notes_entry.place(x=200,y=340)

		self.enter_invoice_button = ttk.Button(self,text="Enter Invoice",command=self.create_new_invoice)
		self.enter_invoice_button.place(x=200,y=380)

		self.invoice_report_button = ttk.Button(self,text="Print Invoices",command=self.invoice_report)
		self.invoice_report_button.place(x=20,y=380)


	def create_new_invoice(self):

		try:

			#Select Vendor error messages:
			if self.clicked.get() == "Select Vendor":

				select_vendor_error_message_1 = tk.messagebox.showinfo(title="New Vendor Invoice",message="Select a vendor for new invoice.")

			#Invoice issue date error messages:
			elif self.vendor_invoice_issue_date_entry.get() == "":

				invoice_issue_date_error_message_1 = tk.messagebox.showinfo(title="New Vendor Invoice",message="Issue date cannot be blank.")

			#Invoice due date error messges:
			elif self.vendor_invoice_due_date_entry.get() == "":

				invoice_due_date_error_message_1 = tk.messagebox.showinfo(title="New Vendor Invoice",message="Due date cannot be blank.")

			#Invoice number errorm messages:
			elif self.vendor_invoice_number_entry.get() == "":

				invoice_number_entry_error_message_1 = tk.messagebox.showinfo(title="New Vendor Invoice",message="Invoice number cannot be blank.")

			#Invoice liability GL error messages:
			elif self.liability_GL_text.get() == "Select Liability GL":

				liability_GL_error_message_1 = tk.messagebox.showinfo(title="New Vendor Invoice",message="Select a liability GL.")

			#Invoice expense GL error messages:
			elif self.expense_GL_text.get() == "Select Expense GL":

				expense_GL_error_message_1 = tk.messagebox.showinfo(title="New Vendor Invoice",message="Select an expense GL.")

			#Invoice amount error messages:
			elif self.vendor_invoice_amount_entry.get() == "":

				invoice_amount_entry_error_message_1 = tk.messagebox.showinfo(title="New Vendor Invoice",message="Invoice amount cannot be blank.")

			else:

				new_invoice_data = []

				new_JE_data = []

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

				journal_entry_timestamp = datetime.datetime.now()

				new_journal_entry_timestamp = journal_entry_timestamp
				new_journal_entry_number = self.JE_number_entry.get()
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
				new_journal_entry_reconciliation_status = 0

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
				new_JE_data.append(new_journal_entry_reconciliation_status)

				JE_entry = NEW_JOURNAL_ENTRY(new_JE_data)
				JE_entry.journal_entry()

				next_JE_number = []

				int_format_JE_number = int(new_journal_entry_number)
				int_next_JE_number = int_format_JE_number + 1

				next_JE_number.append(int_next_JE_number)

				next_journal_entry_number = UPDATE_JOURNAL_ENTRY_CHRONOLOGY(next_JE_number)
				next_journal_entry_number.update_JE_chronology()

				confirmation_message = tk.messagebox.showinfo(title="New Vendor Invoice",message="New vendor invoice successfully created.")

		except Exception as error:

			journal_entry_error_message_1 = tk.messagebox.showinfo(title="New Vendor Invoice",message=f"{error}")


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

		except Exception as error:

			print(error)


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
