"""
[ ]
[ ]
[ ]
[ ]	Inventory_new_product.py
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




class NEW_PRODUCT_ENTRY:

	def __init__(self,new_product_entry):

		self.new_product_entry = new_product_entry

	def enter_data(self):

		new_product_sql_script = '''INSERT INTO products(
					PRODUCT_NAME,
					PRODUCT_NUMBER,
					PRODUCT_VENDOR_NAME,
					PRODUCT_SALES_PRICE)
					VALUES(?,?,?,?);'''

		with sqlite3.connect("SQL.db") as connection:

			try:
				cursor = connection.cursor()

				cursor.execute(new_product_sql_script,self.new_product_entry)

				connection.commit()

				cursor.close()

			except sqlite3.Error as error:

				print(f"NEW_PRODUCT_ENTRY ERROR: {error}")




class NEW_PRODUCT_WINDOW(tk.Toplevel):

	alive = False

	product_vendors = ["Select Vendor"]

	select_vendors_SQL_script = '''SELECT VENDOR_NAME FROM vendors;'''

	#Initiate SQL.db connection:

	with sqlite3.connect("SQL.db") as connection:

		cursor = connection.cursor()

		cursor.execute(select_vendors_SQL_script)

		for item in cursor:

			product_vendors.append(" ".join(item))

		connection.commit()

		cursor.close()

	def __init__(self,*args,**kwargs):

		super().__init__(*args,**kwargs)
		self.config(width=425,height=235)
		self.title("New Vendor Product")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.product_name_label = ttk.Label(self,text="Product Name:")
		self.product_name_label.place(x=20,y=20)
		self.product_name_entry = ttk.Entry(self)
		self.product_name_entry.place(x=200,y=20)

		self.product_number_label = ttk.Label(self,text="Product Number:")
		self.product_number_label.place(x=20,y=60)
		self.product_number_entry = ttk.Entry(self)
		self.product_number_entry.place(x=200,y=60)

		self.product_vendor_label = ttk.Label(self,text="Product Vendor:")
		self.product_vendor_label.place(x=20,y=100)
		self.clicked = tk.StringVar()
		self.clicked.set(f"{self.product_vendors[0]}")
		self.product_option_menu = ttk.OptionMenu(self,self.clicked,self.product_vendors[0],*self.product_vendors)
		self.product_option_menu.place(x=200,y=100)

		self.product_price_label = ttk.Label(self,text="Product Price:")
		self.product_price_label.place(x=20,y=140)
		self.product_price_entry = ttk.Entry(self)
		self.product_price_entry.place(x=200,y=140)

		self.new_product_button = ttk.Button(self,text="New Product",command=self.create_new_product)
		self.new_product_button.place(x=20,y=190)

		self.print_product_button = ttk.Button(self,text="Print Products",command=self.print_product_data)
		self.print_product_button.place(x=200,y=190)


	def create_new_product(self):

		product_data = []

		new_product_name = self.product_name_entry.get()
		new_product_number = self.product_number_entry.get()
		new_product_vendor_name = self.clicked.get()
		new_product_price = self.product_price_entry.get()

		if new_product_name == "":

			new_product_name_error_message_1 = tk.messagebox.showinfo(title="New Vendor Product",message="Product name cannot be blank.")

		elif new_product_number == "":

			new_product_number_error_message_1 = tk.messagebox.showinfo(title="New Vendor Product",message=f"New product number cannot be blank.")

		elif new_product_vendor_name == "Select Vendor":

			new_product_vendor_name_error_message_1 = tk.messagebox.showinfo(title="New Vendor Product",message="Product vendor name cannot be blank.")

		elif new_product_price == "":

			new_product_price_error_message_1 = tk.messagebox.showinfo(title="New Vendor Product",message="Product price cannot be blank.")

		else:

			try:

				verify_product_name_data = []

				verify_product_names_sql_script = '''SELECT PRODUCT_NAME FROM products;'''

				with sqlite3.connect("SQL.db") as connection:

					cursor = connection.cursor()

					cursor.execute(verify_product_names_sql_script)

					for item in cursor:

						verify_product_name_data.append(*item)

					connection.commit()

					cursor.close()

				if new_product_name in verify_product_name_data:

					duplicate_product_name_error_message = tk.messagebox.showinfo(title="New Vendor Product",message="Duplicate product name:  please use a different name for new product.")

				else:

					product_data.append(new_product_name)
					product_data.append(new_product_number)
					product_data.append(new_product_vendor_name)
					product_data.append(new_product_price)

					new_product = NEW_PRODUCT_ENTRY(product_data)

					new_product.enter_data()

					new_product_confirmation_message = tk.messagebox.showinfo(title="New Vendor Product",message="New Product created!")

					verify_product_name_data.clear()

			except Exception as error:

				new_product_error_message = tk.messagebox.showinfo(title="New Vendor Product",message=f"{error}")


	def print_product_data(self):

		print_product_sql_script = '''SELECT * FROM products;'''

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(print_product_sql_script)

				for item in cursor:

					print(item)

				connection.commit()

				cursor.close()

		except Exception as error:

			print_product_data_error_message_1 = tk.messagebox.showinfo(title="New Vendor Product",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
