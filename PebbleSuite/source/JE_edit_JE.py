import datetime
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class EDIT_JE_WINDOW(tk.Toplevel):

	alive = False

	edit_selection_temporary_memory = []

	journal_entry_sql_script = '''SELECT JOURNAL_ENTRY_NUMBER FROM journal_entries;'''


	def __init__(self,*args,**kwargs):

		options = ["Select Journal Entry"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.journal_entry_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()

		"""
		_______________________
		DEFINE TKINTER WIDGETS:
		_______________________
		"""

		super().__init__(*args,**kwargs)
		self.config(width=600,height=265)
		self.title("Edit Journal Entry")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.journal_entry_name_label = ttk.Label(self,text="Journal Entry Name:")
		self.journal_entry_name_label.place(x=20,y=15)

		self.select_journal_entry_scrollbar = ttk.Scrollbar(self)
		self.select_journal_entry_scrollbar.place(x=353,y=45,width=20,height=170)
		self.select_journal_entry_listbox = tk.Listbox(self,yscrollcommand=self.select_journal_entry_scrollbar.set)
		self.select_journal_entry_listbox.place(x=20,y=45,width=333,height=170)
		self.select_journal_entry_scrollbar.config(command=self.select_journal_entry_listbox.yview)

		search_journal_entry_name_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM journal_entries;'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(search_journal_entry_name_sql_script)

			connection.commit()

			for item in cursor:

				self.select_journal_entry_listbox.insert(0," ".join(item))

			cursor.close()

		self.edit_journal_entry_button = ttk.Button(self,text="Edit Journal Entry",command=self.edit_journal_entry)
		self.edit_journal_entry_button.place(x=20,y=230)

		self.journal_entry_name_label = ttk.Label(self,text="Journal Entry Name:")
		self.journal_entry_name_label.place(x=400,y=15)
		self.journal_entry_name_entry_text = tk.StringVar()
		self.journal_entry_name_entry = ttk.Entry(self,textvariable=self.journal_entry_name_entry_text,width=21)
		self.journal_entry_name_entry.place(x=400,y=45)

		self.journal_entry_number_label = ttk.Label(self,text="Journal Entry Number:")
		self.journal_entry_number_label.place(x=400,y=85)
		self.journal_entry_number_entry_text = tk.StringVar()
		self.journal_entry_number_entry = ttk.Entry(self,textvariable=self.journal_entry_number_entry_text,state=tk.DISABLED,width=21)
		self.journal_entry_number_entry.place(x=400,y=115)

		self.journal_entry_type_label = ttk.Label(self,text="Journal Entry Type:")
		self.journal_entry_type_label.place(x=400,y=155)
		self.journal_entry_type_entry_text = tk.StringVar()
		self.journal_entry_type_entry = ttk.Entry(self,textvariable=self.journal_entry_type_entry_text,state=tk.DISABLED,width=21)
		self.journal_entry_type_entry.place(x=400,y=185)

		self.cancel_journal_entry_changes_button = ttk.Button(self,text="Cancel",command=self.cancel_changes)
		self.cancel_journal_entry_changes_button.place(x=490,y=230)

		self.submit_journal_entry_changes_button = ttk.Button(self,text="Save",command=self.submit_changes)
		self.submit_journal_entry_changes_button.place(x=400,y=230)


	def edit_journal_entry(self):

		try:

			query_journal_entry_sql_script = '''SELECT * FROM journal_entries WHERE JOURNAL_ENTRY_NUMBER=?'''

			for item in self.select_journal_entry_listbox.curselection():

				select_journal_entry = self.select_journal_entry_listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				collect = []

				cursor = connection.cursor()

				cursor.execute(query_journal_entry_sql_script,[select_journal_entry])

				for item in cursor:

					collect.append(item)

					self.edit_selection_temporary_memory.append(item)

				self.journal_entry_name_entry_text.set(f"{collect[0][0]}")
				self.journal_entry_number_entry_text.set(f"{collect[0][1]}")
				self.journal_entry_type_entry_text.set(f"{collect[0][2]}")

				connection.commit()

				cursor.close()

		except Exception as error:

			edit_journal_entry_error_message = tk.messagebox.showinfo(title="Edit Journal Entry",message=f"{error}")


	def submit_changes(self):

		try:

			retrieve_journal_entry_sql_script = '''SELECT * FROM journal_entries WHERE GENERAL_LEDGER_NAME=?;'''
			edit_journal_entry_name_sql_script = '''UPDATE journal_entries SET GENERAL_LEDGER_NAME=? WHERE GENERAL_LEDGER_NAME=?;'''

			retrieve_debit_journal_entries_sql_script = '''SELECT * FROM journal_entries WHERE DEBIT_GENERAL_LEDGER_NAME=?;'''
			edit_JE_debit_GL_name_sql_script = '''UPDATE journal_entries SET DEBIT_GENERAL_LEDGER_NAME=? WHERE DEBIT_GENERAL_LEDGER_NAME=?'''

			retrieve_credit_journal_entries_sql_script = '''SELECT * FROM journal_entries WHERE CREDIT_GENERAL_LEDGER_NAME=?;'''
			edit_JE_credit_GL_name_sql_script = '''UPDATE journal_entries SET CREDIT_GENERAL_LEDGER_NAME=? WHERE CREDIT_GENERAL_LEDGER_NAME=?;'''

			prev_journal_entry_name = self.edit_selection_temporary_memory[0][0]

			new_journal_entry_name = self.journal_entry_name_entry_text.get()

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(edit_journal_entry_name_sql_script,(new_journal_entry_name,prev_journal_entry_name))

				edit_journal_entry_names_confirmation_message = tk.messagebox.showinfo("Edit Journal Entry",message="Journal Entry Name successfully changed.")

				cursor.execute(retrieve_debit_journal_entries_sql_script,[prev_journal_entry_name])
				cursor.execute(edit_JE_debit_GL_name_sql_script,(new_journal_entry_name,prev_journal_entry_name))

				edit_debit_journal_entry_names_confirmation_message = tk.messagebox.showinfo("Edit Journal Entry",message="Journal Entry debit journal entry names successfully changed.")

				cursor.execute(retrieve_credit_journal_entries_sql_script,[prev_journal_entry_name])
				cursor.execute(edit_JE_credit_GL_name_sql_script,(new_journal_entry_name,prev_journal_entry_name))

				edit_credit_journal_entry_names_confirmation_message = tk.messagebox.showinfo("Edit Journal Entry",message="Journal Entry credit journal entry names successfully changed.")

				connection.commit()

				cursor.close()

				self.edit_selection_temporary_memory.clear()

				self.journal_entry_name_entry_text.set("")
				self.journal_entry_number_entry_text.set("")
				self.journal_entry_type_entry_text.set("")

				edit_journal_entry_data_confirmation_message = tk.messagebox.showinfo(title="Edit Journal Entry",message="Journal Entry data successfully changed.")

		except Exception as error:

			edit_credit_journal_entry_names_error_message = tk.messagebox.showinfo(title="Edit Journal Entry",message=f"{error}")


	def cancel_changes(self):

		try:

			self.edit_selection_temporary_memory.clear()

			self.journal_entry_name_entry_text.set("")
			self.journal_entry_number_entry_text.set("")
			self.journal_entry_type_entry_text.set("")

		except Exception as error:

			cancel_changes_error_message = tk.messagebox.showinfo(title="Edit Journal Entry",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
