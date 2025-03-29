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
from AP_pay_invoice import *
from AP_print_invoice import *
from AP_new_credit_memo import *
from AP_edit_credit_memo import *
from AP_delete_credit_memo import *
from AP_apply_credit_memo import *
from AP_print_credit_memo import *

#Accounts Receivable modules:
from AR_new_client import *
from AR_edit_client import *
from AR_delete_client import *
from AR_new_invoice import *
from AR_edit_invoice import *
from AR_delete_invoice import *
from AR_pay_invoice import *
from AR_print_invoice import *
from AR_new_credit_memo import *
from AR_edit_credit_memo import *
from AR_delete_credit_memo import *
from AR_apply_credit_memo import *
from AR_print_credit_memo import *

#Company Menu modules:
from Company_commands import *
from Export_database import *

#General Ledger Menu modules:
from GL_new_GL import *
from GL_edit_GL import *
from GL_delete_GL import *

#Help Memu modules:
from Help_commands import *

#Inventory Menu modeules:
from Inventory_new_product import *
from Inventory_edit_product import *

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
		self.scrollbar.place(x=377,y=165,width=20,height=385)
		self.listbox = tk.Listbox(self, yscrollcommand=self.scrollbar.set)
		self.listbox.place(x=20,y=165,width=357,height=385)
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
		self.text_scrollbar.place(x=920,y=165,width=20,height=385)
		self.textbox = tk.Text(self,yscrollcommand=self.text_scrollbar)
		self.textbox.place(x=430,y=165,width=490,height=385)


		"""
		[ ]
		[ ]
		[ ]
		[ ]	"NEW NOTE" SECTION TKINTER WIDGETS:
		[ ]
		[ ]
		[ ]
		"""


		self.new_task_button = ttk.Button(self,text="Create New Task",command=self.new_task)
		self.new_task_button.place(x=280,y=80)

		self.clear_note_data_button = ttk.Button(self,text="Clear Task Entries",command=self.clear_note_entries)
		self.clear_note_data_button.place(x=110,y=560)

		self.new_task_name_label = ttk.Label(self,text="New Task Name:")
		self.new_task_name_label.place(x=20,y=15)
		self.new_task_name_entry = ttk.Entry(self)
		self.new_task_name_entry.place(x=20,y=40,width=375)

		self.new_note_date_label = ttk.Label(self,text="New Task Date:")
		self.new_note_date_label.place(x=20,y=80)
		self.new_task_date_entry_text = tk.StringVar()
		self.new_task_date_entry_text.set("MM/DD/YYYY")
		self.new_task_date_entry = ttk.Entry(self,textvariable=self.new_task_date_entry_text)
		self.new_task_date_entry.place(x=130,y=80,width=100)

		self.note_names_list_label = ttk.Label(self,text="Task List:")
		self.note_names_list_label.place(x=20,y=140)


		"""
		[ ]
		[ ]
		[ ]
		[ ]	BOTTOM ROW BUTTONS:
		[ ]
		[ ]
		[ ]
		"""


		self.open_task_note_button = ttk.Button(self,text="Open Task",command=self.display_note)
		self.open_task_note_button.place(x=20,y=560)

		self.update_task_note_button = ttk.Button(self,text="Save Changes",command=self.save_note_changes)
		self.update_task_note_button.place(x=430,y=560)

		self.clear_task_note_button = ttk.Button(self,text="Close Task",command=self.close_note)
		self.clear_task_note_button.place(x=535,y=560)

		self.delete_task_note_button = ttk.Button(self,text="Delete Task",command=self.delete_task_note)
		self.delete_task_note_button.place(x=240,y=560)


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
		self.editing_task_name_label.place(x=430,y=15)
		self.editing_task_name_entry_text = tk.StringVar()
		self.editing_task_name_entry = ttk.Entry(self,textvariable=self.editing_task_name_entry_text,state=tk.DISABLED)
		self.editing_task_name_entry.place(x=430,y=40,width=375)

		self.editing_task_date_label = ttk.Label(self,text="Date Created:")
		self.editing_task_date_label.place(x=825,y=15)
		self.editing_task_date_entry_text = tk.StringVar()
		self.editing_task_date_entry = ttk.Entry(self,textvariable=self.editing_task_date_entry_text,state=tk.DISABLED)
		self.editing_task_date_entry.place(x=825,y=40,width=100)

		self.editing_task_notes_label = ttk.Label(self,text="Current Task Notes:")
		self.editing_task_notes_label.place(x=430,y=140)


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
