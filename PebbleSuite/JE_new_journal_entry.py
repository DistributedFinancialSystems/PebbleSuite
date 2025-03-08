"""
[ ]
[ ]
[ ]
[ ]	JE_new_journal_entry.py
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

"""
[ ]
[ ]
[ ]
[ ]	NEW JOURNAL ENTRY CLASS
[ ]
[ ]
[ ]
"""

journal_entry_queue = 0


class NEW_JOURNAL_ENTRY:

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
					INVOICE_NUMBER,
					GENERAL_LEDGER_NAME,
					GENERAL_LEDGER_NUMBER,
					GENERAL_LEDGER_TYPE,
					OFFSET_GENERAL_LEDGER_NAME,
					OFFSET_GENERAL_LEDGER_TYPE,
					JOURNAL_ENTRY_DEBIT_AMOUNT,
					JOURNAL_ENTRY_CREDIT_AMOUNT,
					JOURNAL_ENTRY_NAME,
					JOURNAL_ENTRY_NOTES)
					VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);'''

		with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

			try:
				cursor = connection.cursor()
				cursor.execute(new_debit_JE_sql_script,self.new_journal_entry)
				connection.commit()
				cursor.close()

			except sqlite3.Error as error:
				print(f"debit_entry errror: {error}")

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
					INVOICE_NUMBER,
					GENERAL_LEDGER_NAME,
					GENERAL_LEDGER_NUMBER,
					GENERAL_LEDGER_TYPE,
					OFFSET_GENERAL_LEDGER_NAME,
					OFFSET_GENERAL_LEDGER_TYPE,
					JOURNAL_ENTRY_DEBIT_AMOUNT,
					JOURNAL_ENTRY_CREDIT_AMOUNT,
					JOURNAL_ENTRY_NAME,
					JOURNAL_ENTRY_NOTES)
					VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);'''

		with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

			try:
				cursor = connection.cursor()
				cursor.execute(new_credit_JE_sql_script,self.new_journal_entry)
				connection.commit()
				cursor.close()

			except sqlite3.Error as error:
				print(f"credit_entry error: {error}")

"""
[ ]
[ ]
[ ]
[ ]	NEW_JE_WINDOW CLASS
[ ]
[ ]
[ ]
"""

class NEW_JE_WINDOW(tk.Toplevel):

	GL_data = []

	alive = False

	GL_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers;'''

	GL_options = ["Select General Ledger"]

	#Search for GL data in SQL.db.

	try:

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(GL_sql_script)

			for item in cursor:
				GL_options.append(" ".join(item))

			connection.commit()
			cursor.close()

	except sqlite3.Error as error:

		display_GL_data_error_message = tk.messagebox.showinfo(title="Display General Ledgers",message=f"Error: {error}")

	#Define tkinter widgets for NEW_JE_WINDOW().

	def __init__(self,*args,**kwargs):

		super().__init__(*args,**kwargs)
		self.config(width=800,height=710)
		self.title("New Journal Entry")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.JE_date_label = ttk.Label(self,text="Journal Entry Date")
		self.JE_date_label.place(x=20,y=20)
		self.JE_date_entry = ttk.Entry(self)
		self.JE_date_entry.place(x=20,y=45)

		self.JE_number_label = ttk.Label(self,text="Journal Entry Number")
		self.JE_number_label.place(x=220,y=20)
		self.JE_number_entry_text = tk.StringVar()
		self.JE_number_entry_text.set(journal_entry_queue)
		self.JE_number_entry = ttk.Entry(self,textvariable=self.JE_number_entry_text,state=tk.DISABLED)
		self.JE_number_entry.place(x=220,y=45)

		self.debit = tk.StringVar()
		self.debit.set(f"{self.GL_options[0]}")

		self.credit = tk.StringVar()
		self.credit.set(f"{self.GL_options[0]}")

		self.debit_GL_option_menu_label = ttk.Label(self,text="Debit General Ledger")
		self.debit_GL_option_menu_label.place(x=20,y=100)
		self.debit_GL_option_menu = ttk.OptionMenu(self,self.debit,self.GL_options[0],*self.GL_options)
		self.debit_GL_option_menu.place(x=20,y=125)
		self.debit_GL_amount_label = ttk.Label(self,text="Debit Amount")
		self.debit_GL_amount_label.place(x=220,y=100)
		self.debit_GL_entry = ttk.Entry(self)
		self.debit_GL_entry.place(x=220,y=125)

		self.credit_GL_option_menu_label = ttk.Label(self,text="Credit General Ledger")
		self.credit_GL_option_menu_label.place(x=420,y=100)
		self.credit_GL_option_menu = ttk.OptionMenu(self,self.credit,self.GL_options[0],*self.GL_options)
		self.credit_GL_option_menu.place(x=420,y=125)
		self.credit_GL_amount_label = ttk.Label(self,text="Credit Amount")
		self.credit_GL_amount_label.place(x=620,y=100)
		self.credit_GL_entry = ttk.Entry(self)
		self.credit_GL_entry.place(x=620,y=125)

		self.JE_notes_label = ttk.Label(self,text="Journal Entry Notes")
		self.JE_notes_label.place(x=420,y=20)
		self.JE_notes_entry = ttk.Entry(self,width=45)
		self.JE_notes_entry.place(x=420,y=45)

		self.new_JE_button = ttk.Button(self,text="Enter Journal Entry",command=self.create_new_JE)
		self.new_JE_button.place(x=20,y=600)

		self.print_JE_button = ttk.Button(self,text="Print Journal Entries",command=self.print_journal_entries)
		self.print_JE_button.place(x=200,y=600)

	"""
	[ ]
	[ ]
	[ ]
	[ ]	CREATE_NEW_JE FUNCTION:
	[ ]
	[ ]
	[ ]
	"""

	def create_new_JE(self):

		#Define debit data list and credit data list:
		debit_JE_data = []
		credit_JE_data = []

		#Retrieve journal entry data:
		new_JE_timestamp = datetime.datetime.now()
		new_JE_number = self.JE_number_entry.get()
		new_JE_date = self.JE_date_entry.get()

		new_invoice_number = None

		new_debit_GL_name = self.debit.get()
		new_credit_GL_name = self.credit.get()

		new_GL_number = None
		new_GL_type = None

		new_offset_GL_name_2 = self.credit.get()
		new_offset_GL_name_1 = self.debit.get()

		new_offset_GL_number = None
		new_offset_GL_type = None

		new_GL_debit = self.debit_GL_entry.get()
		new_GL_credit = self.credit_GL_entry.get()

		new_JE_name = None
		new_JE_notes = self.JE_notes_entry.get()


		if new_debit_GL_name == "Select General Ledger":

			select_debit_GL_error_message = tk.messagebox.showinfo(title="Error",message="Please select a general ledger.")

		elif new_credit_GL_name == "Select General Ledger":

			select_credit_GL_error_message = tk.messagebox.showinfo(title="Error",message="Please select a general ledger.")

		elif new_GL_debit != new_GL_credit:

			matching_values_error_message = tk.messagebox.showinfo(title="Error",message="Journal entry values must be equal.")

		else:

			debit_JE_data.append(new_JE_timestamp)
			debit_JE_data.append(new_JE_number)
			debit_JE_data.append(new_JE_date)
			debit_JE_data.append(new_invoice_number)
			debit_JE_data.append(new_debit_GL_name)
			debit_JE_data.append(new_GL_number)
			debit_JE_data.append(new_GL_type)
			debit_JE_data.append(new_offset_GL_name_2)
			#debit_JE_data.append(new_offset_GL_number)
			debit_JE_data.append(new_offset_GL_type)
			debit_JE_data.append(new_GL_debit)
			debit_JE_data.append(0)
			debit_JE_data.append(new_JE_name)
			debit_JE_data.append(new_JE_notes)

			credit_JE_data.append(new_JE_timestamp)
			credit_JE_data.append(new_JE_number)
			credit_JE_data.append(new_JE_date)
			credit_JE_data.append(new_invoice_number)
			credit_JE_data.append(new_credit_GL_name)
			credit_JE_data.append(new_GL_number)
			credit_JE_data.append(new_GL_type)
			credit_JE_data.append(new_offset_GL_name_1)
			#credit_JE_data.append(new_offset_GL_number)
			credit_JE_data.append(new_offset_GL_type)
			credit_JE_data.append(0)
			credit_JE_data.append(new_GL_credit)
			credit_JE_data.append(new_JE_name)
			credit_JE_data.append(new_JE_notes)

			try:

				#NEW_JE_ENTRY class from above.
				new_debit = NEW_JOURNAL_ENTRY(debit_JE_data)
				new_credit = NEW_JOURNAL_ENTRY(credit_JE_data)
				new_debit.debit_entry()
				new_credit.credit_entry()

				new_JE_confirmation_message = tk.messagebox.showinfo(title="New Journal Entry",message="New journal entry successfully entered.")

			except sqlite3.Error as error:

				print(error)

	"""
	[ ]
	[ ]
	[ ]
	[ ]	PRINT_JOURNAL_ENTRIES FUNCTION:
	[ ]
	[ ]
	[ ]
	"""

	def print_journal_entries(self):

		search_JE_data = '''SELECT * FROM journal_entries;'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(search_JE_data)

			for item in cursor:
				print(item)

			connection.commit()
			cursor.close()

	"""
	[ ]
	[ ]
	[ ]
	[ ]	DESTROY FUNCTION:
	[ ]
	[ ]
	[ ]
	"""

	def destroy(self):

		self.__class__.alive = False
		return super().destroy()
