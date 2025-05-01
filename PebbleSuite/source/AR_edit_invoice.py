import datetime
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class AR_EDIT_INVOICE_WINDOW(tk.Toplevel):

	alive = False

	client_sql_script = '''SELECT CLIENT_NAME FROM clients;'''

	def __init__(self,*args,**kwargs):

		options = ["Select Client"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.client_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()

		super().__init__(*args,**kwargs)
		self.config(width=600,height=550)
		self.title("Edit Client Invoice")
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
		self.scrollbar.place(x=353,y=300,width=20,height=200)
		self.listbox = tk.Listbox(self,yscrollcommand=self.scrollbar.set)
		self.listbox.place(x=20,y=300,width=333,height=200)
		self.scrollbar.config(command=self.listbox.yview)

		self.search_invoices_button = ttk.Button(self,text="Search Invoices",command=self.search_invoices)
		self.search_invoices_button.place(x=20,y=255)

		self.clear_invoices_button = ttk.Button(self,text="Clear All Invoices",command=self.clear_invoices)
		self.clear_invoices_button.place(x=120,y=510)

		self.edit_invoice_button = ttk.Button(self,text="Edit Invoice",command=self.edit_invoice)
		self.edit_invoice_button.place(x=20,y=510)

		self.invoice_issue_date_label = ttk.Label(self,text="Invoice Issue Date:")
		self.invoice_issue_date_label.place(x=400,y=15)
		self.invoice_issue_date_entry_text = tk.StringVar()
		self.invoice_issue_date_entry = ttk.Entry(self,textvariable=self.invoice_issue_date_entry_text)
		self.invoice_issue_date_entry.place(x=400,y=45)

		self.invoice_due_date_label = ttk.Label(self,text="Invoice Due Date:")
		self.invoice_due_date_label.place(x=400,y=85)
		self.invoice_due_date_entry_text = tk.StringVar()
		self.invoice_due_date_entry = ttk.Entry(self,textvariable=self.invoice_due_date_entry_text)
		self.invoice_due_date_entry.place(x=400,y=115)

		self.invoice_number_label = ttk.Label(self,text="Invoice Number:")
		self.invoice_number_label.place(x=400,y=155)
		self.invoice_number_entry_text = tk.StringVar()
		self.invoice_number_entry = ttk.Entry(self,textvariable=self.invoice_number_entry_text,state=tk.DISABLED)
		self.invoice_number_entry.place(x=400,y=185)

		self.invoice_asset_GL_label = ttk.Label(self,text="Invoice Asset GL:")
		self.invoice_asset_GL_label.place(x=400,y=225)
		self.invoice_asset_GL_entry_text = tk.StringVar()
		self.invoice_asset_GL_entry = ttk.Entry(self,textvariable=self.invoice_asset_GL_entry_text,state=tk.DISABLED)
		self.invoice_asset_GL_entry.place(x=400,y=255)

		self.invoice_income_GL_label = ttk.Label(self,text="Invoice Income GL:")
		self.invoice_income_GL_label.place(x=400,y=295)
		self.invoice_income_GL_entry_text = tk.StringVar()
		self.invoice_income_GL_entry = ttk.Entry(self,textvariable=self.invoice_income_GL_entry_text,state=tk.DISABLED)
		self.invoice_income_GL_entry.place(x=400,y=325)

		self.invoice_amount_label = ttk.Label(self,text="Invoice Amount:")
		self.invoice_amount_label.place(x=400,y=365)
		self.invoice_amount_entry_text = tk.StringVar()
		self.invoice_amount_entry = ttk.Entry(self,textvariable=self.invoice_amount_entry_text)
		self.invoice_amount_entry.place(x=400,y=395)

		self.invoice_notes_label = ttk.Label(self,text="Invoice Notes:")
		self.invoice_notes_label.place(x=400,y=435)
		self.invoice_notes_entry_text = tk.StringVar()
		self.invoice_notes_entry = ttk.Entry(self,textvariable=self.invoice_notes_entry_text)
		self.invoice_notes_entry.place(x=400,y=465)

		self.cancel_invoice_changes_button = ttk.Button(self,text="Close",command=self.cancel_changes)
		self.cancel_invoice_changes_button.place(x=490,y=510)

		self.submit_invoice_changes_button = ttk.Button(self,text="Save",command=self.submit_changes)
		self.submit_invoice_changes_button.place(x=400,y=510)


	def search_invoices(self):

		try:

			search_client_sql_script = '''SELECT INVOICE_NUMBER FROM client_invoices WHERE INVOICE_NAME=? AND INVOICE_STATUS="Open";'''

			self.listbox.delete(0,tk.END)

			for item in self.select_client_listbox.curselection():

				select_client = self.select_client_listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(search_client_sql_script,[select_client])

				for item in cursor:

					self.listbox.insert(0,item)

				connection.commit()

				cursor.close()

		except Exception as error:

			search_invoices_error_message_1 = tk.messagebox.showinfo(title="Edit Client Invoice",message=f"{error}")


	def clear_invoices(self):

		try:

			self.listbox.delete(0,tk.END)

		except Exception as error:

			clear_invoice_error_message_1 = tk.messagebox.showinfo(title="Edit Client Invoice",message=f"{error}")


	def edit_invoice(self):

		try:

			query_invoice_sql_script = '''SELECT * FROM client_invoices WHERE INVOICE_NUMBER=?'''

			for item in self.listbox.curselection():

				select_invoice = self.listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				collect = []

				cursor = connection.cursor()

				cursor.execute(query_invoice_sql_script,select_invoice)

				for item in cursor:

					collect.append(item)

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

			edit_invoice_error_message = tk.messagebox.showinfo(title="Edit Client Invoice",message=f"{error}")


	def submit_changes(self):

		try:

			retrieve_invoice_sql_script = '''SELECT * FROM client_invoices WHERE INVOICE_NUMBER=?;'''
			edit_invoice_issue_date_sql_script = '''UPDATE client_invoices SET INVOICE_ISSUE_DATE=? WHERE INVOICE_NUMBER=?;'''
			edit_invoice_due_date_sql_script = '''UPDATE client_invoices SET INVOICE_DUE_DATE=? WHERE INVOICE_NUMBER=?;'''
			edit_invoice_amount_sql_script = '''UPDATE client_invoices SET INVOICE_AMOUNT=? WHERE INVOICE_NUMBER=?;'''
			edit_invoice_notes_sql_script = '''UPDATE client_invoices SET INVOICE_NOTES=? WHERE INVOICE_NUMBER=?;'''

			retrieve_journal_entry_sql_script = '''SELECT * FROM journal_entries WHERE CLIENT_INVOICE_NUMBER=?;'''
			edit_JE_date_sql_script = '''UPDATE journal_entries SET JOURNAL_ENTRY_DATE=? WHERE CLIENT_INVOICE_NUMBER=?;'''
			edit_JE_debit_amount_sql_script = '''UPDATE journal_entries SET JOURNAL_ENTRY_DEBIT_AMOUNT=? WHERE CLIENT_INVOICE_NUMBER=?'''
			edit_JE_credit_amount_sql_script = '''UPDATE journal_entries SET JOURNAL_ENTRY_CREDIT_AMOUNT=? WHERE CLIENT_INVOICE_NUMBER=?'''
			edit_JE_notes_sql_script = '''UPDATE journal_entries SET JOURNAL_ENTRY_NOTES=? WHERE CLIENT_INVOICE_NUMBER=?'''

			reference_invoice_number = self.invoice_number_entry_text.get()
			new_invoice_issue_date = self.invoice_issue_date_entry_text.get()
			new_invoice_due_date = self.invoice_due_date_entry_text.get()
			new_invoice_number = self.invoice_number_entry_text.get()
			new_invoice_asset_GL = self.invoice_asset_GL_entry_text.get()
			new_invoice_income_GL = self.invoice_income_GL_entry_text.get()
			new_invoice_amount = self.invoice_amount_entry_text.get()
			new_invoice_notes = self.invoice_notes_entry_text.get()

			if new_invoice_issue_date == "":

				new_invoice_issue_date_error_message_1 = tk.messagebox.showinfo(title="Edit Client Invoice",message="Invoice issue date cannot be blank.")

			elif new_invoice_due_date == "":

				new_invoice_due_date_error_message_1 = tk.messagebox.showinfo(title="Edit Client Invoice",message="Invoice due date cannot be blank.")

			elif new_invoice_number == "":

				new_invoice_number_error_message_1 = tk.messagebox.showinfo(title="Edit Client Invoice",message="Invoice number cannot be blank.")

			elif new_invoice_asset_GL == "":

				new_invoice_asset_GL_error_message_1 = tk.messagebox.showinfo(title="Edit Client Invoice",message="Asset GL cannot be blank.")

			elif new_invoice_income_GL == "":

				new_invoice_income_GL_error_message_1 = tk.messagebox.showinfo(title="Edit Client Invoice",message="Income GL cannot be blank.")

			elif new_invoice_amount == "":

				new_invoice_amount_error_message_1 = tk.messagebox.showinfo(title="Edit Client Invoice",message="Invoice amount cannot be blank.")

			else:

				with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

					cursor = connection.cursor()

					cursor.execute(edit_invoice_issue_date_sql_script,(new_invoice_issue_date,reference_invoice_number))
					cursor.execute(edit_invoice_due_date_sql_script,(new_invoice_due_date,reference_invoice_number))
					cursor.execute(edit_invoice_amount_sql_script,(new_invoice_amount,reference_invoice_number))
					cursor.execute(edit_invoice_notes_sql_script,(new_invoice_notes,reference_invoice_number))

					cursor.execute(edit_JE_date_sql_script,(new_invoice_issue_date,reference_invoice_number))
					cursor.execute(edit_JE_debit_amount_sql_script,(new_invoice_amount,reference_invoice_number))
					cursor.execute(edit_JE_credit_amount_sql_script,(new_invoice_amount,reference_invoice_number))
					cursor.execute(edit_JE_notes_sql_script,(new_invoice_notes,reference_invoice_number))

					connection.commit()

					cursor.close()

					edit_invoice_confirmation_message = tk.messagebox.showinfo(title="Edit Client Invoice",message="Invoice successfully edited.")

		except Exception as error:

			edit_invoice_error_message_3 = tk.messagebox.showinfo(title="Edit Client Invoice",message=f"{error}")


	def cancel_changes(self):

		try:

			self.invoice_issue_date_entry_text.set("")
			self.invoice_due_date_entry_text.set("")
			self.invoice_number_entry_text.set("")
			self.invoice_asset_GL_entry_text.set("")
			self.invoice_income_GL_entry_text.set("")
			self.invoice_amount_entry_text.set("")
			self.invoice_notes_entry_text.set("")

		except Exception as error:

			cancel_changes_error_message = tk.messagebox.showinfo(title="Edit Client Invoice",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
