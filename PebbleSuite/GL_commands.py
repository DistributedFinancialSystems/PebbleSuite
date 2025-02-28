#GL_commands.py

import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




"""
		NEW GL SECTION
"""




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

			try:
				cursor = connection.cursor()
				cursor.execute(new_GL_sql_script,self.new_GL_entry)
				connection.commit()
				cursor.close()

			except sqlite3.Error as error:
				print(f"NEW_GL_ENTRY ERROR: {error}")




class NEW_GL_WINDOW(tk.Toplevel):

	alive = False

	GL_types = ["Select GL Type","Select GL Type","Asset","Liability","Equity","Income","Expense"]

	def __init__(self,*args,**kwargs):

		super().__init__(*args,**kwargs)
		self.config(width=390,height=225)
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

		GL_data = []
		new_GL_name = self.GL_name_entry.get()
		GL_data.append(new_GL_name)
		new_GL_number = self.GL_number_entry.get()
		GL_data.append(new_GL_number)
		new_GL_type = self.clicked.get()
		GL_data.append(new_GL_type)

		try:
			#NEW_GL_ENTRY class from above.
			new_GL = NEW_GL_ENTRY(GL_data)
			new_GL.enter_data()
			new_GL_confirmation_message = tk.messagebox.showinfo(title="New General Ledger",message="New General Ledger created!")
			new_GL_restart_message = tk.messagebox.showinfo(title="New General Ledger",message="Restart PebbleSuite to update General Ledger search lists.")

		except sqlite3.Error as error:
			new_GL_error_message = tk.messagebox.showinfo(title="New General Ledger",message=f"Error: {error}")


	def print_GL_data(self):

		print_GL_sql_script = '''SELECT * FROM general_ledgers'''

		try:
			with sqlite3.connect("SQL.db") as connection:
				cursor = connection.cursor()
				cursor.execute(print_GL_sql_script)

				for item in cursor:
					print(item)

				connection.commit()
				cursor.close()

		except sqlite3.Error as error:
			print(f"print_GL_data error: {error}")


	def destroy(self):

		self.__class__.alive = False
		return super().destroy()



"""
		EDIT VENDOR SECTION
"""




class EDIT_GL_WINDOW(tk.Toplevel):

	#Define class admin variables

	GL_data = []

	alive = False

	GL_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers;'''

	GL_options = ["Select General Ledger","Select General Ledger"]


	#Search for GL data in SQL.db.

	try:

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(GL_sql_script)

			for item in cursor:
				GL_options.append(item)

			connection.commit()
			cursor.close()

	except sqlite3.Error as error:

		display_GL_data_error_message = tk.messagebox.showinfo(title="Display General Ledgers",message=f"Error: {error}")

	#Define tkinter widgets for EDIT_GL_WINDOW().

	def __init__(self,*args,**kwargs):

		super().__init__(*args,**kwargs)
		self.config(width=390,height=265)
		self.title("Edit General Ledger")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{self.GL_options[0]}")

		self.GL_option_menu_label = ttk.Label(self,text="Select General Ledger:")
		self.GL_option_menu_label.place(x=20,y=20)
		self.GL_option_menu = ttk.OptionMenu(self,self.clicked,*self.GL_options)
		self.GL_option_menu.place(x=200,y=20)

		self.GL_name_label = ttk.Label(self,text="General Ledger Name:")
		self.GL_name_label.place(x=20,y=60)
		self.GL_name_entry_text = tk.StringVar()
		self.GL_name_entry = ttk.Entry(self,textvariable=self.GL_name_entry_text)
		self.GL_name_entry.place(x=200,y=60)

		self.GL_number_label = ttk.Label(self,text="General Ledger Number:")
		self.GL_number_label.place(x=20,y=100)
		self.GL_number_entry_text = tk.StringVar()
		self.GL_number_entry = ttk.Entry(self,textvariable=self.GL_number_entry_text)
		self.GL_number_entry.place(x=200,y=100)

		self.GL_type_label = ttk.Label(self,text="General Ledger Type is not editable.")
		self.GL_type_label.place(x=20,y=140)

		self.search_GL_data_button = ttk.Button(self,text="Retrieve GL Data",command=self.search_GL_data)
		self.search_GL_data_button.place(x=20,y=220)

		self.change_GL_data_button = ttk.Button(self,text="Submit Data Changes",command=self.change_GL_data)
		self.change_GL_data_button.place(x=200,y=220)

	def search_GL_data(self):

		#Define function's admin variables

		search_GL_name = self.clicked.get()
		search_GL_sql_script = '''SELECT * FROM general_ledgers WHERE GENERAL_LEDGER_NAME=?'''

		#Search for data in SQL.db for specified GL.

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()
				cursor.execute(search_GL_sql_script,[search_GL_name])

				data_format1 = [*cursor]
				data_format2 = str(data_format1)
				data_format3 = data_format2.split(",")

				self.GL_name_entry_text.set(f"{data_format3[0]}")
				self.GL_number_entry_text.set(f"{data_format3[1]}")

				connection.commit()
				cursor.close()

			search_GL_confirmation_message = tk.messagebox.showinfo(title="Search General Ledger",message="GL data retrieved")

		except sqlite3.Error as error:

			search_GL_error_message = tk.messagebox.showinfo(title="Search General Ledger",message=f"Error: {error}")


	def change_GL_data(self):

		#Define function's admin variables

		search_GL_name = self.clicked.get()
		retrieve_GL_sql_script = '''SELECT * FROM general_ledgers;'''
		edit_GL_name_sql_script = '''UPDATE general_ledgers SET GENERAL_LEDGER_NAME=? WHERE GENERAL_LEDGER_NAME=?;'''
		edit_GL_number_sql_script = '''UPDATE general_ledgers SET GENERAL_LEDGER_NUMBER=? WHERE GENERAL_LEDGER_NAME=?'''
		new_GL_name = self.GL_name_entry.get()
		new_GL_number = self.GL_number_entry.get()

		#Update data in SQL.db for specified GL.

		try:

			with sqlite3.connect("SQL.db") as connection:
				cursor = connection.cursor()
				cursor.execute(edit_GL_number_sql_script,(new_GL_number,search_GL_name))
				cursor.execute(edit_GL_name_sql_script,(new_GL_name,search_GL_name))
				connection.commit()
				cursor.close()

			edit_GL_confirmation_message = tk.messagebox.showinfo(title="Edit General Ledger",message="General Ledger changes successful")
			edit_GL_restart_message = tk.messagebox.showinfo(title="Edit General Ledger",message="Restart PebbleSuite to update General Ledger search lists.")

		except sqlite3.Error as error:

			edit_GL_error_message = tk.messagebox.showinfo(title="Edit General Ledger",message=f"Error: {error}")


	def destroy(self):

		self.__class__.alive = False
		return super().destroy()



"""
		DELETE GL SECTION
"""
