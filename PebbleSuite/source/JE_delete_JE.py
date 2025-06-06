import datetime
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class DELETE_GL_WINDOW(tk.Toplevel):

	alive = False

	delete_selection_temporary_memory = []

	general_ledger_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers;'''

	def __init__(self,*args,**kwargs):

		options = ["Select General Ledger"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.general_ledger_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()

		super().__init__(*args,**kwargs)
		self.config(width=600,height=270)
		self.title("Delete General Ledger")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.general_ledger_name_label = ttk.Label(self,text="General Ledger Name:")
		self.general_ledger_name_label.place(x=20,y=15)

		self.select_general_ledger_scrollbar = ttk.Scrollbar(self)
		self.select_general_ledger_scrollbar.place(x=353,y=45,width=20,height=170)
		self.select_general_ledger_listbox = tk.Listbox(self,yscrollcommand=self.select_general_ledger_scrollbar.set)
		self.select_general_ledger_listbox.place(x=20,y=45,width=333,height=170)
		self.select_general_ledger_scrollbar.config(command=self.select_general_ledger_listbox.yview)

		search_general_ledger_name_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers;'''


		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(search_general_ledger_name_sql_script)

			connection.commit()

			for item in cursor:

				self.select_general_ledger_listbox.insert(0," ".join(item))

			cursor.close()


		self.delete_general_ledger_button = ttk.Button(self,text="Select General Ledger",command=self.delete_general_ledger)
		self.delete_general_ledger_button.place(x=20,y=230)

		self.general_ledger_name_label = ttk.Label(self,text="General Ledger Name:")
		self.general_ledger_name_label.place(x=400,y=15)
		self.general_ledger_name_entry_text = tk.StringVar()
		self.general_ledger_name_entry = ttk.Entry(self,textvariable=self.general_ledger_name_entry_text,width=21)
		self.general_ledger_name_entry.place(x=400,y=45)

		self.general_ledger_number_label = ttk.Label(self,text="General Ledger Number:")
		self.general_ledger_number_label.place(x=400,y=85)
		self.general_ledger_number_entry_text = tk.StringVar()
		self.general_ledger_number_entry = ttk.Entry(self,textvariable=self.general_ledger_number_entry_text,state=tk.DISABLED,width=21)
		self.general_ledger_number_entry.place(x=400,y=115)

		self.general_ledger_type_label = ttk.Label(self,text="General Ledger Type:")
		self.general_ledger_type_label.place(x=400,y=155)
		self.general_ledger_type_entry_text = tk.StringVar()
		self.general_ledger_type_entry = ttk.Entry(self,textvariable=self.general_ledger_type_entry_text,state=tk.DISABLED,width=21)
		self.general_ledger_type_entry.place(x=400,y=185)

		self.cancel_general_ledger_changes_button = ttk.Button(self,text="Cancel",command=self.cancel_changes)
		self.cancel_general_ledger_changes_button.place(x=490,y=230)

		self.submit_general_ledger_changes_button = ttk.Button(self,text="Delete",command=self.submit_changes)
		self.submit_general_ledger_changes_button.place(x=400,y=230)


	def delete_general_ledger(self):

		try:

			query_general_ledger_sql_script = '''SELECT * FROM general_ledgers WHERE GENERAL_LEDGER_NAME=?'''

			for item in self.select_general_ledger_listbox.curselection():

				select_general_ledger = self.select_general_ledger_listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				collect = []

				cursor = connection.cursor()

				cursor.execute(query_general_ledger_sql_script,[select_general_ledger])

				for item in cursor:

					collect.append(item)

					self.delete_selection_temporary_memory.append(item)

				self.general_ledger_name_entry_text.set(f"{collect[0][0]}")
				self.general_ledger_number_entry_text.set(f"{collect[0][1]}")
				self.general_ledger_type_entry_text.set(f"{collect[0][2]}")

				connection.commit()

				cursor.close()

		except Exception as error:

			delete_general_ledger_error_message_1 = tk.messagebox.showinfo(title="Delete General Ledger",message=f"{error}")


	def submit_changes(self):

		try:

			#general_ledgers SQL scripts:
			retrieve_general_ledger_sql_script = '''SELECT * FROM general_ledgers WHERE GENERAL_LEDGER_NAME=?;'''
			delete_general_ledger_name_sql_script = '''DELETE FROM general_ledgers WHERE GENERAL_LEDGER_NAME=?;'''

			#journal_entries SQL scripts:
			retrieve_journal_entries_sql_script = '''SELECT * FROM journal_entries WHERE GENERAL_LEDGER_NAME=?;'''
			delete_JE_debit_GL_name_sql_script = '''DELETE FROM journal_entries WHERE DEBIT_GENERAL_LEDGER_NAME=?;'''
			delete_JE_credit_GL_name_sql_script = '''DELETE FROM journal_entries WHERE CREDIT_GENERAL_LEDGER_NAME=?;'''

			#vendor_invoices SQL scripts:
			retrieve_vendor_invoices_sql_script_1 = '''SELECT * FROM vendor_invoices WHERE INVOICE_LIABILITY_ACCOUNT=?;'''
			retrieve_vendor_invoices_sql_script_2 = '''SELECT * FROM vendor_invoices WHERE INVOICE_EXPENSE_ACCOUNT=?;'''
			delete_vendor_invoices_sql_script_1 = '''DELETE FROM vendor_invoices WHERE INVOICE_LIABILITY_ACCOUNT=?;'''
			delete_vendor_invoices_sql_script_2 = '''DELETE FROM vendor_invoices WHERE INVOICE_EXPENSE_ACCOUNT=?;'''

			#client_invoices SQL scripts:
			retrieve_client_invoices_sql_script_1 = '''SELECT * FROM client_invoices WHERE INVOICE_ASSET_ACCOUNT=?;'''
			retrieve_client_invoices_sql_script_2 = '''SELECT * FROM client_invoices WHERE INVOICE_INCOME_ACCOUNT=?;'''
			delete_client_invoices_sql_script_1 = '''DELETE FROM client_invoices WHERE INVOICE_ASSET_ACCOUNT=?;'''
			delete_client_invoices_sql_script_2 = '''DELETE FROM client_invoices WHERE INVOICE_INCOME_ACCOUNT=?;'''

			#vendor_credit_memos SQL scripts:
			retrieve_vendor_credit_memos_sql_script_1 = '''SELECT * FROM vendor_credit_memos WHERE CREDIT_MEMO_ASSET_ACCOUNT=?;'''
			retrieve_vendor_credit_memos_sql_script_2 = '''SELECT * FROM vendor_credit_memos WHERE CREDIT_MEMO_INCOME_ACCOUNT=?;'''
			delete_vendor_credit_memos_sql_script_1 = '''DELETE FROM vendor_credit_memos WHERE CREDIT_MEMO_ASSET_ACCOUNT=?;'''
			delete_vendor_credit_memos_sql_script_2 = '''DELETE FROM vendor_credit_memos WHERE CREDIT_MEMO_INCOME_ACCOUNT=?;'''

			#client_credit_memos SQL scripts:
			retrieve_client_credit_memos_sql_script_1 = '''SELECT * FROM client_credit_memos WHERE CREDIT_MEMO_LIABILITY_ACCOUNT=?;'''
			retrieve_client_credit_memos_sql_script_2 = '''SELECT * FROM client_credit_memos WHERE CREDIT_MEMO_EXPENSE_ACCOUNT=?;'''
			delete_client_credit_memos_sql_script_1 = '''DELETE FROM client_credit_memos WHERE CREDIT_MEMO_LIABILITY_ACCOUNT=?;'''
			delete_client_credit_memos_sql_script_2 = '''DELETE FROM client_credit_memos WHERE CREDIT_MEMO_EXPENSE_ACCOUNT=?;'''

			prev_general_ledger_name = self.delete_selection_temporary_memory[0][0]
			prev_general_ledger_number = self.delete_selection_temporary_memory[0][1]

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(retrieve_general_ledger_sql_script,[prev_general_ledger_name])
				cursor.execute(delete_general_ledger_name_sql_script,[prev_general_ledger_name])

				delete_general_ledger_confirmation_message_1 = tk.messagebox.showinfo(title="Delete General Ledger",message="General Ledger data deleted")

				cursor.execute(retrieve_general_ledger_sql_script,[prev_general_ledger_name])
				cursor.execute(delete_JE_debit_GL_name_sql_script,[prev_general_ledger_name])
				cursor.execute(delete_JE_credit_GL_name_sql_script,[prev_general_ledger_name])

				delete_journal_entries_confirmation_message_1 = tk.messagebox.showinfo(title="Delete General Ledger",message="Journal Entries successfully deleted")

				cursor.execute(retrieve_vendor_invoices_sql_script_1,[prev_general_ledger_name])
				cursor.execute(delete_vendor_invoices_sql_script_1,[prev_general_ledger_name])
				cursor.execute(retrieve_vendor_invoices_sql_script_2,[prev_general_ledger_name])
				cursor.execute(delete_vendor_invoices_sql_script_2,[prev_general_ledger_name])

				delete_vendor_invoices_confirmation_message_1 = tk.messagebox.showinfo(title="Delete General Ledger",message="Vendor Invoice data successfully deleted")

				cursor.execute(retrieve_client_invoices_sql_script_1,[prev_general_ledger_name])
				cursor.execute(delete_client_invoices_sql_script_1,[prev_general_ledger_name])
				cursor.execute(retrieve_client_invoices_sql_script_2,[prev_general_ledger_name])
				cursor.execute(delete_client_invoices_sql_script_2,[prev_general_ledger_name])

				delete_client_invoices_confirmation_message_1 = tk.messagebox.showinfo(title="Delete General Ledger",message="Client Invoice data successfully deleted")

				cursor.execute(retrieve_vendor_credit_memos_sql_script_1,[prev_general_ledger_name])
				cursor.execute(retrieve_vendor_credit_memos_sql_script_2,[prev_general_ledger_name])
				cursor.execute(delete_vendor_credit_memos_sql_script_1,[prev_general_ledger_name])
				cursor.execute(delete_vendor_credit_memos_sql_script_2,[prev_general_ledger_name])

				delete_vendor_credit_memos_confirmation_message_1 = tk.messagebox.showinfo(title="Delete General Ledger",message="Vendor credit memo data successfully deleted.")

				cursor.execute(retrieve_client_credit_memos_sql_script_1,[prev_general_ledger_name])
				cursor.execute(retrieve_client_credit_memos_sql_script_2,[prev_general_ledger_name])
				cursor.execute(delete_client_credit_memos_sql_script_1,[prev_general_ledger_name])
				cursor.execute(delete_client_credit_memos_sql_script_2,[prev_general_ledger_name])

				delete_client_credit_memos_confirmation_message_1 = tk.messagebox.showinfo(title="Delete General Ledger",message="Client credit memo data successfully deleted.")

				connection.commit()

				cursor.close()

			self.delete_selection_temporary_memory.clear()
			self.general_ledger_name_entry_text.set("")
			self.general_ledger_number_entry_text.set("")
			self.general_ledger_type_entry_text.set("")

		except Exception as error:

			temporary_memory_error_message_1 = tk.messagebox.showinfo(title="Delete General Ledger",message=f"{error}")


	def cancel_changes(self):

		try:

			self.general_ledger_name_entry_text.set("")
			self.general_ledger_number_entry_text.set("")
			self.general_ledger_type_entry_text.set("")

		except Exception as error:

			cancel_changes_error_message = tk.messagebox.showinfo(title="Delete General Ledger",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
