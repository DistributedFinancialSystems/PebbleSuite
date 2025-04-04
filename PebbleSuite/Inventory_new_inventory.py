#Python Standard Library dependencies

import datetime
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo


class ADD_INVENTORY:

	def __init__(self,new_inventory_entry):

		self.new_inventory_entry = new_inventory_entry

	def enter_data(self):

		new_inventory_sql_script = '''INSERT INTO inventory(
						PRODUCT_VENDOR_NAME,
						PRODUCT_NAME,
						PRODUCT_PURCHASE_DATE,
						PRODUCT_TOTAL_PURCHASE_PRICE,
						PRODUCT_EXPIRATION_DATE,
						PRODUCT_UNIT_QUANTITY,
						PRODUCT_UNIT_WHOLESALE_PRICE)
						VALUES(?,?,?,?,?,?,?);'''

		try:

			with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

				cursor = connection.cursor()

				cursor.execute(new_inventory_sql_script,self.new_inventory_entry)

				connection.commit()

				cursor.close()

				add_inventory_confirmation_message = tk.messagebox.showinfo(title="Add Inventry",message=f"New product inventory added.")

		except sqlite3.Error as error:

			add_inventory_error_message = tk.messagebox.showinfo(title="Add Inventory",message=f"{error}")


"""
class INVENTORY_JOURNAL_ENTRY:

	def __init__(self,inventory_journal_entry):

		self.inventory_journal_entry = inventory_journal_entry

	def enter_data(self):

		journal_entry_sql_script = '''INSERT INTO journal_entries(
						LDLDLD,
						BABABA)
						VALUES(?,?);'''

		with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

			cursor = connection.cursor()

			cursor.execute(journal_entry_sql_script,self.inventory_journal_entry)

			connection.commit()

			cursor.close()
"""


