import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class NEW_GL_ENTRY:

	def __init__(self,new_GL_entry):

		self.new_GL_entry = new_GL_entry

	def enter_data(self):

		new_GL_sql_script = '''INSERT INTO general_ledgers(
					GENERAL_LEDGER_NAME,
					GENERAL_LEDGER_NUMBER,
					GENERAL_LEDGER_TYPE)
					VALUES(?,?,?);'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(new_GL_sql_script,self.new_GL_entry)

			connection.commit()

			cursor.close()




class NEW_GL_WINDOW(tk.Toplevel):

	alive = False

	GL_types = 	[
			"Select GL Type",
			"Select GL Type",
			"Asset - Bank Account",
			"Asset - Inventory",
			"Asset - Accounts Receivable",
			"Asset - Fixed Asset",
			"Asset - Other",
			"Liability - Accounts Payable",
			"Liability - Notes Payable",
			"Liability - Long-Term Debt",
			"Liability - Other",
			"Equity - Owner's Equity",
			"Equity - Other Investment",
			"Income - Sales Income",
			"Income - Other Income",
			"Expense - Direct Expense",
			"Expense - Indirect Expense"
			]

	def __init__(self,*args,**kwargs):

		super().__init__(*args,**kwargs)
		self.config(width=425,height=225)
		self.title("New General Ledger")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.GL_name_label = ttk.Label(self,text="General Ledger Name:")
		self.GL_name_label.place(x=20,y=20)
		self.GL_name_entry = ttk.Entry(self)
		self.GL_name_entry.place(x=200,y=20)

		self.GL_number_label = ttk.Label(self,text="General Ledger Number:")
		self.GL_number_label.place(x=20,y=60)
		self.GL_number_entry = ttk.Entry(self)
		self.GL_number_entry.place(x=200,y=60)

		self.GL_type_label = ttk.Label(self,text="General Ledger Type:")
		self.GL_type_label.place(x=20,y=100)
		self.clicked = tk.StringVar()
		self.clicked.set(f"{self.GL_types[0]}")
		self.GL_option_menu = ttk.OptionMenu(self,self.clicked,*self.GL_types)
		self.GL_option_menu.place(x=200,y=100)

		self.new_GL_button = ttk.Button(self,text="New General Ledger",command=self.create_new_GL)
		self.new_GL_button.place(x=20,y=180)

		self.print_GL_button = ttk.Button(self,text="Print General Ledgers",command=self.print_GL_data)
		self.print_GL_button.place(x=200,y=180)


	def create_new_GL(self):

		try:

			GL_data = []

			new_GL_name = self.GL_name_entry.get()
			GL_data.append(new_GL_name)
			new_GL_number = self.GL_number_entry.get()
			GL_data.append(new_GL_number)
			new_GL_type = self.clicked.get()
			GL_data.append(new_GL_type)

			GL_names = []

			verify_GL_names_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers;'''

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(verify_GL_names_sql_script)

				for item in cursor:

					GL_names.append(*item)

				connection.commit()

				cursor.close()

			if new_GL_name in GL_names:

				duplicate_GL_name_error_message = tk.messagebox.showinfo(title="New General Ledger",message="Duplicate GL name:  please use a different name for new GL.")

			else:

				new_GL = NEW_GL_ENTRY(GL_data)
				new_GL.enter_data()
				new_GL_confirmation_message = tk.messagebox.showinfo(title="New General Ledger",message="New General Ledger created!")

		except Exception as error:

			new_GL_error_message = tk.messagebox.showinfo(title="New General Ledger",message=f"{error}")


	def print_GL_data(self):

		try:

			print_GL_sql_script = '''SELECT * FROM general_ledgers'''

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(print_GL_sql_script)

				for item in cursor:

					print(item)

				connection.commit()

				cursor.close()

		except Exception as error:

			print_GL_data_error_message = tk.messagebox.showinfo(title="New General Ledger",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
