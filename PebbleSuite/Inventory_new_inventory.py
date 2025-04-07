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

				add_inventory_confirmation_message = tk.messagebox.showinfo(title="Add Inventory",message=f"New product inventory added.")

		except sqlite3.Error as error:

			add_inventory_error_message = tk.messagebox.showinfo(title="Add Inventory",message=f"{error}")



class INVENTORY_JOURNAL_ENTRY:

	def __init__(self,inventory_journal_entry):

		self.inventory_journal_entry = inventory_journal_entry

	def enter_data(self):

		journal_entry_sql_script = '''INSERT INTO journal_entries(
						JOURNAL_ENTRY_TIMESTAMP,
						JOURNAL_ENTRY_NUMBER,
						JOURNAL_ENTRY_DATE,
						VENDOR_INVOICE_NUMBER,
						DEBIT_GENERAL_LEDGER_NAME,
						DEBIT_GENERAL_LEDGER_NUMBER,
						DEBIT_GENERAL_LEDGER_TYPE,
						CREDIT_GENERAL_LEDGER_NAME,
						CREDIT_GENERAL_LEDGER_NUMBER,
						CREDIT_GENERAL_LEDGER_TYPE,
						JOURNAL_ENTRY_DEBIT_AMOUNT,
						JOURNAL_ENTRY_CREDIT_AMOUNT,
						JOURNAL_ENTRY_VENDOR_NAME,
						JOURNAL_ENTRY_NOTES)
						VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''

		try:

			with sqlite3.connect("SQL.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as connection:

				cursor = connection.cursor()

				cursor.execute(journal_entry_sql_script,self.inventory_journal_entry)

				connection.commit()

				cursor.close()

		except sqlite3.Error as error:

			journal_entry_error_message = tk.messagebox.showinfo(title="Add Inventory",message=f"{error}")



class NEW_INVENTORY_WINDOW(tk.Toplevel):

	#Define class variables
	alive = False

	vendor_sql_script = '''SELECT VENDOR_NAME FROM vendors;'''

	inventory_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME from general_ledgers WHERE GENERAL_LEDGER_TYPE="Asset - Inventory";'''

	offset_GL_sql_script = '''SELECT GENERAL_LEDGER_NAME from general_ledgers;'''

	#Define class functions
	def __init__(self,*args,**kwargs):

		options = ["Select Vendor"]

		debit_GL_options = ["Select Inventory Account"]

		offset_GL_options = ["Select Offset Account"]

		#Initialize SQL.db connection:
		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.vendor_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()

		#Retrieve inventory GL names from SQL.db:
		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.inventory_GL_sql_script)

			for item in cursor:

				debit_GL_options.append(" ".join(item))

			connection.commit()

			cursor.close()

		#Retrieve offset GL names from SQL.db:
		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.offset_GL_sql_script)

			for item in cursor:

				offset_GL_options.append(" ".join(item))

			connection.commit()

			cursor.close()

		#Define class tkinter widgets:
		super().__init__(*args,**kwargs)
		self.config(width=610,height=760)
		self.title("Add Vendor Inventory")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.product_name_label = ttk.Label(self,text="Vendor Name:")
		self.product_name_label.place(x=20,y=15)

		#Search for vendor names in SQL.db.
		#Insert vendor names into vendor search listbox widget.
		self.select_vendor_scrollbar = ttk.Scrollbar(self)
		self.select_vendor_scrollbar.place(x=353,y=45,width=20,height=300)
		self.select_vendor_listbox = tk.Listbox(self,yscrollcommand=self.select_vendor_scrollbar.set)
		self.select_vendor_listbox.place(x=20,y=45,width=333,height=300)
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
		self.scrollbar.place(x=353,y=395,width=20,height=310)
		self.listbox = tk.Listbox(self,yscrollcommand=self.scrollbar.set)
		self.listbox.place(x=20,y=395,width=333,height=310)
		self.scrollbar.config(command=self.listbox.yview)

		self.search_products_button = ttk.Button(self,text="Search Products",command=self.search_products)
		self.search_products_button.place(x=20,y=355)

		self.clear_products_button = ttk.Button(self,text="Clear List",command=self.clear_products)
		self.clear_products_button.place(x=125,y=720)

		self.select_product_button = ttk.Button(self,text="Select Product",command=self.select_product)
		self.select_product_button.place(x=20,y=720)

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

		self.product_invoice_date_label = ttk.Label(self,text="Invoice Number:")
		self.product_invoice_date_label.place(x=400,y=155)
		self.product_invoice_date_entry_text = tk.StringVar()
		self.product_invoice_date_entry = ttk.Entry(self,textvariable=self.product_invoice_date_entry_text)
		self.product_invoice_date_entry.place(x=400,y=185)

		self.product_purchase_date_label = ttk.Label(self,text="Purchase Date:")
		self.product_purchase_date_label.place(x=400,y=225)
		self.product_purchase_date_entry_text = tk.StringVar()
		self.product_purchase_date_entry = ttk.Entry(self,textvariable=self.product_purchase_date_entry_text)
		self.product_purchase_date_entry.place(x=400,y=255)

		self.product_total_price_label = ttk.Label(self,text="Total Price:")
		self.product_total_price_label.place(x=400,y=295)
		self.product_total_price_entry_text = tk.StringVar()
		self.product_total_price_entry = ttk.Entry(self,textvariable=self.product_total_price_entry_text)
		self.product_total_price_entry.place(x=400,y=325)

		self.product_exp_date_label = ttk.Label(self,text="Expiration Date:")
		self.product_exp_date_label.place(x=400,y=365)
		self.product_exp_date_entry_text = tk.StringVar()
		self.product_exp_date_entry = ttk.Entry(self,textvariable=self.product_exp_date_entry_text)
		self.product_exp_date_entry.place(x=400,y=395)

		self.product_unit_quantity_label = ttk.Label(self,text="Unit Quantity:")
		self.product_unit_quantity_label.place(x=400,y=435)
		self.product_unit_quantity_entry_text = tk.StringVar()
		self.product_unit_quantity_entry = ttk.Entry(self,textvariable=self.product_unit_quantity_entry_text)
		self.product_unit_quantity_entry.place(x=400,y=465)

		self.product_unit_price_label = ttk.Label(self,text="Unit Price:")
		self.product_unit_price_label.place(x=400,y=505)
		self.product_unit_price_entry_text = tk.StringVar()
		self.product_unit_price_entry = ttk.Entry(self,textvariable=self.product_unit_price_entry_text)
		self.product_unit_price_entry.place(x=400,y=535)

		self.product_debit_gl_label = ttk.Label(self,text="Debit GL:")
		self.product_debit_gl_label.place(x=400,y=575)
		self.product_debit_gl_entry_text = tk.StringVar()
		self.product_debit_gl_entry_text.set(f"{debit_GL_options[0]}")
		self.product_debit_gl_option_menu = ttk.OptionMenu(self,self.product_debit_gl_entry_text,debit_GL_options[0],*debit_GL_options)
		self.product_debit_gl_option_menu.place(x=400,y=605)

		self.product_credit_gl_label = ttk.Label(self,text="Credit GL:")
		self.product_credit_gl_label.place(x=400,y=645)
		self.product_credit_gl_entry_text = tk.StringVar()
		self.product_credit_gl_entry_text.set(f"{offset_GL_options[0]}")
		self.product_credit_gl_option_menu = ttk.OptionMenu(self,self.product_credit_gl_entry_text,offset_GL_options[0],*offset_GL_options)
		self.product_credit_gl_option_menu.place(x=400,y=675)

		self.cancel_product_changes_button = ttk.Button(self,text="Close",command=self.cancel_changes)
		self.cancel_product_changes_button.place(x=490,y=720)

		self.submit_product_changes_button = ttk.Button(self,text="Save",command=self.submit_changes)
		self.submit_product_changes_button.place(x=400,y=720)


	def search_products(self):

		search_product_sql_script = '''SELECT PRODUCT_NAME FROM products WHERE PRODUCT_VENDOR_NAME=?;'''

		try:

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

				search_products_error_message_1 = tk.messagebox.showinfo(title="Add Inventory",message=f"{error}")

		except:

			search_producs_error_message_2 = tk.messagebox.showinfo(title="Add Inventory",message="Select vendor name from list.")


	def clear_products(self):

		try:

			self.listbox.delete(0,tk.END)

		except:

			clear_products_error_message_1 = tk.messagebox.showinfo(title="Add Inventory",message="Unable to clear product list.")


	def select_product(self):

		#Define SQL.db scripts:
		query_product_sql_script = '''SELECT * FROM products WHERE PRODUCT_NAME=?;'''

		try:

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

				edit_product_error_message_1 = tk.messagebox.showinfo(title="Add Inventory",message=f"{error}")

		except:

			edit_product_error_message_2 = tk.messagebox.showinfo(title="Add Inventory",message="Select product from list.")


	def submit_changes(self):

		try:

			#Collect inventory sql entry data:

			product_data = []

			vendor_name = self.vendor_name_entry_text.get()
			product_name = self.product_name_entry_text.get()
			product_purchase_date = self.product_purchase_date_entry_text.get()
			product_purchase_price = self.product_total_price_entry_text.get()
			product_expiration_date = self.product_exp_date_entry_text.get()
			product_unit_quantity = self.product_unit_quantity_entry_text.get()
			product_unit_price = self.product_unit_price_entry_text.get()

			#Collect journal entry data for new inventory:

			journal_entry_data = []

			journal_entry_timestamp = datetime.datetime.now()
			journal_entry_number = None
			journal_entry_date = self.product_purchase_date_entry_text.get()
			vendor_invoice_number = self.product_invoice_date_entry_text.get()
			debit_general_ledger_name = self.product_debit_gl_entry_text.get()
			debit_general_ledger_number = None
			debit_general_ledger_type = None
			credit_general_ledger_name = self.product_credit_gl_entry_text.get()
			credit_general_ledger_number = None
			credit_general_ledger_type = None
			journal_entry_debit_amount = self.product_total_price_entry_text.get()
			journal_entry_credit_amount = self.product_total_price_entry_text.get()
			journal_entry_vendor_name = self.vendor_name_entry_text.get()
			journal_entry_notes = None

			#Error handling:

			if vendor_name == "":

				vendor_name_error_message_1 = tk.messagebox.showinfo(title="Add Vendor Inventory",message="Vendor name cannot be blank.")

			elif product_name == "":

				product_name_error_message_1 = tk.messagebox.showinfo(title="Add Vendor Inventory",message="Product name cannot be blank.")

			elif vendor_invoice_number == "":

				vendor_invoice_number_error_message_1 = tk.messagebox.showinfo(title="Add Vendor Inventory",message="Vendor invoice number cannot be blank.")

			elif product_purchase_date == "":

				product_purchase_date_error_message_1 = tk.messagebox.showinfo(title="Add Vendor Inventory",message="Product purchase date cannot be blank.")

			elif product_purchase_price == "":

				product_purchase_price_error_message_1 = tk.messagebox.showinfo(title="Add Vendor Inventory",message="Product total price cannot be blank.")

			elif product_expiration_date == "":

				product_expiration_date_error_message_1 = tk.messagebox.showinfo(title="Add Vendor Inventory",message="Product expiration date cannot be blank.")

			elif product_unit_quantity == "":

				product_unit_quantity_error_message_1 = tk.messagebox.showinfo(title="Add Vendor Inventory",message="Unit quantity cannot be blank.")

			elif product_unit_price == "":

				product_unit_price_error_message_1 = tk.messagebox.showinfo(title="Add Vendor Invoice",message="Unit price cannot be blank.")

			elif debit_general_ledger_name == "Select Inventory Account":

				debit_gl_error_message = tk.messagebox.showinfo(title="Add Vendor Inventory",message="Please select a debit GL")

			elif credit_general_ledger_name == "Select Offset Account":

				credit_gl_error_message = tk.messagebox.showinfo(title="Add Vendor Inventory",message="Please select a credit account")

			else:

				product_data.append(vendor_name)
				product_data.append(product_name)
				product_data.append(product_purchase_date)
				product_data.append(product_purchase_price)
				product_data.append(product_expiration_date)
				product_data.append(product_unit_quantity)
				product_data.append(product_unit_price)

				inventory_sql_entry = ADD_INVENTORY(product_data)
				inventory_sql_entry.enter_data()

				journal_entry_data.append(journal_entry_timestamp)
				journal_entry_data.append(journal_entry_number)
				journal_entry_data.append(journal_entry_date)
				journal_entry_data.append(vendor_invoice_number)
				journal_entry_data.append(debit_general_ledger_name)
				journal_entry_data.append(debit_general_ledger_number)
				journal_entry_data.append(debit_general_ledger_type)
				journal_entry_data.append(credit_general_ledger_name)
				journal_entry_data.append(credit_general_ledger_number)
				journal_entry_data.append(credit_general_ledger_type)
				journal_entry_data.append(journal_entry_debit_amount)
				journal_entry_data.append(journal_entry_credit_amount)
				journal_entry_data.append(journal_entry_vendor_name)
				journal_entry_data.append(journal_entry_notes)

				journal_entry_sql_entry = INVENTORY_JOURNAL_ENTRY(journal_entry_data)
				journal_entry_sql_entry.enter_data()

				product_data.clear()
				journal_entry_data.clear()

		except Exception as error:

			add_inventory_error_message = tk.messagebox.showinfo(title="Add Vendor Inventory",message=f"{error}")


	def cancel_changes(self):

		try:

			self.vendor_name_entry_text.set("")
			self.product_name_entry_text.set("")
			self.product_purchase_date_entry_text.set("")
			self.product_total_price_entry_text.set("")
			self.product_exp_date_entry_text.set("")
			self.product_unit_quantity_entry_text.set("")
			self.product_unit_price_entry_text.set("")

		except Exception as error:

			cancel_changes_error_message = tk.messagebox.showinfo(title="Add Vendor Inventory",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