class NEW_INVENTORY_WINDOW(tk.Toplevel):

	#Define class variables
	alive = False

	vendor_sql_script = '''SELECT VENDOR_NAME FROM vendors;'''

	#Define class functions
	def __init__(self,*args,**kwargs):

		options = ["Select Vendor"]


		#Initialize SQL.db connection:
		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.vendor_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()

		#Define class tkinter widgets:
		super().__init__(*args,**kwargs)
		self.config(width=600,height=550)
		self.title("Add Vendor Inventory")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.product_name_label = ttk.Label(self,text="Vendor Name")
		self.product_name_label.place(x=20,y=15)

		#Search for vendor names in SQL.db.
		#Insert vendor names into vendor search listbox widget.
		self.select_vendor_scrollbar = ttk.Scrollbar(self)
		self.select_vendor_scrollbar.place(x=353,y=45,width=20,height=200)
		self.select_vendor_listbox = tk.Listbox(self,yscrollcommand=self.select_vendor_scrollbar.set)
		self.select_vendor_listbox.place(x=20,y=45,width=333,height=200)
		self.select_vendor_scrollbar.config(command=self.select_vendor_listbox.yview)

		search_vendor_name_sql_script = '''SELECT VENDOR_NAME FROM vendors;'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(search_vendor_name_sql_script)

			connection.commit()

			for item in cursor:

				self.select_vendor_listbox.insert(0," ".join(item))

			cursor.close()

		#Invoice selection listbox widget:
		self.scrollbar = ttk.Scrollbar(self)
		self.scrollbar.place(x=353,y=300,width=20,height=200)
		self.listbox = tk.Listbox(self,yscrollcommand=self.scrollbar.set)
		self.listbox.place(x=20,y=300,width=333,height=200)
		self.scrollbar.config(command=self.listbox.yview)

		self.search_products_button = ttk.Button(self,text="Search Products",command=self.search_products)
		self.search_products_button.place(x=20,y=255)

		self.clear_products_button = ttk.Button(self,text="Clear List",command=self.clear_products)
		self.clear_products_button.place(x=120,y=510)

		self.select_product_button = ttk.Button(self,text="Select Product",command=self.select_product)
		self.select_product_button.place(x=20,y=510)

		self.vendor_name_label = ttk.Label(self,text="Vendor Name:")
		self.vendor_name_label.place(x=400,y=15)
		self.vendor_name_entry_text = tk.StringVar()
		self.vendor_name_entry = ttk.Entry(self,textvariable=self.vendor_name_entry_text,state=tk.DISABLED)
		self.vendor_name_entry.place(x=400,y=45)

		self.product_name_label = ttk.Label(self,text="Product Name:")
		self.product_name_label.place(x=400,y=85)
		self.product_name_entry_text = tk.StringVar()
		self.product_name_entry = ttk.Entry(self,textvariable=self.product_name_entry_text,state=tk.DISABLED)
		self.product_name_entry.place(x=400,y=115)

		self.product_purchase_date_label = ttk.Label(self,text="Purchase Date:")
		self.product_purchase_date_label.place(x=400,y=155)
		self.product_purchase_date_entry_text = tk.StringVar()
		self.product_purchase_date_entry = ttk.Entry(self,textvariable=self.product_purchase_date_entry_text)
		self.product_purchase_date_entry.place(x=400,y=185)

		self.product_total_price_label = ttk.Label(self,text="Total Price:")
		self.product_total_price_label.place(x=400,y=225)
		self.product_total_price_entry_text = tk.StringVar()
		self.product_total_price_entry = ttk.Entry(self,textvariable=self.product_total_price_entry_text)
		self.product_total_price_entry.place(x=400,y=255)

		self.product_exp_date_label = ttk.Label(self,text="Expiration Date:")
		self.product_exp_date_label.place(x=400,y=295)
		self.product_exp_date_entry_text = tk.StringVar()
		self.product_exp_date_entry = ttk.Entry(self,textvariable=self.product_exp_date_entry_text)
		self.product_exp_date_entry.place(x=400,y=325)

		self.product_unit_quantity_label = ttk.Label(self,text="Unit Quantity:")
		self.product_unit_quantity_label.place(x=400,y=365)
		self.product_unit_quantity_entry_text = tk.StringVar()
		self.product_unit_quantity_entry = ttk.Entry(self,textvariable=self.product_unit_quantity_entry_text)
		self.product_unit_quantity_entry.place(x=400,y=395)

		self.product_unit_price_label = ttk.Label(self,text="Unit Price:")
		self.product_unit_price_label.place(x=400,y=435)
		self.product_unit_price_entry_text = tk.StringVar()
		self.product_unit_price_entry = ttk.Entry(self,textvariable=self.product_unit_price_entry_text)
		self.product_unit_price_entry.place(x=400,y=465)

		self.cancel_product_changes_button = ttk.Button(self,text="Close",command=self.cancel_changes)
		self.cancel_product_changes_button.place(x=490,y=510)

		self.submit_product_changes_button = ttk.Button(self,text="Save",command=self.submit_changes)
		self.submit_product_changes_button.place(x=400,y=510)


	def search_products(self):

		search_product_sql_script = '''SELECT PRODUCT_NAME FROM products WHERE PRODUCT_VENDOR_NAME=?;'''

		for item in self.select_vendor_listbox.curselection():

			select_product = self.select_vendor_listbox.get(item)

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(search_product_sql_script,[select_product])

				for item in cursor:

					self.listbox.insert(0," ".join(item))

				connection.commit()

				cursor.close()

		except sqlite3.Error as error:

			search_products_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")


	def clear_products(self):

		self.listbox.delete(0,tk.END)


	def select_product(self):

		#Define SQL.db scripts:
		query_product_sql_script = '''SELECT * FROM products WHERE PRODUCT_NAME=?;'''

		for item in self.listbox.curselection():

			select_product = self.listbox.get(item)

		try:

			with sqlite3.connect("SQL.db") as connection:

				collect = []

				cursor = connection.cursor()

				cursor.execute(query_product_sql_script,[select_product])

				for item in cursor:

					collect.append(item)

				self.vendor_name_entry_text.set(f"{collect[0][2]}")
				self.product_name_entry_text.set(f"{collect[0][0]}")

				connection.commit()

				cursor.close()

		except sqlite3.Error as error:

			edit_product_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")


	def submit_changes(self):

		#Define SQL.db scripts:

		product_data = []

		vendor_name = self.vendor_name_entry_text.get()
		product_name = self.product_name_entry_text.get()
		product_purchase_date = self.product_purchase_date_entry_text.get()
		product_purchase_price = self.product_total_price_entry_text.get()
		product_expiration_date = self.product_exp_date_entry_text.get()
		product_unit_quantity = self.product_unit_quantity_entry_text.get()
		product_unit_price = self.product_unit_price_entry_text.get()

		product_data.append(vendor_name)
		product_data.append(product_name)
		product_data.append(product_purchase_date)
		product_data.append(product_purchase_price)
		product_data.append(product_expiration_date)
		product_data.append(product_unit_quantity)
		product_data.append(product_unit_price)

		inventory_sql_entry = ADD_INVENTORY(product_data)
		inventory_sql_entry.enter_data()


	def cancel_changes(self):

		try:

			self.vendor_name_entry_text.set("")
			self.product_name_entry_text.set("")
			self.product_purchase_date_entry_text.set("")
			self.product_total_price_entry_text.set("")
			self.product_exp_date_entry_text.set("")
			self.product_unit_quantity_entry_text.set("")
			self.product_unit_price_entry_text.set("")

		except:

			cancel_changes_error_message = tk.messagebox.showinfo(title="Error",message="Unable to clear data entries.")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
