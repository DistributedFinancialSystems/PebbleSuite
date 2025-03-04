"""
[ ]
[ ]
[ ]
[ ]	GL_new_GL.py
[ ]
[ ]
[ ]
"""
"""
[ ]
[ ]
[ ]
[ ]	IMPORT PYTHON DEPENDENCIES
[ ]
[ ]
[ ]
"""


import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo


"""
[ ]
[ ]
[ ]
[ ]	NEW_GL_ENTRY CLASS
[ ]
[ ]
[ ]
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


"""
[ ]
[ ]
[ ]
[ ]	NEW_GL_WINDOW CLASS
[ ]
[ ]
[ ]
"""


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
