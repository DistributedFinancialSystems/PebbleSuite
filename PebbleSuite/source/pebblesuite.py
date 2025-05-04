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

#Python Standard Library modules.
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import stripe
import os

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

#Customers Menu modules:
from Customers_new_customer import *
from Customers_edit_customer import *
from Customers_delete_customer import *
from Customers_customer_summary import *

#Company Menu modules:
from Company_commands import *
from Export_database import *

#General Ledger Menu modules:
from GL_new_GL import *
from GL_edit_GL import *
from GL_delete_GL import *
from GL_GL_summary import *

#Help Memu modules:
from Help_commands import *

#Inventory Menu modeules:
from Inventory_new_product import *
from Inventory_edit_product import *
from Inventory_delete_product import *
from Inventory_new_inventory import *

#Journal Entries modules:
from JE_new_journal_entry import *
from JE_JE_summary import *

#Reports Menu modules:
from Reports_commands import *
from Reports_AP_aging_report import *
from Reports_AR_aging_report import *
from Reports_vendor_summary import *
from Reports_client_summary import *

#Settings Menu modules:
from Settings_stripe_account import *


"""
class TestFrame(tk.Frame):

	def __init__(self):

		super().__init__()

		tk.Label(self,text="Test Label")
"""




class APP(tk.Tk):

	retrieve_note_names = '''SELECT TASK_NAME FROM tasks;'''

	def __init__(self):

		super().__init__()
		self.title("Distributed Financial Systems  -  PebbleSuite Solo")
		self.geometry("960x540")
		self.resizable(0,0)

		root_menu = MENU_BAR(self)
		self.config(menu=root_menu)

		self.files_frame = tk.Frame(self,height=540,width=960)
		self.files_frame.pack()

		"""
		self.tasks_frame = tk.Frame(self,height=540,width=960)
		self.tasks_frame.pack()
		"""

		self.tasks_button = ttk.Button(self,text="Tasks",command=self.tasks_window)
		self.tasks_button.place(x=20,y=12)

		self.files_button = ttk.Button(self,text="Files",command=self.na)
		self.files_button.place(x=130,y=12)

		self.database_button = ttk.Button(self,text="Database",command=self.na)
		self.database_button.place(x=275,y=12)

		self.directory_label = ttk.Label(self,text="Directory:")
		self.directory_label.place(x=430,y=12)
		self.directory_text = tk.StringVar()
		self.current_directory = os.getcwd()
		self.check_directory = os.path.dirname(self.current_directory)
		self.directory_text.set(f"{self.check_directory}")

		self.directory_entry = ttk.Entry(self,textvariable=self.directory_text)
		self.directory_entry.place(x=500,y=12,width=300)

		self.set_directory_button = ttk.Button(self,text="Set Directory",command=self.change_directory)
		self.set_directory_button.place(x=825,y=12)

		self.separator = ttk.Separator(self,orient='horizontal')
		self.separator.place(relx=0,rely=0.10,relwidth=1,relheight=1)

		"""

		self.files_button = ttk.Button(self,text="Files",command=self.files_window)
		self.files_button.place(x=120,y=20)
		"""

		"""
		self.testframe1 = TestFrame()
		self.testframe1.grid(row=2,column=3)
		"""

		"""
	def files_window(self):

		for widget in self.winfo_children():

			widget.destroy()

		self.files_label = ttk.Label(self.files_frame,text="Files Frame")
		self.files_label.place(x=100,y=100)

		self.files_button = ttk.Button(self.files_frame,text="Button",command=self.na)
		self.files_button.place(x=200,y=100)

		self.scrollbar = ttk.Scrollbar(self.files_frame)
		self.scrollbar.place(x=120,y=100,width=20,height=100)
		self.listbox = tk.Listbox(self.files_frame,yscrollcommand=self.scrollbar.set)
		self.listbox.place(x=20,y=100,width=100,height=100)
		self.scrollbar.config(command=self.listbox.yview)
		"""


		"""
		______________________
		TASKS TKINTER WIDGETS:
		______________________
		"""

	def na(self):

		pass

	def change_directory(self):

		try:

			new_dir = self.directory_text.get()
			os.chdir(new_dir)

			change_directory_confirmation_message = tk.messagebox.showinfo(title="PebbleSuite",message=f"New working directory:  {new_dir}")

		except Exception as error:

			tk.change_directory_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")

	def tasks_window(self):

		"""

		for widget in self.files_frame.winfo_children():

			widget.destroy()

		"""

		self.scrollbar = ttk.Scrollbar(self)
		self.scrollbar.place(x=377,y=175,width=20,height=315)
		self.listbox = tk.Listbox(self, yscrollcommand=self.scrollbar.set)
		self.listbox.place(x=20,y=175,width=357,height=315)
		self.scrollbar.config(command=self.listbox.yview)

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.retrieve_note_names)

			connection.commit()

			for item in cursor:

				self.listbox.insert(0," ".join(item))

			cursor.close()

		self.text_scrollbar = ttk.Scrollbar(self)
		self.text_scrollbar.place(x=920,y=175,width=20,height=315)
		self.textbox = tk.Text(self,yscrollcommand=self.text_scrollbar,wrap=tk.WORD)
		self.textbox.place(x=430,y=175,width=490,height=315)

		self.new_task_button = ttk.Button(self,text="Create New Task",command=self.new_task)
		self.new_task_button.place(x=275,y=140)

		self.clear_note_data_button = ttk.Button(self,text="Clear Task Entries",command=self.clear_note_entries)
		self.clear_note_data_button.place(x=110,y=500)

		self.new_task_name_label = ttk.Label(self,text="New Task Name:")
		self.new_task_name_label.place(x=20,y=80)
		self.new_task_name_entry = ttk.Entry(self)
		self.new_task_name_entry.place(x=20,y=100,width=375)

		self.new_note_date_label = ttk.Label(self,text="New Task Date:")
		self.new_note_date_label.place(x=20,y=140)
		self.new_task_date_entry_text = tk.StringVar()
		self.new_task_date_entry_text.set("MM/DD/YYYY")
		self.new_task_date_entry = ttk.Entry(self,textvariable=self.new_task_date_entry_text)
		self.new_task_date_entry.place(x=130,y=140,width=100)

		self.open_task_note_button = ttk.Button(self,text="Open Task",command=self.display_note)
		self.open_task_note_button.place(x=20,y=500)

		self.update_task_note_button = ttk.Button(self,text="Save Changes",command=self.save_note_changes)
		self.update_task_note_button.place(x=430,y=500)

		self.clear_task_note_button = ttk.Button(self,text="Close Task",command=self.close_note)
		self.clear_task_note_button.place(x=535,y=500)

		self.delete_task_note_button = ttk.Button(self,text="Delete Task",command=self.delete_task_note)
		self.delete_task_note_button.place(x=240,y=500)

		self.editing_task_name_label = ttk.Label(self,text="Current Task:")
		self.editing_task_name_label.place(x=430,y=80)
		self.editing_task_name_entry_text = tk.StringVar()
		self.editing_task_name_entry = ttk.Entry(self,textvariable=self.editing_task_name_entry_text,state=tk.DISABLED)
		self.editing_task_name_entry.place(x=430,y=100,width=375)

		self.editing_task_date_label = ttk.Label(self,text="Date Created:")
		self.editing_task_date_label.place(x=825,y=80)
		self.editing_task_date_entry_text = tk.StringVar()
		self.editing_task_date_entry = ttk.Entry(self,textvariable=self.editing_task_date_entry_text,state=tk.DISABLED)
		self.editing_task_date_entry.place(x=825,y=100,width=100)

		self.editing_task_notes_label = ttk.Label(self,text="Current Task Notes:")
		self.editing_task_notes_label.place(x=430,y=140)


	def new_task(self):

		new_task_sql_script = '''INSERT INTO tasks(
					TASK_NAME,
					TASK_DATE,
					TASK_NOTE)
					VALUES(?,?,0);'''

		retrieve_note_names = '''SELECT TASK_NAME FROM tasks;'''

		new_task_data = []
		new_task_name = self.new_task_name_entry.get()
		new_task_data.append(new_task_name)
		new_task_date = self.new_task_date_entry.get()
		new_task_data.append(new_task_date)

		if new_task_name == "":

			task_name_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message="Enter name for new note.")

		elif new_task_date.count(" ") > 0:

			task_date_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message="Enter date for new note.")

		elif new_task_date.count("/") != 2:

			task_date_error_message_2 = tk.messagebox.showinfo(title="PebbleSuite",message="Enter date for new note.")

		elif new_task_date == "MM/DD/YYYY":

			task_date_error_message_3 = tk.messagebox.showinfo(title="PebbleSuite",message="Enter date for new note.")

		else:

			with sqlite3.connect("SQL.db") as connection:

				try:

					cursor = connection.cursor()

					cursor.execute(new_task_sql_script,new_task_data)

					connection.commit()

					cursor.close()

					new_task_confirmation_message = tk.messagebox.showinfo(title="PebbleSuite",message="New task successfully created.")

				except Exception as error:

					new_task_error_message = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")

			self.listbox.delete(0,tk.END)
			self.new_task_name_entry.delete(0,tk.END)
			self.new_task_date_entry.delete(0,tk.END)

			with sqlite3.connect("SQL.db") as connection:

				try:

					cursor = connection.cursor()

					cursor.execute(retrieve_note_names)

					connection.commit()

					for item in cursor:

						self.listbox.insert(0," ".join(item))

					cursor.close()

				except Exception as error:

					new_task_error_message2 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")


	def clear_note_entries(self):

		try:

			self.new_task_name_entry.delete(0,tk.END)
			self.new_task_date_entry.delete(0,tk.END)

		except Exception as error:

			clear_note_entries_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")


	def display_note(self):

		display_date_sql_script = '''SELECT TASK_DATE FROM tasks WHERE TASK_NAME=?;'''
		display_note_sql_script = '''SELECT TASK_NOTE FROM tasks WHERE TASK_NAME=?;'''

		try:

			for item in self.listbox.curselection():

				select_task = self.listbox.get(item)

				with sqlite3.connect("SQL.db") as connection:

					note_cursor = connection.cursor()

					note_cursor.execute(display_note_sql_script,[select_task])

					self.textbox.delete(1.0,tk.END)

					for item in note_cursor:

						self.textbox.insert(tk.END," ".join(item))

					connection.commit()

					note_cursor.close()

					date_cursor = connection.cursor()

					date_cursor.execute(display_date_sql_script,[select_task])

					connection.commit()

					for item in date_cursor:

						self.editing_task_date_entry_text.set(item)

					date_cursor.close()

				self.editing_task_name_entry_text.set(select_task)

		except Exception as error:

			display_note_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")


	def save_note_changes(self):

		update_note_sql_script = '''UPDATE tasks SET TASK_NOTE=? WHERE TASK_NAME=?;'''

		update_data_list = []

		set_task_name = self.editing_task_name_entry.get()

		set_task_note = self.textbox.get(1.0,"end-1c")

		try:

			update_data_list.append(set_task_name)
			update_data_list.append(set_task_note)
			update_data_list.reverse()

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(update_note_sql_script,update_data_list)

				connection.commit()

				cursor.close()

			save_note_changes_confirmation_message = tk.messagebox.showinfo(title="PebbleSuite",message="Task updates saved successfully.")

		except Exception as error:

			save_note_changes_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")


	def close_note(self):

		try:

			self.editing_task_name_entry_text.set("")
			self.editing_task_date_entry_text.set("")
			self.textbox.delete(1.0,tk.END)

		except Exception as error:

			close_note_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")


	def delete_task_note(self):

		query_note_sql_script = '''SELECT * FROM tasks WHERE TASK_NAME=?;'''
		delete_note_sql_script = '''DELETE FROM tasks WHERE TASK_NAME=?;'''
		query_all_notes_sql_script = '''SELECT TASK_NAME FROM tasks;'''


		for item in self.listbox.curselection():

			select_task = self.listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				try:

					cursor = connection.cursor()

					cursor.execute(query_note_sql_script,[select_task])

					cursor.execute(delete_note_sql_script,[select_task])

					connection.commit()

					cursor.close()

					delete_note_confirmation_message = tk.messagebox.showinfo(title="PebbleSuite",message="Task successfully deleted.")

				except Exception as error:

					delete_note_error_message = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")

			self.listbox.delete(0,tk.END)
			self.editing_task_name_entry_text.set("")
			self.editing_task_date_entry_text.set("")
			self.textbox.delete(1.0,tk.END)

			with sqlite3.connect("SQL.db") as connection:

				try:

					cursor = connection.cursor()

					cursor.execute(query_all_notes_sql_script)

					for item in cursor:

						self.listbox.insert(0," ".join(item))

					connection.commit()

					cursor.close()

				except Exception as error:

					delete_note_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")


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

	except Exception as error:

		print(error)
