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
						CREDIT_MEMO_NOTES,
						CREDIT_MEMO_STATUS)
						VALUES(?,?,?,?,?,?,?,?,?);'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(new_credit_memo_sql_script,self.new_credit_memo_entry)

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




class NEW_CLIENT_CREDIT_MEMO_WINDOW(tk.Toplevel):

	client_sql_script = '''SELECT CLIENT_NAME FROM clients;'''
	liability_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers WHERE GENERAL_LEDGER_TYPE="Liability - Accounts Payable";'''
	expense_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers WHERE GENERAL_LEDGER_TYPE="Expense - Indirect Expense";'''

	alive = False

	def __init__(self,*args,**kwargs):

		#_____________________________________________________
		#Retrieving journal entry chronology data from SQL.db:
		#_____________________________________________________
		journal_entry_chronology = []

		journal_entry_chronology_sql_script = '''SELECT * FROM journal_entry_chronology;'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(journal_entry_chronology_sql_script)

			for item in cursor:

				journal_entry_chronology.append(item)

			connection.commit()

			cursor.close()

		#____________________________________
		#Retrieving client names from SQL.db:
		#____________________________________
		options = ["Select Client"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.client_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()

		#______________________________________
		#Retrieving liability GL's from SQL.db:
		#______________________________________
		liability_GL_options = ["Select Liability GL"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.liability_GL_sql_script)

			for item in cursor:

				liability_GL_options.append(" ".join(item))

			connection.commit()

			cursor.close()

		#____________________________________
		#Retrieving expense GL's from SQL.db:
		#____________________________________
		expense_GL_options = ["Select Expense GL"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.expense_GL_sql_script)

			for item in cursor:

				expense_GL_options.append(" ".join(item))

			connection.commit()

			cursor.close()

		#____________________________
		#Configuring Tkinter widgets:
		#____________________________
		super().__init__(*args,**kwargs)
		self.config(width=390,height=420)
		self.title("New Client Credit Memo")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set("Select Client")

		self.client_name_label = ttk.Label(self,text="Select Client:")
		self.client_name_label.place(x=20,y=20)
		self.client_option_menu = ttk.OptionMenu(self,self.clicked,options[0],*options)
		self.client_option_menu.place(x=200,y=20)

		self.JE_number_label = ttk.Label(self,text="Journal Entry Number:")
		self.JE_number_label.place(x=20,y=60)
		self.JE_number_entry_text = tk.StringVar()
		self.JE_number_entry_text.set(journal_entry_chronology[0])
		self.JE_number_entry = ttk.Entry(self,textvariable=self.JE_number_entry_text,state=tk.DISABLED)
		self.JE_number_entry.place(x=200,y=60)

		self.client_credit_memo_issue_date_label = ttk.Label(self,text="Credit Memo Issue Date:")
		self.client_credit_memo_issue_date_label.place(x=20,y=100)
		self.client_credit_memo_issue_date_entry_text = tk.StringVar()
		self.client_credit_memo_issue_date_entry = ttk.Entry(self,textvariable=self.client_credit_memo_issue_date_entry_text)
		self.client_credit_memo_issue_date_entry.place(x=200,y=100)

		self.client_credit_memo_due_date_label = ttk.Label(self,text="Credit Memo Due Date:")
		self.client_credit_memo_due_date_label.place(x=20,y=140)
		self.client_credit_memo_due_date_entry_text = tk.StringVar()
		self.client_credit_memo_due_date_entry = ttk.Entry(self,textvariable=self.client_credit_memo_due_date_entry_text)
		self.client_credit_memo_due_date_entry.place(x=200,y=140)

		self.client_credit_memo_number_label = ttk.Label(self,text="Credit Memo Number:")
		self.client_credit_memo_number_label.place(x=20,y=180)
		self.client_credit_memo_number_entry_text = tk.StringVar()
		self.client_credit_memo_number_entry = ttk.Entry(self,textvariable=self.client_credit_memo_number_entry_text)
		self.client_credit_memo_number_entry.place(x=200,y=180)

		self.liability_GL_label = ttk.Label(self,text="Credit Memo Liability GL:")
		self.liability_GL_label.place(x=20,y=220)
		self.liability_GL_text = tk.StringVar()
		self.liability_GL_text.set("Select Liability GL")
		self.liability_GL_option_menu = ttk.OptionMenu(self,self.liability_GL_text,liability_GL_options[0],*liability_GL_options)
		self.liability_GL_option_menu.place(x=200,y=220)

		self.expense_GL_label = tk.Label(self,text="Credit Memo Expense GL:")
		self.expense_GL_label.place(x=20,y=260)
		self.expense_GL_text = tk.StringVar()
		self.expense_GL_text.set("Select Expense GL")
		self.expense_GL_option_menu = ttk.OptionMenu(self,self.expense_GL_text,expense_GL_options[0],*expense_GL_options)
		self.expense_GL_option_menu.place(x=200,y=260)

		self.client_credit_memo_amount_label = ttk.Label(self,text="Credit Memo Amount:")
		self.client_credit_memo_amount_label.place(x=20,y=300)
		self.client_credit_memo_amount_entry_text = tk.StringVar()
		self.client_credit_memo_amount_entry = ttk.Entry(self,textvariable=self.client_credit_memo_amount_entry_text)
		self.client_credit_memo_amount_entry.place(x=200,y=300)

		self.client_credit_memo_notes_label = ttk.Label(self,text="Credit Memo Notes:")
		self.client_credit_memo_notes_label.place(x=20,y=340)
		self.client_credit_memo_notes_entry_text = tk.StringVar()
		self.client_credit_memo_notes_entry = ttk.Entry(self,textvariable=self.client_credit_memo_notes_entry_text)
		self.client_credit_memo_notes_entry.place(x=200,y=340)

		self.enter_credit_memo_button = ttk.Button(self,text="Enter Credit Memos",command=self.create_new_credit_memo)
		self.enter_credit_memo_button.place(x=200,y=380)

		self.credit_memo_report_button = ttk.Button(self,text="Print Credit Memos",command=self.credit_memo_report)
		self.credit_memo_report_button.place(x=20,y=380)


	def create_new_credit_memo(self):

		try:

			new_credit_memo_name = self.clicked.get()
			new_credit_memo_issue_date = self.client_credit_memo_issue_date_entry.get()
			new_credit_memo_due_date = self.client_credit_memo_due_date_entry.get()
			new_credit_memo_number = self.client_credit_memo_number_entry.get()
			new_liability_GL = self.liability_GL_text.get()
			new_expense_GL = self.expense_GL_text.get()
			new_credit_memo_amount = self.client_credit_memo_amount_entry.get()
			new_credit_memo_notes = self.client_credit_memo_notes_entry.get()
			new_credit_memo_status = "Open"

			journal_entry_timestamp = datetime.datetime.now()

			new_journal_entry_timestamp = journal_entry_timestamp
			new_journal_entry_number = self.JE_number_entry.get()
			new_journal_entry_date = self.client_credit_memo_issue_date_entry.get()
			new_credit_memo_number = self.client_credit_memo_number_entry.get()
			new_debit_general_ledger_name = self.expense_GL_text.get()
			new_debit_general_ledger_number = None
			new_debit_general_ledger_type = None
			new_credit_general_ledger_name = self.liability_GL_text.get()
			new_credit_general_ledger_number = None
			new_credit_general_ledger_type = None
			new_journal_entry_debit_amount = self.client_credit_memo_amount_entry.get()
			new_journal_entry_credit_amount = self.client_credit_memo_amount_entry.get()
			new_journal_entry_name = self.clicked.get()
			new_journal_entry_notes = self.client_credit_memo_notes_entry.get()
			new_journal_entry_reconciliation_status = 0

			#Select client error messages:
			if self.clicked.get() == "Select Client":

				select_client_error_message_1 = tk.messagebox.showinfo(title="New Client Credit Memo",message="Select a client for new credit memo.")

			#credit_memo issue date error messages:
			elif self.client_credit_memo_issue_date_entry.get() == "":

				credit_memo_issue_date_error_message_1 = tk.messagebox.showinfo(title="New Client Credit Memo",message="Issue date cannot be blank.")

			#credit_memo due date error messges:
			elif self.client_credit_memo_due_date_entry.get() == "":

				credit_memo_due_date_error_message_1 = tk.messagebox.showinfo(title="New Client Credit Memo",message="Due date cannot be blank.")

			#credit_memo number errorm messages:
			elif self.client_credit_memo_number_entry.get() == "":

				credit_memo_number_entry_error_message_1 = tk.messagebox.showinfo(title="New Client Credit Memo",message="credit_memo number cannot be blank.")

			#credit_memo liability GL error messages:
			elif self.liability_GL_text.get() == "Select Liability GL":

				liability_GL_error_message_1 = tk.messagebox.showinfo(title="New Client Credit Memo",message="Select a liability GL.")

			#credit_memo expense GL error messages:
			elif self.expense_GL_text.get() == "Select Expense GL":

				expense_GL_error_message_1 = tk.messagebox.showinfo(title="New Client Credit Memo",message="Select an expense GL.")

			#credit_memo amount error messages:
			elif self.client_credit_memo_amount_entry.get() == "":

				credit_memo_amount_entry_error_message_1 = tk.messagebox.showinfo(title="New Client Credit Memo",message="credit_memo amount cannot be blank.")

			else:

				#_________________________________________________
				#Collecting credit memo data from Tkinter widgets:
				#_________________________________________________
				new_credit_memo_data = []

				new_credit_memo_data.append(new_credit_memo_name)
				new_credit_memo_data.append(new_credit_memo_issue_date)
				new_credit_memo_data.append(new_credit_memo_due_date)
				new_credit_memo_data.append(new_credit_memo_number)
				new_credit_memo_data.append(new_liability_GL)
				new_credit_memo_data.append(new_expense_GL)
				new_credit_memo_data.append(new_credit_memo_amount)
				new_credit_memo_data.append(new_credit_memo_notes)
				new_credit_memo_data.append(new_credit_memo_status)

				new_credit_memo = NEW_CLIENT_CREDIT_MEMO_ENTRY(new_credit_memo_data)
				new_credit_memo.enter_credit_memo()

				#___________________________________________________
				#Collecting journal entry data from Tkinter widgets:
				#___________________________________________________
				new_JE_data = []

				new_JE_data.append(new_journal_entry_timestamp)
				new_JE_data.append(new_journal_entry_number)
				new_JE_data.append(new_journal_entry_date)
				new_JE_data.append(new_credit_memo_number)
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

				journal_entry = NEW_JOURNAL_ENTRY(new_JE_data)
				journal_entry.journal_entry()

				#_________________________________________________________
				#Updating journal entry chronology for next journal entry:
				#_________________________________________________________
				next_JE_number = []

				int_format_JE_number = int(new_journal_entry_number)
				int_next_JE_number = int_format_JE_number + 1

				next_JE_number.append(int_next_JE_number)

				next_journal_entry_number = UPDATE_JOURNAL_ENTRY_CHRONOLOGY(next_JE_number)
				next_journal_entry_number.update_JE_chronology()

				create_new_credit_memo_confirmation_message_1 = tk.messagebox.showinfo(title="New Client Credit Memo",message="New Credit Memo Created.")

				#_________________________________________
				#Clearing data from Tkinter entry widgets:
				#_________________________________________
				self.JE_number_entry_text.set("")
				self.client_credit_memo_issue_date_entry_text.set("")
				self.client_credit_memo_due_date_entry_text.set("")
				self.client_credit_memo_number_entry_text.set("")
				self.liability_GL_text.set("Select Liability GL")
				self.expense_GL_text.set("Select Expense GL")
				self.client_credit_memo_amount_entry_text.set("")
				self.client_credit_memo_notes_entry_text.set("")

		except Exception as error:

			create_new_credit_memo_error_message_1 = tk.messagebox.showinfo(title="New Client Credit Memo",message=f"{error}")


	def credit_memo_report(self):

		try:

			credit_memo_report_sql_script = '''SELECT * FROM client_credit_memos;'''

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(credit_memo_report_sql_script)

				for item in cursor:

					print(item)

				connection.commit()

				cursor.close()

		except Exception as error:

			print(error)


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()

