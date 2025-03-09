"""
[ ]
[ ]
[ ]
[ ]	PROGRAM_NAME:	PEBBLESUITE SOLO
[ ]	CREATED_BY:	DISTRIBUTED FINANCIAL SYSTEMS, LLC
[ ]	VERSION:	00.00
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


#Python Standard Library modules.
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo

#PebbleSuite custom modules.
from MenuBar import *

#Accounts Payable modules:
from AP_new_vendor import *
from AP_edit_vendor import *
from AP_delete_vendor import *
from AP_new_invoice import *
from AP_edit_invoice import *
from AP_delete_invoice import *
from AP_new_credit_memo import *

#Accounts Receivable modules:
from AR_new_client import *
from AR_edit_client import *
from AR_delete_client import *
from AR_new_invoice import *
from AR_edit_invoice import *
from AR_delete_invoice import *
from AR_new_credit_memo import *

#Company Menu modules:
from Company_commands import *
from Export_database import *

#General Ledger Menu modules:
from GL_new_GL import *
from GL_edit_GL import *
from GL_delete_GL import *

#Help Memu modules:
from Help_commands import *

#Journal Entries modules:
from JE_new_journal_entry import *

#Reports Menu modules:
from Reports_commands import *
from Reports_AP_aging_report import *
from Reports_AR_aging_report import *
from Reports_vendor_summary import *
from Reports_client_summary import *


"""
[ ]
[ ]
[ ]
[ ]	PEBBLESUITE MAIN WINDOW:
[ ]
[ ]
[ ]
"""


class APP(tk.Tk):

	retrieve_note_names = '''SELECT TASK_NAME FROM tasks;'''

	def __init__(self):

		#Initialize PebbleSuite parent class Tkinter widget.
		super().__init__()
		self.title("Distributed Financial Systems  -  PebbleSuite Solo")
		self.geometry("960x605")
		self.resizable(0,0)

		#Connect Menu Bar Tkinter widget to __main()__ PebbleSuite window.
		root_menu = MENU_BAR(self)
		self.config(menu=root_menu)


		"""
		[ ]
		[ ]
		[ ]
		[ ]	NOTES MENU TKINTER WIDGETS:
		[ ]
		[ ]
		[ ]
		"""


		self.scrollbar = ttk.Scrollbar(self)
		self.scrollbar.place(x=290,y=150,width=20,height=440)
		self.listbox = tk.Listbox(self, yscrollcommand=self.scrollbar.set)
		self.listbox.place(x=20,y=150,width=270,height=440)
		self.scrollbar.config(command=self.listbox.yview)

		#Initialize SQL.db connection
		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()
			cursor.execute(self.retrieve_note_names)
			connection.commit()

			for item in cursor:

				self.listbox.insert(0," ".join(item))

			cursor.close()


		"""
		[ ]
		[ ]
		[ ]
		[ ]	TEXTBOX TKINTER WIDGETS:
		[ ]
		[ ]
		[ ]
		"""


		self.text_scrollbar = ttk.Scrollbar(self)
		self.text_scrollbar.place(x=920,y=150,width=20,height=400)
		self.textbox = tk.Text(self,yscrollcommand=self.text_scrollbar)
		self.textbox.place(x=330,y=150,width=590,height=400)


		"""
		[ ]
		[ ]
		[ ]
		[ ]	"NEW NOTE" SECTION TKINTER WIDGETS:
		[ ]
		[ ]
		[ ]
		"""


		self.new_task_button = ttk.Button(self,text="New Note",command=self.new_task)
		self.new_task_button.place(x=20,y=40)

		self.clear_note_data_button = ttk.Button(self,text="Clear Note Entries",command=self.clear_note_entries)
		self.clear_note_data_button.place(x=110,y=40)

		self.new_task_name_label = ttk.Label(self,text="New Note Name:")
		self.new_task_name_label.place(x=330,y=15)
		self.new_task_name_entry = ttk.Entry(self)
		self.new_task_name_entry.place(x=330,y=40,width=300)

		self.new_note_date_label = ttk.Label(self,text="New Note Date:")
		self.new_note_date_label.place(x=650,y=15)
		self.new_task_date_entry_text = tk.StringVar()
		self.new_task_date_entry_text.set("MM/DD/YYYY")
		self.new_task_date_entry = ttk.Entry(self,textvariable=self.new_task_date_entry_text)
		self.new_task_date_entry.place(x=650,y=40,width=100)

		self.new_note_due_date_label = ttk.Label(self,text="Note Due Date:")
		self.new_note_due_date_label.place(x=775,y=15)
		self.new_note_due_date_entry = ttk.Entry(self)
		self.new_note_due_date_entry.place(x=775,y=40,width=100)


		"""
		[ ]
		[ ]
		[ ]
		[ ]	BOTTOM ROW BUTTONS:
		[ ]
		[ ]
		[ ]
		"""


		self.open_task_note_button = ttk.Button(self,text="Open Note",command=self.display_note)
		self.open_task_note_button.place(x=20,y=105)

		self.update_task_note_button = ttk.Button(self,text="Save Changes",command=self.save_note_changes)
		self.update_task_note_button.place(x=330,y=560)

		self.clear_task_note_button = ttk.Button(self,text="Close Note",command=self.close_note)
		self.clear_task_note_button.place(x=435,y=560)

		self.delete_task_note_button = ttk.Button(self,text="Delete Note",command=self.delete_task_note)
		self.delete_task_note_button.place(x=110,y=105)


		"""
		[ ]
		[ ]
		[ ]
		[ ]	NOTE EDITING ENTRY WIDGETS:
		[ ]
		[ ]
		[ ]
		"""


		self.editing_task_name_label = ttk.Label(self,text="Current Task:")
		self.editing_task_name_label.place(x=330,y=85)
		self.editing_task_name_entry_text = tk.StringVar()
		self.editing_task_name_entry = ttk.Entry(self,textvariable=self.editing_task_name_entry_text,state=tk.DISABLED)
		self.editing_task_name_entry.place(x=330,y=105,width=300)

		self.editing_task_date_label = ttk.Label(self,text="Date Created:")
		self.editing_task_date_label.place(x=650,y=85)
		self.editing_task_date_entry_text = tk.StringVar()
		self.editing_task_date_entry = ttk.Entry(self,textvariable=self.editing_task_date_entry_text,state=tk.DISABLED)
		self.editing_task_date_entry.place(x=650,y=105,width=100)

		self.editing_note_due_date_label = ttk.Label(self,text="Due Date:")
		self.editing_note_due_date_label.place(x=775,y=85)
		self.editing_note_due_date_entry_text = tk.StringVar()
		self.editing_note_due_date_entry = ttk.Entry(self,textvariable=self.editing_note_due_date_entry_text,state=tk.DISABLED)
		self.editing_note_due_date_entry.place(x=775,y=105,width=100)


	"""
	[ ]
	[ ]
	[ ]
	[ ]	"NEW NOTE" BUTTON FUNCTION:
	[ ]
	[ ]
	[ ]
	"""


	def new_task(self):

		#Define SQL.db scripts:
		new_task_sql_script = '''INSERT INTO tasks(
					TASK_NAME,
					TASK_DATE,
					TASK_NOTE)
					VALUES(?,?,0);'''

		retrieve_note_names = '''SELECT TASK_NAME FROM tasks;'''

		#Define function variables:
		new_task_data = []
		new_task_name = self.new_task_name_entry.get()
		new_task_data.append(new_task_name)
		new_task_date = self.new_task_date_entry.get()
		new_task_data.append(new_task_date)

		if new_task_name == "":

			task_name_error_message_1 = tk.messagebox.showinfo(title="Error",message="Enter name for new note.")

		elif new_task_date.count(" ") > 0:

			task_date_error_message_1 = tk.messagebox.showinfo(title="Error",message="Enter date for new note.")

		elif new_task_date.count("/") != 2:

			task_date_error_message_2 = tk.messagebox.showinfo(title="Error",message="Enter date for new note.")

		elif new_task_date == "MM/DD/YYYY":

			task_date_error_message_3 = tk.messagebox.showinfo(title="Error",message="Enter date for new note.")

		else:

			#Initialize SQL.db connection:
			with sqlite3.connect("SQL.db") as connection:

				try:

					cursor = connection.cursor()
					cursor.execute(new_task_sql_script,new_task_data)
					connection.commit()
					cursor.close()
					new_task_confirmation_message = tk.messagebox.showinfo(title="New Task",message="New task entered into database.")

				except sqlite3.Error as error:

					new_task_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")

			#Delete data in tkinter widgets:
			self.listbox.delete(0,tk.END)
			self.new_task_name_entry.delete(0,tk.END)
			self.new_task_date_entry.delete(0,tk.END)
			self.new_note_due_date_entry.delete(0,tk.END)

			#Initialize SQL.db connection:
			with sqlite3.connect("SQL.db") as connection:

				try:

					cursor = connection.cursor()
					cursor.execute(retrieve_note_names)
					connection.commit()

					for item in cursor:

						self.listbox.insert(0," ".join(item))

					cursor.close()

				except sqlite3.Error as error:

					new_task_error_message2 = tk.messagebox.showinfo(title="Error",message=f"{error}")


	"""
	[ ]
	[ ]
	[ ]
	[ ]	"CLEAR NOTE ENTRIES" BUTTON FUNCTION:
	[ ]
	[ ]
	[ ]
	"""


	def clear_note_entries(self):

		self.new_task_name_entry.delete(0,tk.END)
		self.new_task_date_entry.delete(0,tk.END)


	"""
	[ ]
	[ ]
	[ ]
	[ ]	"OPEN NOTE" BUTTON FUNCTION:
	[ ]
	[ ]
	[ ]
	"""


	def display_note(self):

		display_date_sql_script = '''SELECT TASK_DATE FROM tasks WHERE TASK_NAME=?;'''
		display_note_sql_script = '''SELECT TASK_NOTE FROM tasks WHERE TASK_NAME=?;'''

		for item in self.listbox.curselection():

			select_task = self.listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				#Select task note from SQL.db:
				note_cursor = connection.cursor()
				note_cursor.execute(display_note_sql_script,[select_task])

				for item in note_cursor:
					self.textbox.insert(tk.END," ".join(item))

				connection.commit()
				note_cursor.close()

				#Select task date from SQL.db:
				date_cursor = connection.cursor()
				date_cursor.execute(display_date_sql_script,[select_task])
				connection.commit()

				for item in date_cursor:
					self.editing_task_date_entry_text.set(item)

				date_cursor.close()

		self.editing_task_name_entry_text.set(select_task)


	"""
	[ ]
	[ ]
	[ ]
	[ ]	"SAVE NOTE CHANGES" BUTTON FUNCTION:
	[ ]
	[ ]
	[ ]
	"""


	def save_note_changes(self):

		#Define SQL.db scripts:
		update_note_sql_script = '''UPDATE tasks SET TASK_NOTE=? WHERE TASK_NAME=?;'''

		#Define function variables:
		update_data_list = []
		set_task_name = self.editing_task_name_entry.get()
		set_task_note = self.textbox.get(1.0,"end-1c")

		#Define data formatting functions:
		update_data_list.append(set_task_name)
		update_data_list.append(set_task_note)
		update_data_list.reverse()

		#SQL.db functionality:
		with sqlite3.connect("SQL.db") as connection:
			cursor = connection.cursor()
			cursor.execute(update_note_sql_script,update_data_list)
			connection.commit()
			cursor.close()

		save_note_changes_confirmation_message = tk.messagebox.showinfo(title="Save Changes",message="Note updates saved successfully.")


	"""
	[ ]
	[ ]
	[ ]
	[ ]	"CLOSE NOTE" BUTTON FUNCTION:
	[ ]
	[ ]
	[ ]
	"""


	def close_note(self):

		self.editing_task_name_entry_text.set("")
		self.editing_task_date_entry_text.set("")
		self.textbox.delete(1.0,tk.END)


	"""
	[ ]
	[ ]
	[ ]
	[ ]	"DELETE NOTE BUTTON FUNCTION:
	[ ]
	[ ]
	[ ]
	"""


	def delete_task_note(self):

		#Define SQL database scripts:
		query_note_sql_script = '''SELECT * FROM tasks WHERE TASK_NAME=?;'''
		delete_note_sql_script = '''DELETE FROM tasks WHERE TASK_NAME=?;'''
		query_all_notes_sql_script = '''SELECT TASK_NAME FROM tasks;'''

		#Select item from listbox tkinter widget:
		for item in self.listbox.curselection():

			select_task = self.listbox.get(item)

			#Initialize SQL.db connection:
			with sqlite3.connect("SQL.db") as connection:

				try:

					cursor = connection.cursor()
					cursor.execute(query_note_sql_script,[select_task])
					cursor.execute(delete_note_sql_script,[select_task])
					connection.commit()
					cursor.close()
					delete_note_confirmation_message = tk.messagebox.showinfo(title="Delete Note",message="Note deleted")

				except sqlite3.Error as error:

					delete_note_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")

			#Clear note entry tkinter widgets:
			self.listbox.delete(0,tk.END)
			self.editing_task_name_entry.delete(0,tk.END)
			self.editing_task_date_entry.delete(0,tk.END)
			self.editing_note_due_date_entry.delete(0,tk.END)
			self.textbox.delete(1.0,tk.END)

			#Initialize SQL.db connection:
			with sqlite3.connect("SQL.db") as connection:

				try:

					cursor = connection.cursor()
					cursor.execute(query_all_notes_sql_script)

					for item in cursor:

						self.listbox.insert(0," ".join(item))

					connection.commit()

					cursor.close()

				except sqlite3.Error as error:

					delete_note_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")


"""
[ ]
[ ]
[ ]
[ ]	__main__ PROGRAM ENTRY POINT
[ ]
[ ]
[ ]
"""


if __name__ == "__main__":

	try:
		app = APP()
		app.mainloop()

	except sqlite3.Error as error:
		print(error)


"""
[ ]
[ ]
[ ]
[ ]	END OF FILE
[ ]
[ ]
[ ]
"""
