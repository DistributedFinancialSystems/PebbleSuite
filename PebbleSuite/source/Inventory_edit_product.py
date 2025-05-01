import datetime
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class EDIT_PRODUCT_WINDOW(tk.Toplevel):

	alive = False

	edit_selection_temporary_memory = []

	product_sql_script = '''SELECT PRODUCT_NAME FROM products;'''

	def __init__(self,*args,**kwargs):

		options = ["Select Product"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.product_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()

		super().__init__(*args,**kwargs)
		self.config(width=600,height=340)
		self.title("Edit Product")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.product_name_label = ttk.Label(self,text="Product Name:")
		self.product_name_label.place(x=20,y=15)

		self.select_product_scrollbar = ttk.Scrollbar(self)
		self.select_product_scrollbar.place(x=353,y=45,width=20,height=240)
		self.select_product_listbox = tk.Listbox(self,yscrollcommand=self.select_product_scrollbar.set)
		self.select_product_listbox.place(x=20,y=45,width=333,height=240)
		self.select_product_scrollbar.config(command=self.select_product_listbox.yview)

		search_product_name_sql_script = '''SELECT PRODUCT_NAME FROM products;'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(search_product_name_sql_script)

			connection.commit()

			for item in cursor:

				self.select_product_listbox.insert(0," ".join(item))

			cursor.close()

		self.edit_product_button = ttk.Button(self,text="Edit Product",command=self.edit_product)
		self.edit_product_button.place(x=20,y=300)

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

		self.submit_product_changes_button = ttk.Button(self,text="Save",command=self.submit_changes)
		self.submit_product_changes_button.place(x=400,y=300)


	def edit_product(self):

		try:

			query_product_sql_script = '''SELECT * FROM products WHERE PRODUCT_NAME=?'''

			for item in self.select_product_listbox.curselection():

				select_product = self.select_product_listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				collect = []

				cursor = connection.cursor()

				cursor.execute(query_product_sql_script,[select_product])

				for item in cursor:

					collect.append(item)

					self.edit_selection_temporary_memory.append(item)

				self.product_name_entry_text.set(f"{collect[0][0]}")
				self.product_number_entry_text.set(f"{collect[0][1]}")
				self.product_vendor_name_entry_text.set(f"{collect[0][2]}")
				self.product_sales_price_entry_text.set(f"{collect[0][3]}")

				connection.commit()

				cursor.close()

		except Exception as error:

			edit_product_error_message = tk.messagebox.showinfo(title="Edit Product",message=f"{error}")


	def submit_changes(self):

		try:

			retrieve_product_sql_script = '''SELECT * FROM products WHERE PRODUCT_NAME=?;'''
			edit_product_number_sql_script = '''UPDATE products SET PRODUCT_NUMBER=? WHERE PRODUCT_NUMBER=? AND PRODUCT_NAME=? AND PRODUCT_VENDOR_NAME=?;'''
			edit_product_price_sql_script = '''UPDATE products SET PRODUCT_SALES_PRICE=? WHERE PRODUCT_SALES_PRICE=? AND PRODUCT_NAME=? AND PRODUCT_VENDOR_NAME=?;'''

			product_name = self.edit_selection_temporary_memory[0][0]

			prev_product_number = self.edit_selection_temporary_memory[0][1]
			new_product_number = self.product_number_entry_text.get()

			vendor_name = self.edit_selection_temporary_memory[0][2]

			prev_product_sales_price = self.edit_selection_temporary_memory[0][3]
			new_product_sales_price = self.product_sales_price_entry_text.get()

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(edit_product_number_sql_script,(new_product_number,prev_product_number,product_name,vendor_name))
				cursor.execute(edit_product_price_sql_script,(new_product_sales_price,prev_product_sales_price,product_name,vendor_name))

				connection.commit()

				cursor.close()

				edit_product_names_confirmation_message = tk.messagebox.showinfo("Edit Product",message="Product details successfully changed.")

			self.edit_selection_temporary_memory.clear()

			self.product_name_entry_text.set("")
			self.product_number_entry_text.set("")
			self.product_vendor_name_entry_text.set("")
			self.product_sales_price_entry_text.set("")

		except Exception as error:

			submit_changes_error_message_1 = tk.messagebox.showinfo(title="Edit Product",message=f"{error}")


	def cancel_changes(self):

		try:

			self.edit_selection_temporary_memory.clear()

			self.product_name_entry_text.set("")
			self.product_number_entry_text.set("")
			self.product_vendor_name_entry_text.set("")
			self.product_sales_price_entry_text.set("")

		except Exception as error:

			cancel_changes_error_message = tk.messagebox.showinfo(title="Edit Product",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
