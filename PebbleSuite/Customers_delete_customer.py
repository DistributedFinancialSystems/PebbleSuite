#Python Standard Library dependencies
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class DELETE_CUSTOMER_ENTRY:


	def __init__(self,delete_customer_entry):

		self.delete_customer_entry = delete_customer_entry


	def delete_data(self):

		query_customer_sql_script = '''SELECT * FROM customers WHERE CUSTOMER_NAME=?'''
		delete_customer_sql_script = '''DELETE FROM customers WHERE CUSTOMER_NAME=?'''

		"""

		04-12-2025:  Will likely bring back customer credit memos function, but not including it for now.


		query_customer_invoices_sql_script = '''SELECT * FROM customer_invoices WHERE INVOICE_NAME=?;'''
		delete_customer_invoices_sql_script = '''DELETE FROM customer_invoices WHERE INVOICE_NAME=?;'''
		query_customer_credit_memos_sql_script = '''SELECT * FROM customer_credit_memos WHERE CREDIT_MEMO_NAME=?;'''
		delete_customer_credit_memos_sql_script = '''DELETE FROM customer_credit_memos WHERE CREDIT_MEMO_NAME=?;'''

		"""

		with sqlite3.connect("SQL.db") as connection:

			try:

				cursor = connection.cursor()

				cursor.execute(query_customer_sql_script,[self.delete_customer_entry])
				cursor.execute(delete_customer_sql_script,[self.delete_customer_entry])

				"""

				cursor.execute(query_customer_invoices_sql_script,[self.delete_customer_entry])
				cursor.execute(delete_customer_invoices_sql_script,[self.delete_customer_entry])

				delete_customer_invoices_confirmation_message = tk.messagebox.showinfo(title="Delete Customer",message="Customer invoice data successfully deleted")

				cursor.execute(query_customer_credit_memos_sql_script,[self.delete_customer_entry])
				cursor.execute(delete_customer_credit_memos_sql_script,[self.delete_customer_entry])

				delete_customer_credit_memos_confirmation_messages = tk.messagebox.showinfo(title="Delete Customer",message="Customer credit memo data successfully deleted")

				"""

				connection.commit()

				cursor.close()

				delete_customer_confirmation_message_1 = tk.messagebox.showinfo(title="Delete Customer",message="Customer contact data successfully deleted.")

			except Exception as error:

				delete_customer_error_message_1 = tk.messagebox.showinfo(title="Delete Customer",message=f"{error}")



class DELETE_CUSTOMER_WINDOW(tk.Toplevel):

	customer_sql_script = '''SELECT CUSTOMER_NAME FROM customers;'''

	alive = False

	dummy_variable = "null"

	def __init__(self,*args,**kwargs):

		customer_data = []

		options = ["Select Customer"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.customer_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()

		super().__init__(*args,**kwargs)
		self.config(width=390,height=150)
		self.title("Delete Customer")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True
		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")
		self.customer_name_label = ttk.Label(self,text="Customer Name")
		self.customer_name_label.place(x=20,y=40)
		self.customer_option_menu = ttk.OptionMenu(self,self.clicked,options[0],*options)
		self.customer_option_menu.place(x=200,y=40)
		self.delete_customer_button = ttk.Button(self,text="Delete Customer",command=self.delete_customer)
		self.delete_customer_button.place(x=20,y=110)


	def delete_customer(self):

		customer_data = self.clicked.get()

		try:

			if customer_data == "Select Customer":

				delete_customer_error_message_1 = tk.messagebox.showinfo(title="Delete Customer",message="Select a customer to delete.")

			else:

				delete_object = DELETE_CUSTOMER_ENTRY(customer_data)
				delete_object.delete_data()

		except Exception as error:

			delete_customer_error_message_2 = tk.messagebox.showinfo(title="Delete Customer",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
