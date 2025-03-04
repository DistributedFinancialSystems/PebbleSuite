#Python Standard Library dependencies

import datetime
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class EDIT_GL_WINDOW(tk.Toplevel):

	#Define class variables
	alive = False

	edit_selection_temporary_memory = []


	general_ledger_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers;'''


	#Define class functions
	def __init__(self,*args,**kwargs):

		options = ["Select General Ledger"]


		#Initialize SQL.db connection:
		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(self.general_ledger_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()
			cursor.close()


		#Define class tkinter widgets:
		super().__init__(*args,**kwargs)
		self.config(width=600,height=550)
		self.title("Edit General Ledger")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.general_ledger_name_label = ttk.Label(self,text="General Ledger Name")
		self.general_ledger_name_label.place(x=20,y=15)


		#Search for general ledger names in SQL.db.
		#Insert general ledger names into general ledger search listbox widget.
		self.select_general_ledger_scrollbar = ttk.Scrollbar(self)
		self.select_general_ledger_scrollbar.place(x=353,y=45,width=20,height=200)
		self.select_general_ledger_listbox = tk.Listbox(self,yscrollcommand=self.select_general_ledger_scrollbar.set)
		self.select_general_ledger_listbox.place(x=20,y=45,width=333,height=200)
		self.select_general_ledger_scrollbar.config(command=self.select_general_ledger_listbox.yview)


		search_general_ledger_name_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers;'''


		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(search_general_ledger_name_sql_script)
			connection.commit()

			for item in cursor:

				self.select_general_ledger_listbox.insert(0," ".join(item))

			cursor.close()


		self.edit_general_ledger_button = ttk.Button(self,text="Edit General Ledger",command=self.edit_general_ledger)
		self.edit_general_ledger_button.place(x=20,y=510)

		self.general_ledger_name_label = ttk.Label(self,text="General Ledger Name:")
		self.general_ledger_name_label.place(x=400,y=15)
		self.general_ledger_name_entry_text = tk.StringVar()
		self.general_ledger_name_entry = ttk.Entry(self,textvariable=self.general_ledger_name_entry_text)
		self.general_ledger_name_entry.place(x=400,y=45)

		self.general_ledger_number_label = ttk.Label(self,text="General Ledger Number:")
		self.general_ledger_number_label.place(x=400,y=185)
		self.general_ledger_number_entry_text = tk.StringVar()
		self.general_ledger_number_entry = ttk.Entry(self,textvariable=self.general_ledger_number_entry_text,state=tk.DISABLED)
		self.general_ledger_number_entry.place(x=400,y=215)

		self.general_ledger_type_label = ttk.Label(self,text="General Ledger Type:")
		self.general_ledger_type_label.place(x=400,y=1255)
		self.general_ledger_type_entry_text = tk.StringVar()
		self.general_ledger_type_entry = ttk.Entry(self,textvariable=self.general_ledger_type_entry_text,state=tk.DISABLED)
		self.general_ledger_type_entry.place(x=400,y=155)

		self.cancel_general_ledger_changes_button = ttk.Button(self,text="Close",command=self.cancel_changes)
		self.cancel_general_ledger_changes_button.place(x=490,y=510)

		self.submit_general_ledger_changes_button = ttk.Button(self,text="Save",command=self.submit_changes)
		self.submit_general_ledger_changes_button.place(x=400,y=510)


	def edit_general_ledger(self):

		#Define SQL.db scripts:
		query_general_ledger_sql_script = '''SELECT * FROM general_ledgers WHERE GENERAL_LEDGER_NAME=?'''


		for item in self.select_general_ledger_listbox.curselection():

			select_general_ledger = self.select_general_ledger_listbox.get(item)

		try:

			with sqlite3.connect("SQL.db") as connection:

				collect = []

				cursor = connection.cursor()
				cursor.execute(query_general_ledger_sql_script,[select_general_ledger])

				for item in cursor:
					collect.append(item)
					self.edit_selection_temporary_memory.append(item)

				self.general_ledger_name_entry_text.set(f"{collect[0][0]}")
				self.general_ledger_number_entry_text.set(f"{collect[0][1]}")
				self.general_ledger_type_entry_text.set(f"{collect[0][2]}")

				connection.commit()
				cursor.close()

		except sqlite3.Error as error:

			edit_general_ledger_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")


	def submit_changes(self):

		#Define SQL.db scripts:
		retrieve_general_ledger_sql_script = '''SELECT * FROM general_ledgers WHERE GENERAL_LEDGER_NAME=?;'''
		edit_general_ledger_name_sql_script = '''UPDATE general_ledgers SET GENERAL_LEDGER_NAME=? WHERE GENERAL_LEDGER_NAME=?;'''
		edit_general_ledger_number_sql_script = '''UPDATE general_ledgers SET GENERAL_LEDGER_NUMBER=? WHERE GENERAL_LEDGER_NAME=?;'''

		retrieve_journal_entries_sql_script = '''SELECT * FROM journal_entries WHERE GENERAL_LEDGER_NAME=?;'''
		edit_JE_GL_name_sql_script = '''UPDATE journal_entries SET GENERAL_LEDGER_NAME=? WHERE GENERAL_LEDGER_NAME=?'''
		edit_JE_GL_number_sql_script = '''UPDATE journal_entries SET GENERAL_LEDGER_NUMBER=? WHERE GENERAL_LEDGER_NUMBER=?'''


		#Define function variables:
		prev_general_ledger_name = self.edit_selection_temporary_memory[0][0]
		prev_general_ledger_number = self.edit_selection_temporary_memory[0][1]
		new_general_ledger_name = self.general_ledger_name_entry_text.get()
		new_general_ledger_number = self.general_ledger_number_entry_text.get()


		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()
				cursor.execute(edit_general_ledger_name_sql_script,(new_general_ledger_name,prev_general_ledger_name))
				cursor.execute(edit_general_ledger_number_sql_script,(new_general_ledger_number,prev_general_ledger_number))
				connection.commit()
				cursor.close()

		except sqlite3.Error as error:

			edit_general_ledger_error_message_2 = tk.messagebox.showinfo(title="Error",message=f"{error}")

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()
				cursor.execute(edit_JE_GL_name_sql_script,(new_general_ledger_name,prev_general_ledger_name))
				cursor.execute(edit_JE_GL_number_sql_script,(new_general_ledger_number,prev_general_ledger_number))
				connection.commit()
				cursor.close()
				edit_general_ledger_confirmation_message = tk.messagebox.showinfo("Edit General Ledger",message="General Ledger successfully edited.")

		except sqlite3.Error as error:

			edit_general_ledger_error_message_3 = tk.messagebox.showinfo(title="Error",message=f"{error}")

		#Clear temporary memory variable:
		self.edit_selection_temporary_memory.clear()
		self.general_ledger_name_entry_text.set("")
		self.general_ledger_number_entry_text.set("")
		self.general_ledger_type_entry_text.set("")


	def cancel_changes(self):

		try:

			self.general_ledger_name_entry_text.set("")
			self.general_ledger_number_entry_text.set("")
			self.general_ledger_type_entry_text.set("")

		except:

			cancel_changes_error_message = tk.messagebox.showinfo(title="Error",message="Unable to clear data entries.")


	def destroy(self):
		self.__class__.alive = False
		return super().destroy()
