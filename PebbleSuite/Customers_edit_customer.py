import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import stripe
import time



class EDIT_CUSTOMER_WINDOW(tk.Toplevel):

	"""
	_______________________________________
	Define class variables and SQL scripts:
	_______________________________________
	"""
	alive = False

	customer_sql_script = '''SELECT CUSTOMER_NAME FROM customers;'''

	def __init__(self,*args,**kwargs):

		"""
		___________________________________
		Retrieve customer data from SQL.db:
		___________________________________
		"""
		customer_data = []

		options = ["Select Customer"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.customer_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()
		"""
		"""

		"""
		_______________________
		Define Tkinter widgets:
		_______________________
		"""
		super().__init__(*args,**kwargs)
		self.config(width=700,height=505)
		self.title("Edit Customer")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		"""
		"""

		"""
		________________________________________________________
		RETRIEVE CUSTOMER NAMES FROM SQL.DB, ENTER INTO LISTBOX.
		________________________________________________________
		"""

		self.customers_label = ttk.Label(self,text="Customers:")
		self.customers_label.place(x=20,y=20)
		self.sort_customers_button = ttk.Button(self,text="Sort Customers A-Z",command=self.sort_customers)
		self.sort_customers_button.place(x=120,y=20)

		self.customer_scrollbar = ttk.Scrollbar(self)
		self.customer_scrollbar.place(x=240,y=60,width=20,height=380)
		self.customer_listbox = tk.Listbox(self,yscrollcommand=self.customer_scrollbar.set)
		self.customer_listbox.place(x=20,y=60,width=220,height=380)
		self.customer_scrollbar.config(command=self.customer_listbox.yview)

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.customer_sql_script)

			for item in cursor:

				self.customer_listbox.insert(0," ".join(item))

			connection.commit()

			cursor.close()

		self.search_customer_data_button = ttk.Button(self,text="Retrieve Customer Data",command=self.search_customer_data)
		self.search_customer_data_button.place(x=20,y=460)

		self.customer_name_label = ttk.Label(self,text="Customer:")
		self.customer_name_label.place(x=300,y=20)
		self.customer_name = tk.StringVar()
		self.customer_name_entry = ttk.Entry(self,textvariable=self.customer_name,state=tk.DISABLED)
		self.customer_name_entry.place(x=500,y=20)

		self.customer_address1_label = ttk.Label(self,text="Address 1:")
		self.customer_address1_label.place(x=300,y=60)
		self.customer_address1_entry_text = tk.StringVar()
		self.customer_address1_entry = ttk.Entry(self,textvariable=self.customer_address1_entry_text)
		self.customer_address1_entry.place(x=500,y=60)

		self.customer_address2_label = tk.Label(self,text="Address 2:")
		self.customer_address2_label.place(x=300,y=100)
		self.customer_address2_entry_text = tk.StringVar()
		self.customer_address2_entry = ttk.Entry(self,textvariable=self.customer_address2_entry_text)
		self.customer_address2_entry.place(x=500,y=100)

		self.customer_city_label = ttk.Label(self,text="City:")
		self.customer_city_label.place(x=300,y=140)
		self.customer_city_entry_text = tk.StringVar()
		self.customer_city_entry = tk.Entry(self,textvariable=self.customer_city_entry_text)
		self.customer_city_entry.place(x=500,y=140)

		self.customer_state_label = ttk.Label(self,text="State/Province/Territory:")
		self.customer_state_label.place(x=300,y=180)
		self.customer_state_entry_text = tk.StringVar()
		self.customer_state_entry = ttk.Entry(self,textvariable=self.customer_state_entry_text)
		self.customer_state_entry.place(x=500,y=180)

		self.customer_zip_postal_code_label = ttk.Label(self,text="ZIP Code/Postal Code:")
		self.customer_zip_postal_code_label.place(x=300,y=220)
		self.customer_zip_postal_code_entry_text = tk.StringVar()
		self.customer_zip_postal_code_entry = ttk.Entry(self,textvariable=self.customer_zip_postal_code_entry_text)
		self.customer_zip_postal_code_entry.place(x=500,y=220)

		self.customer_country_label = ttk.Label(self,text="Country:")
		self.customer_country_label.place(x=300,y=260)
		self.customer_country_entry_text = tk.StringVar()
		self.customer_country_entry = tk.Entry(self,textvariable=self.customer_country_entry_text)
		self.customer_country_entry.place(x=500,y=260)

		self.customer_contact_name_label = ttk.Label(self,text="Customer Contact Name:")
		self.customer_contact_name_label.place(x=300,y=300)
		self.customer_contact_name_entry_text = tk.StringVar()
		self.customer_contact_name_entry = ttk.Entry(self,textvariable=self.customer_contact_name_entry_text)
		self.customer_contact_name_entry.place(x=500,y=300)

		self.customer_contact_phone_label = ttk.Label(self,text="Customer Contact Phone:")
		self.customer_contact_phone_label.place(x=300,y=340)
		self.customer_contact_phone_entry_text = tk.StringVar()
		self.customer_contact_phone_entry = ttk.Entry(self,textvariable=self.customer_contact_phone_entry_text)
		self.customer_contact_phone_entry.place(x=500,y=340)

		self.customer_contact_email_label = ttk.Label(self,text="Customer Contact Email:")
		self.customer_contact_email_label.place(x=300,y=380)
		self.customer_contact_email_entry_text = tk.StringVar()
		self.customer_contact_email_entry = ttk.Entry(self,textvariable=self.customer_contact_email_entry_text)
		self.customer_contact_email_entry.place(x=500,y=380)

		self.customer_contact_notes_label = ttk.Label(self,text="Customer Contact Notes:")
		self.customer_contact_notes_label.place(x=300,y=420)
		self.customer_contact_notes_entry_text = tk.StringVar()
		self.customer_contact_notes_entry = ttk.Entry(self,textvariable=self.customer_contact_notes_entry_text)
		self.customer_contact_notes_entry.place(x=500,y=420)

		self.clear_data_entries_button = ttk.Button(self,text="Clear Data Entries",command=self.clear_data_entries)
		self.clear_data_entries_button.place(x=300,y=460)

		self.change_customer_data_button = ttk.Button(self,text="Submit Data Changes",command=self.change_customer_data)
		self.change_customer_data_button.place(x=500,y=460)

		self.customer_stripe_id = tk.StringVar()


	def sort_customers(self):

		try:

			pass

		except Exception as error:

			sort_customers_error_message_1 = tk.messagebox.showinfo(title="Edit Customer",message=f"{error}")


	def search_customer_data(self):

		try:

			collect = []

			search_customers_sql_script = '''SELECT * FROM customers WHERE CUSTOMER_NAME=?'''

			for item in self.customer_listbox.curselection():

				select_customer = self.customer_listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(search_customers_sql_script,[select_customer])

				for item in cursor:

					collect.append(item)

				self.customer_name.set(f"{collect[0][0]}")
				self.customer_address1_entry_text.set(f"{collect[0][1]}")
				self.customer_address2_entry_text.set(f"{collect[0][2]}")
				self.customer_city_entry_text.set(f"{collect[0][3]}")
				self.customer_state_entry_text.set(f"{collect[0][4]}")
				self.customer_zip_postal_code_entry_text.set(f"{collect[0][5]}")
				self.customer_country_entry_text.set(f"{collect[0][6]}")
				self.customer_contact_name_entry_text.set(f"{collect[0][7]}")
				self.customer_contact_phone_entry_text.set(f"{collect[0][8]}")
				self.customer_contact_email_entry_text.set(f"{collect[0][9]}")
				self.customer_contact_notes_entry_text.set(f"{collect[0][10]}")
				self.customer_stripe_id.set(f"{collect[0][11]}")

				connection.commit()

				cursor.close()

		except Exception as error:

			search_customer_data_error_message_1 = tk.messagebox.showinfo(title="Edit Customer",message=f"{error}")

	def clear_data_entries(self):

		try:

			self.customer_name.set("")
			self.customer_address1_entry_text.set("")
			self.customer_address2_entry_text.set("")
			self.customer_city_entry_text.set("")
			self.customer_state_entry_text.set("")
			self.customer_zip_postal_code_entry_text.set("")
			self.customer_country_entry_text.set("")
			self.customer_contact_name_entry_text.set("")
			self.customer_contact_phone_entry_text.set("")
			self.customer_contact_email_entry_text.set("")
			self.customer_contact_notes_entry_text.set("")
			self.customer_stripe_id.set("")

		except Exception as error:

			clear_data_entries_error_message_1 = tk.messagebox.showinfo(title="Edit Customer",message=f"{error}")


	def change_customer_data(self):

		try:

			retrieve_customers_sql_script = '''SELECT * FROM customers;'''
			edit_customer_address1_sql_script = '''UPDATE customers SET ADDRESS_1=? WHERE CUSTOMER_NAME=?;'''
			edit_customer_address2_sql_script = '''UPDATE customers SET ADDRESS_2=? WHERE CUSTOMER_NAME=?;'''
			edit_customer_city_sql_script = '''UPDATE customers SET CITY=? WHERE CUSTOMER_NAME=?;'''
			edit_customer_state_sql_script = '''UPDATE customers SET STATE=? WHERE CUSTOMER_NAME=?;'''
			edit_customer_zip_sql_script = '''UPDATE customers SET POSTAL_CODE=? WHERE CUSTOMER_NAME=?;'''
			edit_customer_country_sql_script = '''UPDATE customers SET COUNTRY=? WHERE CUSTOMER_NAME=?;'''
			edit_contact_name_sql_script = '''UPDATE customers SET CONTACT_NAME=? WHERE CUSTOMER_NAME=?;'''
			edit_contact_phone_sql_script = '''UPDATE customers SET CONTACT_PHONE=? WHERE CUSTOMER_NAME=?;'''
			edit_contact_email_sql_script = '''UPDATE customers SET CONTACT_EMAIL=? WHERE CUSTOMER_NAME=?;'''
			edit_customer_notes_sql_script = '''UPDATE customers SET CUSTOMER_NOTES=? WHERE CUSTOMER_NAME=?;'''

			search_customer_name = self.customer_name.get()
			new_address1 = self.customer_address1_entry.get()
			new_address2 = self.customer_address2_entry.get()
			new_city = self.customer_city_entry.get()
			new_state = self.customer_state_entry.get()
			new_zip = self.customer_zip_postal_code_entry.get()
			new_country = self.customer_country_entry.get()
			new_contact_name = self.customer_contact_name_entry.get()
			new_contact_phone = self.customer_contact_phone_entry.get()
			new_contact_email = self.customer_contact_email_entry.get()
			new_customer_notes = self.customer_contact_notes_entry.get()

			if search_customer_name == "":

				edit_customer_error_message_1 = tk.messagebox.showinfo(title="Edit Customer",message="Select a customer to edit.")

			else:

				stripe_id_sql_script = '''SELECT STRIPE_API_KEY FROM stripe_api_key;'''

				stripe_api_key = tk.StringVar()

				with sqlite3.connect("SQL.db") as connection:

					"""
					_______________________________
					Update customer data in SQL.db:
					_______________________________
					"""

					cursor = connection.cursor()

					cursor.execute(edit_customer_address1_sql_script,(new_address1,search_customer_name))
					cursor.execute(edit_customer_address2_sql_script,(new_address2,search_customer_name))
					cursor.execute(edit_customer_city_sql_script,(new_city,search_customer_name))
					cursor.execute(edit_customer_state_sql_script,(new_state,search_customer_name))
					cursor.execute(edit_customer_zip_sql_script,(new_zip,search_customer_name))
					cursor.execute(edit_customer_country_sql_script,(new_country,search_customer_name))
					cursor.execute(edit_contact_name_sql_script,(new_contact_name,search_customer_name))
					cursor.execute(edit_contact_phone_sql_script,(new_contact_phone,search_customer_name))
					cursor.execute(edit_contact_email_sql_script,(new_contact_email,search_customer_name))
					cursor.execute(edit_customer_notes_sql_script,(new_customer_notes,search_customer_name))

					"""
					____________________________________
					Retrieve Stripe API key from SQL.db:
					____________________________________
					"""

					cursor.execute(stripe_id_sql_script)

					for item in cursor:

						stripe_api_key.set(*item)

					"""
					_______________________________________
					Update customer data in Stripe account:
					_______________________________________
					"""

					get_stripe_api_key = stripe_api_key.get() #Good

					customer_stripe_id = self.customer_stripe_id.get() #Good

					stripe.api_key = get_stripe_api_key

					update_customer = stripe.Customer.modify(customer_stripe_id,email=f'{new_contact_email}')

					time.sleep(10)

					stripe_process_message_1 = tk.messagebox.showinfo(title="Edit Customer",message="Updating customer details in Stripe account.")

					time.sleep(10)

					connection.commit()

					cursor.close()

				edit_customer_confirmation_message_1 = tk.messagebox.showinfo(title="Edit Customer",message="Customer details successfully changed.")

		except Exception as error:

			edit_customer_error_message_1 = tk.messagebox.showinfo(title="Edit Customer",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
