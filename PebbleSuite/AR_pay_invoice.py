"""
[ ]
[ ]
[ ]
[ ]	AR_pay_invoice.py
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




class PAY_INVOICE_UPDATE_STATUS:


	def __init__(self,pay_invoice_status):

		self.pay_invoice_status = pay_invoice_status


	def pay_invoice(self):

		invoice_payment_status_sql_script = '''UPDATE client_invoices SET INVOICE_STATUS="Paid" WHERE INVOICE_NAME=? AND INVOICE_NUMBER=?;'''

		with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

			cursor = connection.cursor()

			cursor.execute(invoice_payment_status_sql_script,self.pay_invoice_status)

			connection.commit()

			cursor.close()




class PAY_INVOICE_UPDATE_PAYMENT_DATE:


	def __init__(self,pay_invoice_date):

		self.pay_invoice_date = pay_invoice_date


	def pay_invoice(self):

		invoice_payment_date_sql_script = '''UPDATE client_invoices SET INVOICE_PAID_DATE=? WHERE INVOICE_NAME=? AND INVOICE_NUMBER=?;'''

		with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

			cursor = connection.cursor()

			cursor.execute(invoice_payment_date_sql_script,self.pay_invoice_date)

			connection.commit()

			cursor.close()




class PAY_INVOICE_JOURNAL_ENTRY:


	def __init__(self,pay_invoice_entry):

		self.pay_invoice_entry = pay_invoice_entry


	def pay_invoice(self):

		new_payment_JE_sql_script = '''INSERT INTO journal_entries(
						JOURNAL_ENTRY_TIMESTAMP,
						JOURNAL_ENTRY_NUMBER,
						JOURNAL_ENTRY_DATE,
						CLIENT_INVOICE_NUMBER,
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

			cursor.execute(new_payment_JE_sql_script,self.pay_invoice_entry)

			connection.commit()

			cursor.close()




class AR_PAY_INVOICE_WINDOW(tk.Toplevel):

	alive = False

	client_sql_script = '''SELECT CLIENT_NAME FROM clients;'''

	asset_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME from general_ledgers WHERE GENERAL_LEDGER_TYPE="Asset - Bank Account";'''

	def __init__(self,*args,**kwargs):

		options = ["Select Client"]

		payment_GL_options = ["Select Bank Account"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.client_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.asset_GL_sql_script)

			for item in cursor:

				payment_GL_options.append(" ".join(item))

			connection.commit()

			cursor.close()

		super().__init__(*args,**kwargs)
		self.config(width=600,height=775)
		self.title("Pay Client Invoice")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.invoice_name_label = ttk.Label(self,text="Client Name")
		self.invoice_name_label.place(x=20,y=15)

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

		self.scrollbar = ttk.Scrollbar(self)
		self.scrollbar.place(x=353,y=300,width=20,height=405)
		self.listbox = tk.Listbox(self,yscrollcommand=self.scrollbar.set)
		self.listbox.place(x=20,y=300,width=333,height=405)
		self.scrollbar.config(command=self.listbox.yview)

		self.search_invoices_button = ttk.Button(self,text="Search Invoices",command=self.search_invoices)
		self.search_invoices_button.place(x=20,y=255)

		self.clear_invoices_button = ttk.Button(self,text="Clear All Invoices",command=self.clear_invoices)
		self.clear_invoices_button.place(x=125,y=725)

		self.pay_invoice_button = ttk.Button(self,text="Select Invoice",command=self.select_invoice)
		self.pay_invoice_button.place(x=20,y=725)

		self.invoice_name_label = ttk.Label(self,text="Client Invoice Name")
		self.invoice_name_label.place(x=400,y=15)
		self.invoice_name_entry_text = tk.StringVar()
		self.invoice_name_entry = ttk.Entry(self,textvariable=self.invoice_name_entry_text,state=tk.DISABLED)
		self.invoice_name_entry.place(x=400,y=45)

		self.invoice_issue_date_label = ttk.Label(self,text="Invoice Issue Date:")
		self.invoice_issue_date_label.place(x=400,y=85)
		self.invoice_issue_date_entry_text = tk.StringVar()
		self.invoice_issue_date_entry = ttk.Entry(self,textvariable=self.invoice_issue_date_entry_text,state=tk.DISABLED)
		self.invoice_issue_date_entry.place(x=400,y=115)

		self.invoice_due_date_label = ttk.Label(self,text="Invoice Due Date:")
		self.invoice_due_date_label.place(x=400,y=155)
		self.invoice_due_date_entry_text = tk.StringVar()
		self.invoice_due_date_entry = ttk.Entry(self,textvariable=self.invoice_due_date_entry_text,state=tk.DISABLED)
		self.invoice_due_date_entry.place(x=400,y=185)

		self.invoice_number_label = ttk.Label(self,text="Invoice Number:")
		self.invoice_number_label.place(x=400,y=225)
		self.invoice_number_entry_text = tk.StringVar()
		self.invoice_number_entry = ttk.Entry(self,textvariable=self.invoice_number_entry_text,state=tk.DISABLED)
		self.invoice_number_entry.place(x=400,y=255)

		self.invoice_asset_GL_label = ttk.Label(self,text="Invoice Asset GL:")
		self.invoice_asset_GL_label.place(x=400,y=295)
		self.invoice_asset_GL_entry_text = tk.StringVar()
		self.invoice_asset_GL_entry = ttk.Entry(self,textvariable=self.invoice_asset_GL_entry_text,state=tk.DISABLED)
		self.invoice_asset_GL_entry.place(x=400,y=325)

		self.invoice_income_GL_label = ttk.Label(self,text="Invoice Income GL:")
		self.invoice_income_GL_label.place(x=400,y=365)
		self.invoice_income_GL_entry_text = tk.StringVar()
		self.invoice_income_GL_entry = ttk.Entry(self,textvariable=self.invoice_income_GL_entry_text,state=tk.DISABLED)
		self.invoice_income_GL_entry.place(x=400,y=395)

		self.invoice_amount_label = ttk.Label(self,text="Invoice Amount:")
		self.invoice_amount_label.place(x=400,y=435)
		self.invoice_amount_entry_text = tk.StringVar()
		self.invoice_amount_entry = ttk.Entry(self,textvariable=self.invoice_amount_entry_text,state=tk.DISABLED)
		self.invoice_amount_entry.place(x=400,y=465)

		self.invoice_notes_label = ttk.Label(self,text="Invoice Notes:")
		self.invoice_notes_label.place(x=400,y=505)
		self.invoice_notes_entry_text = tk.StringVar()
		self.invoice_notes_entry = ttk.Entry(self,textvariable=self.invoice_notes_entry_text,state=tk.DISABLED)
		self.invoice_notes_entry.place(x=400,y=535)

		self.pay_invoice_date_label = ttk.Label(self,text="Payment Date:")
		self.pay_invoice_date_label.place(x=400,y=575)
		self.pay_invoice_date_entry_text = tk.StringVar()
		self.pay_invoice_date_entry = ttk.Entry(self,textvariable=self.pay_invoice_date_entry_text)
		self.pay_invoice_date_entry.place(x=400,y=605)

		self.pay_invoice_payment_account_label = ttk.Label(self,text="Payment Account")
		self.pay_invoice_payment_account_label.place(x=400,y=645)
		self.pay_invoice_payment_account_text = tk.StringVar()
		self.pay_invoice_payment_account_text.set(f"{payment_GL_options[0]}")
		self.pay_invoice_payment_account_option_menu = ttk.OptionMenu(self,self.pay_invoice_payment_account_text,payment_GL_options[0],*payment_GL_options)
		self.pay_invoice_payment_account_option_menu.place(x=400,y=675)

		self.cancel_invoice_changes_button = ttk.Button(self,text="Cancel",command=self.cancel_changes)
		self.cancel_invoice_changes_button.place(x=490,y=725)

		self.submit_invoice_changes_button = ttk.Button(self,text="Submit",command=self.submit_payment)
		self.submit_invoice_changes_button.place(x=400,y=725)


	def search_invoices(self):

		search_client_sql_script = '''SELECT INVOICE_NUMBER FROM client_invoices WHERE INVOICE_NAME=? AND INVOICE_STATUS=?;'''

		invoice_status = "Open"

		try:

			for item in self.select_client_listbox.curselection():

				select_client = self.select_client_listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(search_client_sql_script,(select_client,invoice_status))

				for item in cursor:

					self.listbox.insert(0,item)

				connection.commit()

				cursor.close()

		except Exception as error:

			search_invoices_error_message = tk.messagebox.showinfo(title="Pay Client Invoice",message=f"{error}")


	def clear_invoices(self):

		try:

			self.listbox.delete(0,tk.END)

		except Exception as error:

			clear_invoices_error_message = tk.messagebox.showinfo(title="Pay Client Invoice",message=f"{error}")


	def select_invoice(self):

		query_invoice_sql_script = '''SELECT * FROM client_invoices WHERE INVOICE_NUMBER=?;'''

		try:

			for item in self.listbox.curselection():

				select_invoice = self.listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				collect = []

				cursor = connection.cursor()

				cursor.execute(query_invoice_sql_script,select_invoice)

				for item in cursor:

					collect.append(item)

				self.invoice_name_entry_text.set(f"{collect[0][0]}")
				self.invoice_issue_date_entry_text.set(f"{collect[0][1]}")
				self.invoice_due_date_entry_text.set(f"{collect[0][2]}")
				self.invoice_number_entry_text.set(f"{collect[0][3]}")
				self.invoice_asset_GL_entry_text.set(f"{collect[0][4]}")
				self.invoice_income_GL_entry_text.set(f"{collect[0][5]}")
				self.invoice_amount_entry_text.set(f"{collect[0][6]}")
				self.invoice_notes_entry_text.set(f"{collect[0][7]}")

				connection.commit()

				cursor.close()

		except Exception as error:

			pay_invoice_error_message_1 = tk.messagebox.showinfo(title="Pay Client Invoice",message=f"{error}")


	def submit_payment(self):

		pay_invoice_update_status_data = []
		pay_invoice_update_payment_data = []
		pay_invoice_journal_entry_data = []

		reference_client_name = self.invoice_name_entry_text.get()
		reference_invoice_number = self.invoice_number_entry_text.get()
		reference_invoice_paid_date = self.pay_invoice_date_entry_text.get()

		reference_JE_timestamp = datetime.datetime.now()
		reference_JE_number = None
		reference_JE_entry_date = self.pay_invoice_date_entry_text.get()
		reference_client_invoice_number = self.invoice_number_entry_text.get()
		reference_debit_GL_name = self.pay_invoice_payment_account_text.get()
		reference_debit_GL_number = None
		reference_debit_GL_type = None
		reference_credit_GL_name = self.invoice_asset_GL_entry_text.get()
		reference_credit_GL_number = None
		reference_credit_GL_type = None
		reference_debit_GL_amount = self.invoice_amount_entry_text.get()
		reference_credit_GL_amount = self.invoice_amount_entry_text.get()
		reference_JE_client_name = self.invoice_name_entry_text.get()
		reference_JE_notes = self.invoice_notes_entry_text.get()

		try:

			if reference_client_name == "":

				reference_client_name_error_message_1 = tk.messagebox.showinfo(title="Pay Client Invoice",message="Client name cannot be blank.")

			elif reference_invoice_number == "":

				reference_invoice_number_error_message_1 = tk.messagebox.showinfo(title="Pay Client Invoice",message="Invoice number cannot be blank")

			elif reference_invoice_paid_date == "":

				reference_invoice_paid_date_error_message_1 = tk.messagebox.showinfo(title="Pay Client Invoice",message="Payment date cannot be blank.")

			elif reference_debit_GL_name == "Select Bank Account":

				reference_debit_GL_name_error_message_1 = tk.messagebox.showinfo(title="Pay Client Invoice",message="Payment account cannot be blank.")

			else:

				pay_invoice_update_status_data.append(reference_client_name)
				pay_invoice_update_status_data.append(reference_invoice_number)

				update_payment_status = PAY_INVOICE_UPDATE_STATUS(pay_invoice_update_status_data)
				update_payment_status.pay_invoice()

				pay_invoice_update_payment_data.append(reference_invoice_paid_date)
				pay_invoice_update_payment_data.append(reference_client_name)
				pay_invoice_update_payment_data.append(reference_invoice_number)

				update_payment_date = PAY_INVOICE_UPDATE_PAYMENT_DATE(pay_invoice_update_payment_data)
				update_payment_date.pay_invoice()

				pay_invoice_journal_entry_data.append(reference_JE_timestamp)
				pay_invoice_journal_entry_data.append(reference_JE_number)
				pay_invoice_journal_entry_data.append(reference_JE_entry_date)
				pay_invoice_journal_entry_data.append(reference_client_invoice_number)
				pay_invoice_journal_entry_data.append(reference_debit_GL_name)
				pay_invoice_journal_entry_data.append(reference_debit_GL_number)
				pay_invoice_journal_entry_data.append(reference_debit_GL_type)
				pay_invoice_journal_entry_data.append(reference_credit_GL_name)
				pay_invoice_journal_entry_data.append(reference_credit_GL_number)
				pay_invoice_journal_entry_data.append(reference_credit_GL_type)
				pay_invoice_journal_entry_data.append(reference_debit_GL_amount)
				pay_invoice_journal_entry_data.append(reference_credit_GL_amount)
				pay_invoice_journal_entry_data.append(reference_JE_client_name)
				pay_invoice_journal_entry_data.append(reference_JE_notes)

				new_invoice_payment_journal_entry = PAY_INVOICE_JOURNAL_ENTRY(pay_invoice_journal_entry_data)
				new_invoice_payment_journal_entry.pay_invoice()
				pay_invoice_confirmation_message = tk.messagebox.showinfo("Pay Client Invoice",message="Invoice payment successfully recorded.")

				pay_invoice_update_status_data.clear()
				pay_invoice_update_payment_data.clear()
				pay_invoice_journal_entry_data.clear()

		except Exception as error:

			pay_invoice_error_message_3 = tk.messagebox.showinfo(title="Pay Client Invoice",message=f"{error}")


	def cancel_changes(self):

		try:

			self.invoice_name_entry_text.set("")
			self.invoice_issue_date_entry_text.set("")
			self.invoice_due_date_entry_text.set("")
			self.invoice_number_entry_text.set("")
			self.invoice_asset_GL_entry_text.set("")
			self.invoice_income_GL_entry_text.set("")
			self.invoice_amount_entry_text.set("")
			self.invoice_notes_entry_text.set("")

		except Exception as error:

			cancel_changes_error_message = tk.messagebox.showinfo(title="Pay Client Invoice",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
