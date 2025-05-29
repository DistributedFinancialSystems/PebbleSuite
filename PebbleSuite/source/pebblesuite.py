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
from GL_reconcile_GL import *

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




class APP(tk.Tk):

	def __init__(self):

		super().__init__()
		self.title("Distributed Financial Systems  -  PebbleSuite Solo")
		self.geometry("960x540")
		self.resizable(0,0)

		root_menu = MENU_BAR(self)
		self.config(menu=root_menu)

		self.container = tk.Frame(self,width=960,height=50,bg="lightgray")
		self.container.place(x=0,y=0)
		self.container.grid(row=0,column=0,sticky="nsew")
		self.container.grid_rowconfigure(0,weight=1)
		self.container.grid_columnconfigure(0,weight=1)

		self.container2 = tk.Frame(self,width=960,height=490,bg="lightgray")
		self.container2.place(x=0,y=50)
		self.container2.grid(row=1,column=0,sticky="nsew")
		self.container2.grid_rowconfigure(1,weight=1)
		self.container2.grid_columnconfigure(0,weight=1)

		b1 = ttk.Button(self,text="Sales",command=self.sales_menu)
		b1.place(x=20,y=12)

		b2 = ttk.Button(self,text="Tasks",command=self.tasks_menu)
		b2.place(x=120,y=12)

		b3 = ttk.Button(self,text="Files",command=self.files_menu)
		b3.place(x=220,y=12)

		b4 = ttk.Button(self,text="Database",command=self.database_menu)
		b4.place(x=320,y=12)

		"""
		____________________________________
		Functionality for directory widgets:
		____________________________________
		"""

		self.directory_label = tk.Label(self,text="Directory:",bg="lightgray")
		self.directory_label.place(x=430,y=12)
		self.directory_text = tk.StringVar()

		self.current_directory = []

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute('''SELECT * FROM permanent_directory;''')

			for item in cursor:

				self.current_directory.append(*item)

			connection.commit()

			cursor.close()

		self.check_directory = os.path.dirname(self.current_directory[0])
		self.directory_text.set(f"{self.check_directory}")

		self.directory_entry = ttk.Entry(self,textvariable=self.directory_text)
		self.directory_entry.place(x=500,y=12,width=300)

		self.set_directory_button = ttk.Button(self,text="Set Directory",command=self.change_directory)
		self.set_directory_button.place(x=825,y=12)


	def change_directory(self):

		try:

			update_working_directory_sql_script = '''UPDATE working_directory SET WORKING_DIRECTORY=?;'''

			new_dir = self.directory_text.get()

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(update_working_directory_sql_script,[new_dir])

				connection.commit()

				cursor.close()

			change_directory_confirmation_message = tk.messagebox.showinfo(title="PebbleSuite",message=f"New working directory:  {new_dir}")

		except Exception as error:

			tk.change_directory_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")

	"""
	_________________________
	SALES MENU FUNCTIONS:
	_________________________
	"""

	def sales_menu(self):

		try:

			for widget in self.container2.winfo_children():

				widget.destroy()

			self.sale_date_label = ttk.Label(self.container2,text="Sale Date:")
			self.sale_date_label.place(x=20,y=15)
			self.sale_date_entry_text = tk.StringVar()
			self.sale_date_entry = ttk.Entry(self.container2,textvariable=self.sale_date_entry_text)
			self.sale_date_entry.place(x=90,y=15,width=92)
			self.sale_date_entry_text.set("MM/DD/YYYY")

			self.sale_customer_label = ttk.Label(self.container2,text="Customers:")
			self.sale_customer_label.place(x=20,y=80)

			self.sale_customer_menu = tk.Listbox(self.container2)
			self.sale_customer_menu.place(x=20,y=105)

			self.select_customer_button = ttk.Button(self.container2,text="Select Customer",command=self.select_customer)
			self.select_customer_button.place(x=20,y=315)

			self.sale_products_label = ttk.Label(self.container2,text="Products:")
			self.sale_products_label.place(x=205,y=80)

			self.sale_products_menu = tk.Listbox(self.container2)
			self.sale_products_menu.place(x=205,y=105)

			self.select_product_button = ttk.Button(self.container2,text="Select Product",command=self.select_product)
			self.select_product_button.place(x=205,y=315)

		except Exception as error:

			sales_menu_error_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")


	def select_customer(self):

		try:

			select_customer_confirmation_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message="Customer selected!")

		except Exception as error:

			select_customer_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")


	def select_product(self):

		try:

			select_product_confirmation_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message="Product selected!")

		except Exception as error:

			select_product_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")

	"""
	_____________________
	TASKS MENU FUNCTIONS:
	_____________________
	"""

	def tasks_menu(self):

		try:


			for widget in self.container2.winfo_children():

				widget.destroy()


			self.retrieve_note_names = '''SELECT TASK_NAME FROM tasks;'''

			self.scrollbar = ttk.Scrollbar(self.container2)
			self.scrollbar.place(x=377,y=115,width=20,height=315)
			self.listbox = tk.Listbox(self.container2)
			self.listbox = tk.Listbox(self.container2, yscrollcommand=self.scrollbar.set)
			self.listbox.grid(row=1,column=0,padx=10,pady=10)
			self.listbox.place(x=20,y=115,width=357,height=315)
			self.scrollbar.config(command=self.listbox.yview)


			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(self.retrieve_note_names)

				connection.commit()

				for item in cursor:

					self.listbox.insert(0," ".join(item))

				cursor.close()


			self.text_scrollbar = ttk.Scrollbar(self.container2)
			self.text_scrollbar.grid(row=2,column=1,padx=10,pady=10)
			self.text_scrollbar.place(x=920,y=115,width=20,height=315)
			self.textbox = tk.Text(self.container2,yscrollcommand=self.text_scrollbar,wrap=tk.WORD)
			self.textbox.grid(row=3,column=1,padx=10,pady=10)
			self.textbox.place(x=430,y=115,width=490,height=315)

			self.new_task_button = ttk.Button(self.container2,text="Create New Task",command=self.new_task)
			self.new_task_button.place(x=275,y=75)

			self.clear_note_data_button = ttk.Button(self.container2,text="Clear Task Entries",command=self.clear_note_entries)
			self.clear_note_data_button.place(x=110,y=450)

			self.new_task_name_label = tk.Label(self.container2,text="New Task Name:",bg="lightgray")
			self.new_task_name_label.place(x=20,y=15)
			self.new_task_name_entry = ttk.Entry(self.container2)
			self.new_task_name_entry.place(x=20,y=45,width=375)

			self.new_note_date_label = tk.Label(self.container2,text="New Task Date:",bg="lightgray")
			self.new_note_date_label.place(x=20,y=80)
			self.new_task_date_entry_text = tk.StringVar()
			self.new_task_date_entry_text.set("MM/DD/YYYY")
			self.new_task_date_entry = ttk.Entry(self.container2,textvariable=self.new_task_date_entry_text)
			self.new_task_date_entry.place(x=130,y=80,width=100)

			self.open_task_note_button = ttk.Button(self.container2,text="Open Task",command=self.display_note)
			self.open_task_note_button.place(x=20,y=450)

			self.update_task_note_button = ttk.Button(self.container2,text="Save Changes",command=self.save_note_changes)
			self.update_task_note_button.place(x=430,y=450)

			self.clear_task_note_button = ttk.Button(self.container2,text="Close Task",command=self.close_note)
			self.clear_task_note_button.place(x=545,y=450)

			self.delete_task_note_button = ttk.Button(self.container2,text="Delete Task",command=self.delete_task_note)
			self.delete_task_note_button.place(x=240,y=450)

			self.editing_task_name_label = tk.Label(self.container2,text="Current Task:",bg="lightgray")
			self.editing_task_name_label.place(x=430,y=15)
			self.editing_task_name_entry_text = tk.StringVar()
			self.editing_task_name_entry = ttk.Entry(self.container2,textvariable=self.editing_task_name_entry_text,state=tk.DISABLED)
			self.editing_task_name_entry.place(x=430,y=45,width=375)

			self.editing_task_date_label = tk.Label(self.container2,text="Date Created:",bg="lightgray")
			self.editing_task_date_label.place(x=825,y=15)
			self.editing_task_date_entry_text = tk.StringVar()
			self.editing_task_date_entry = ttk.Entry(self.container2,textvariable=self.editing_task_date_entry_text,state=tk.DISABLED)
			self.editing_task_date_entry.place(x=825,y=45,width=100)

			self.editing_task_notes_label = tk.Label(self.container2,text="Current Task Notes:",bg="lightgray")
			self.editing_task_notes_label.place(x=430,y=80)

		except Exception as error:

			tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")


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
	_____________________
	FILES MENU FUNCTIONS:
	_____________________
	"""

	def files_menu(self):

		try:


			for widget in self.container2.winfo_children():

				widget.destroy()


			files_menu_label_1 = tk.Label(self.container2,text="Files Menu",bg="lightgray")
			files_menu_label_1.place(x=20,y=15)


		except Exception as error:

			files_menu_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")

	"""
	________________________
	DATABASE MENU FUNCTIONS:
	________________________
	"""

	def database_menu(self):

		try:

			for widget in self.container2.winfo_children():

				widget.destroy()

			self.database_menu_label_1 = tk.Label(self.container2,text="Database Menu",bg="lightgray")
			self.database_menu_label_1.place(x=20,y=15)

			self.querybox = tk.Text(self.container2,wrap=tk.WORD)
			self.querybox.place(x=20,y=35,height=100,width=740)

			self.querybox_submit_query_button = ttk.Button(self.container2,text="Submit Query",command=self.submit_query)
			self.querybox_submit_query_button.place(x=770,y=35)

			self.querybox_clear_query_button = ttk.Button(self.container2,text="Clear Query",command=self.clear_query)
			self.querybox_clear_query_button.place(x=770,y=75)

			self.databox = tk.Text(self.container2,wrap=tk.WORD)
			self.databox.place(x=20,y=155,height=315,width=740)

			self.databox_clear_query_data_button = ttk.Button(self.container2,text="Clear Data",command=self.clear_query_data)
			self.databox_clear_query_data_button.place(x=770,y=155)

			self.databox_print_query_data_button = ttk.Button(self.container2,text="Print Data",command=self.print_query_data)
			self.databox_print_query_data_button.place(x=770,y=195)

		except Exception as error:

			database_menu_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")


	def submit_query(self):

		try:

			query = self.querybox.get(1.0,"end-1c")

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(query)

				for item in cursor:

					self.databox.insert(1.0," ".join(item))

					print(item)

				connection.commit()

				cursor.close()

		except Exception as error:

			submit_query_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")


	def clear_query(self):

		try:

			self.querybox.delete(1.0,tk.END)

		except Exception as error:

			clear_query_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")


	def clear_query_data(self):

		try:

			self.databox.delete(1.0,tk.END)

		except Exception as error:

			clear_query_data_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")


	def print_query_data(self):

		try:

			print_query_data_confirmation_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message="Data printed!")

		except Exception as error:

			print_query_data_error_message_1 = tk.messagebox.showinfo(title="PebbleSuite",message=f"{error}")



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
