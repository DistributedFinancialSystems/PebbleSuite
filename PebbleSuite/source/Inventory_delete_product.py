#Python Standard Library dependencies

import datetime
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class DELETE_PRODUCT_WINDOW(tk.Toplevel):

	#Define class variables
	alive = False

	delete_selection_temporary_memory = []

	product_sql_script = '''SELECT PRODUCT_NAME FROM products;'''

	#Define class functions
	def __init__(self,*args,**kwargs):

		options = ["Select Product"]

		#Initialize SQL.db connection:
		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.product_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()

		#Define class tkinter widgets:
		super().__init__(*args,**kwargs)
		self.config(width=600,height=340)
		self.title("Delete Product")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.product_name_label = ttk.Label(self,text="Product Name:")
		self.product_name_label.place(x=20,y=15)

		#Search for Product names in SQL.db.
		#Insert Product names into Product search listbox widget.
		self.select_product_scrollbar = ttk.Scrollbar(self)
		self.select_product_scrollbar.place(x=353,y=45,width=20,height=240)
		self.select_product_listbox = tk.Listbox(self,yscrollcommand=self.select_product_scrollbar.set)
		self.select_product_listbox.place(x=20,y=45,width=333,height=240)
		self.select_product_scrollbar.config(command=self.select_product_listbox.yview)

		search_product_name_sql_script = '''SELECT PRODUCT_NAME FROM products;'''

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(search_product_name_sql_script)

				connection.commit()

				for item in cursor:

					self.select_product_listbox.insert(0," ".join(item))

				cursor.close()

		except sqlite3.Error as error:

			select_products_error_message = tk.messagebox.showinfo(title="Delete Product",message="Unable to retrieve product data.")

		self.delete_product_button = ttk.Button(self,text="Select Product",command=self.delete_product)
		self.delete_product_button.place(x=20,y=300)

		self.product_name_label = ttk.Label(self,text="Product Name:")
		self.product_name_label.place(x=400,y=15)
		self.product_name_entry_text = tk.StringVar()
		self.product_name_entry = ttk.Entry(self,textvariable=self.product_name_entry_text,state=tk.DISABLED,width=21)
		self.product_name_entry.place(x=400,y=45)

		self.product_number_label = ttk.Label(self,text="Product Number:")
		self.product_number_label.place(x=400,y=85)
		self.product_number_entry_text = tk.StringVar()
		self.product_number_entry = ttk.Entry(self,textvariable=self.product_number_entry_text,width=21)
		self.product_number_entry.place(x=400,y=115)

		self.product_vendor_name_label = ttk.Label(self,text="Product Vendor:")
		self.product_vendor_name_label.place(x=400,y=155)
		self.product_vendor_name_entry_text = tk.StringVar()
		self.product_vendor_name_entry = ttk.Entry(self,textvariable=self.product_vendor_name_entry_text,state=tk.DISABLED,width=21)
		self.product_vendor_name_entry.place(x=400,y=185)

		self.product_sales_price_label = ttk.Label(self,text="Sales Price:")
		self.product_sales_price_label.place(x=400,y=225)
		self.product_sales_price_entry_text = tk.StringVar()
		self.product_sales_price_entry = ttk.Entry(self,textvariable=self.product_sales_price_entry_text,width=21)
		self.product_sales_price_entry.place(x=400,y=255)

		self.cancel_product_changes_button = ttk.Button(self,text="Cancel",command=self.cancel_changes)
		self.cancel_product_changes_button.place(x=490,y=300)

		self.submit_product_changes_button = ttk.Button(self,text="Delete",command=self.submit_changes)
		self.submit_product_changes_button.place(x=400,y=300)


	def delete_product(self):

		#Define SQL.db scripts:
		query_product_sql_script = '''SELECT * FROM products WHERE PRODUCT_NAME=?'''


		for item in self.select_product_listbox.curselection():

			select_product = self.select_product_listbox.get(item)

		try:

			with sqlite3.connect("SQL.db") as connection:

				collect = []

				cursor = connection.cursor()

				cursor.execute(query_product_sql_script,[select_product])

				for item in cursor:

					collect.append(item)

					self.delete_selection_temporary_memory.append(item)

				self.product_name_entry_text.set(f"{collect[0][0]}")
				self.product_number_entry_text.set(f"{collect[0][1]}")
				self.product_vendor_name_entry_text.set(f"{collect[0][2]}")
				self.product_sales_price_entry_text.set(f"{collect[0][3]}")

				connection.commit()

				cursor.close()

		except sqlite3.Error as error:

			delete_product_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")


	def submit_changes(self):

		#Define SQL.db scripts:
		retrieve_product_sql_script = '''SELECT * FROM products WHERE PRODUCT_NAME=?;'''
		delete_product_sql_script = '''DELETE FROM products WHERE PRODUCT_NAME=?;'''


		#Define function variables:
		product_name = self.delete_selection_temporary_memory[0][0]

		#Delete Product name:
		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(retrieve_product_sql_script,[product_name])
				cursor.execute(delete_product_sql_script,[product_name])

				connection.commit()

				cursor.close()

				delete_product_names_confirmation_message = tk.messagebox.showinfo("Delete Product",message="Product successfully deleted.")

		except sqlite3.Error as error:

			delete_product_names_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")

		#Clear temporary memory variable:
		self.delete_selection_temporary_memory.clear()

		self.product_name_entry_text.set("")
		self.product_number_entry_text.set("")
		self.product_vendor_name_entry_text.set("")
		self.product_sales_price_entry_text.set("")


	def cancel_changes(self):

		try:

			self.delete_selection_temporary_memory.clear()

			self.product_name_entry_text.set("")
			self.product_number_entry_text.set("")
			self.product_vendor_name_entry_text.set("")
			self.product_sales_price_entry_text.set("")

		except:

			cancel_changes_error_message = tk.messagebox.showinfo(title="Error",message="Unable to clear data entries.")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
