import datetime
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class AP_EDIT_INVOICE_WINDOW(tk.Toplevel):

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
		self.config(width=600,height=615)
		self.title("Edit Vendor Invoice")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.invoice_name_label = ttk.Label(self,text="Vendor Name")
		self.invoice_name_label.place(x=20,y=15)

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
		self.scrollbar.place(x=353,y=300,width=20,height=260)
		self.listbox = tk.Listbox(self,yscrollcommand=self.scrollbar.set)
		self.listbox.place(x=20,y=300,width=333,height=260)
		self.scrollbar.config(command=self.listbox.yview)

		self.search_invoices_button = ttk.Button(self,text="Search Invoices",command=self.search_invoices)
		self.search_invoices_button.place(x=20,y=255)

		self.clear_invoices_button = ttk.Button(self,text="Clear All Invoices",command=self.clear_invoices)
		self.clear_invoices_button.place(x=120,y=575)

		self.edit_invoice_button = ttk.Button(self,text="Edit Invoice",command=self.edit_invoice)
		self.edit_invoice_button.place(x=20,y=575)

		self.invoice_name_label = ttk.Label(self,text="Invoice Name:")
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

		self.invoice_liability_GL_label = ttk.Label(self,text="Invoice Liability GL:")
		self.invoice_liability_GL_label.place(x=400,y=295)
		self.invoice_liability_GL_entry_text = tk.StringVar()
		self.invoice_liability_GL_entry = ttk.Entry(self,textvariable=self.invoice_liability_GL_entry_text,state=tk.DISABLED)
		self.invoice_liability_GL_entry.place(x=400,y=325)

		self.invoice_expense_GL_label = ttk.Label(self,text="Invoice Expense GL:")
		self.invoice_expense_GL_label.place(x=400,y=365)
		self.invoice_expense_GL_entry_text = tk.StringVar()
		self.invoice_expense_GL_entry = ttk.Entry(self,textvariable=self.invoice_expense_GL_entry_text,state=tk.DISABLED)
		self.invoice_expense_GL_entry.place(x=400,y=395)

		self.invoice_amount_label = ttk.Label(self,text="Invoice Amount:")
		self.invoice_amount_label.place(x=400,y=435)
		self.invoice_amount_entry_text = tk.StringVar()
		self.invoice_amount_entry = ttk.Entry(self,textvariable=self.invoice_amount_entry_text)
		self.invoice_amount_entry.place(x=400,y=465)

		self.invoice_notes_label = ttk.Label(self,text="Invoice Notes:")
		self.invoice_notes_label.place(x=400,y=505)
		self.invoice_notes_entry_text = tk.StringVar()
		self.invoice_notes_entry = ttk.Entry(self,textvariable=self.invoice_notes_entry_text)
		self.invoice_notes_entry.place(x=400,y=535)

		self.cancel_invoice_changes_button = ttk.Button(self,text="Close",command=self.cancel_changes)
		self.cancel_invoice_changes_button.place(x=490,y=575)

		self.submit_invoice_changes_button = ttk.Button(self,text="Save",command=self.submit_changes)
		self.submit_invoice_changes_button.place(x=400,y=575)


	def search_invoices(self):

		try:

			search_vendor_sql_script = '''SELECT INVOICE_NUMBER FROM vendor_invoices WHERE INVOICE_NAME=? AND INVOICE_STATUS="Open";'''

			self.listbox.delete(0,tk.END)

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

			search_invoices_error_message_2 = tk.messagebox.showinfo(title="Edit Vendor Invoice",message=f"{error}")


	def clear_invoices(self):

		try:

			self.listbox.delete(0,tk.END)

		except Exception as error:

			clear_invoices_error_message_1 = tk.messagebox.showinfo(title="Edit Vendor Invoice",message=f"{error}")


	def edit_invoice(self):

		try:

			query_invoice_sql_script = '''SELECT * FROM vendor_invoices WHERE INVOICE_NUMBER=?;'''

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
				self.invoice_liability_GL_entry_text.set(f"{collect[0][4]}")
				self.invoice_expense_GL_entry_text.set(f"{collect[0][5]}")
				self.invoice_amount_entry_text.set(f"{collect[0][6]}")
				self.invoice_notes_entry_text.set(f"{collect[0][7]}")

				connection.commit()

				cursor.close()

		except Exception as error:

			edit_invoice_error_message_1 = tk.messagebox.showinfo(title="Edit Vendor Invoice",message=f"{error}")


	def submit_changes(self):

		retrieve_invoice_sql_script = '''SELECT * FROM vendor_invoices WHERE INVOICE_NAME=? AND INVOICE_NUMBER=?;'''
		edit_invoice_issue_date_sql_script = '''UPDATE vendor_invoices SET INVOICE_ISSUE_DATE=? WHERE INVOICE_NAME=? AND INVOICE_NUMBER=?;'''
		edit_invoice_due_date_sql_script = '''UPDATE vendor_invoices SET INVOICE_DUE_DATE=? WHERE INVOICE_NAME=? AND INVOICE_NUMBER=?;'''
		edit_invoice_amount_sql_script = '''UPDATE vendor_invoices SET INVOICE_AMOUNT=? WHERE INVOICE_NAME=? AND INVOICE_NUMBER=?;'''
		edit_invoice_notes_sql_script = '''UPDATE vendor_invoices SET INVOICE_NOTES=? WHERE INVOICE_NAME=? AND INVOICE_NUMBER=?;'''

		retrieve_journal_entry_sql_script = '''SELECT * FROM journal_entries WHERE JOURNAL_ENTRY_VENDOR_NAME=? AND VENDOR_INVOICE_NUMBER=?;'''
		edit_JE_date_sql_script = '''UPDATE journal_entries SET JOURNAL_ENTRY_DATE=? WHERE JOURNAL_ENTRY_VENDOR_NAME=? AND VENDOR_INVOICE_NUMBER=?;'''
		edit_JE_debit_amount_sql_script = '''UPDATE journal_entries SET JOURNAL_ENTRY_DEBIT_AMOUNT=? WHERE JOURNAL_ENTRY_VENDOR_NAME=? AND VENDOR_INVOICE_NUMBER=?'''
		edit_JE_credit_amount_sql_script = '''UPDATE journal_entries SET JOURNAL_ENTRY_CREDIT_AMOUNT=? WHERE JOURNAL_ENTRY_VENDOR_NAME=? AND VENDOR_INVOICE_NUMBER=?'''
		edit_JE_notes_sql_script = '''UPDATE journal_entries SET JOURNAL_ENTRY_NOTES=? WHERE JOURNAL_ENTRY_VENDOR_NAME=? AND VENDOR_INVOICE_NUMBER=?'''

		try:

			reference_vendor_name = self.invoice_name_entry_text.get()
			reference_invoice_number = self.invoice_number_entry_text.get()
			new_invoice_issue_date = self.invoice_issue_date_entry_text.get()
			new_invoice_due_date = self.invoice_due_date_entry_text.get()
			new_invoice_amount = self.invoice_amount_entry_text.get()
			new_invoice_notes = self.invoice_notes_entry_text.get()

			#Error messages:
			if reference_vendor_name == "":

				submit_changes_error_message_1 = tk.messagebox.showinfo(title="Edit Vendor Invoice",message="Vendor name cannot be blank.")

			elif reference_invoice_number == "":

				submit_changes_error_message_2 = tk.messagebox.showinfo(title="Edit Vendor Invoice",message="Invoice number cannot be blank.")

			elif new_invoice_issue_date == "":

				submit_changes_error_message_3 = tk.messagebox.showinfo(title="Edit Vendor Invoice",message="Invoice issue date cannot be blank.")

			elif new_invoice_due_date == "":

				submit_changes_error_message_4 = tk.messagebox.showinfo(title="Edit Vendor Invoice",message="Invoice due date cannot be blank.")

			elif new_invoice_amount == "":

				submit_changes_error_message_5 = tk.messagebox.showinfo(title="Edit Vendor Invoice",message="Invoice amount cannot be blank.")

			else:

				with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

					cursor = connection.cursor()

					cursor.execute(edit_invoice_issue_date_sql_script,[new_invoice_issue_date,reference_vendor_name,reference_invoice_number])
					cursor.execute(edit_invoice_due_date_sql_script,[new_invoice_due_date,reference_vendor_name,reference_invoice_number])
					cursor.execute(edit_invoice_amount_sql_script,[new_invoice_amount,reference_vendor_name,reference_invoice_number])
					cursor.execute(edit_invoice_notes_sql_script,[new_invoice_notes,reference_vendor_name,reference_invoice_number])
					cursor.execute(edit_JE_date_sql_script,[new_invoice_issue_date,reference_vendor_name,reference_invoice_number])
					cursor.execute(edit_JE_debit_amount_sql_script,[new_invoice_amount,reference_vendor_name,reference_invoice_number])
					cursor.execute(edit_JE_credit_amount_sql_script,[new_invoice_amount,reference_vendor_name,reference_invoice_number])
					cursor.execute(edit_JE_notes_sql_script,[new_invoice_notes,reference_vendor_name,reference_invoice_number])

					connection.commit()

					cursor.close()

					edit_invoice_confirmation_message = tk.messagebox.showinfo(title="Edit Vendor Invoice",message="Successfully edited vendor invoice")

		except Exception as error:

			edit_invoice_error_message_2 = tk.messagebox.showinfo(title="Edit Vendor Invoice",message=f"{error}")


	def cancel_changes(self):

		try:

			self.invoice_issue_date_entry_text.set("")
			self.invoice_due_date_entry_text.set("")
			self.invoice_number_entry_text.set("")
			self.invoice_liability_GL_entry_text.set("")
			self.invoice_expense_GL_entry_text.set("")
			self.invoice_amount_entry_text.set("")
			self.invoice_notes_entry_text.set("")

		except Exception as error:

			cancel_changes_error_message_1 = tk.messagebox.showinfo(title="Edit Vendor Invoice",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
