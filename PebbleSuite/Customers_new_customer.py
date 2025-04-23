import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import stripe
import time




class NEW_CUSTOMER_ENTRY:

	def __init__(self,new_customer_entry):

		self.new_customer_entry = new_customer_entry

	def enter_data(self):

		new_customer_sql_script = '''INSERT INTO customers(
					CUSTOMER_NAME,
					ADDRESS_1,
					ADDRESS_2,
					CITY,
					STATE,
					POSTAL_CODE,
					COUNTRY,
					CONTACT_NAME,
					CONTACT_PHONE,
					CONTACT_EMAIL,
					CUSTOMER_NOTES,
					STRIPE_ID)
					VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(new_customer_sql_script,self.new_customer_entry)

			connection.commit()

			cursor.close()

	def stripe_entry(self,customer_name):

		try:

			stripe_api_key = None

			customer_id = None

			retrieve_stripe_api_key = '''SELECT * FROM stripe_api_key;'''

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(retrieve_stripe_api_key)

				for item in cursor:

					stripe_api_key = str(*item)

				connection.commit()

				cursor.close()

			stripe.api_key = stripe_api_key

			customer = stripe.Customer.create(name=customer_name)

			stripe_entry_confirmation_message_1 = tk.messagebox.showinfo(title="Add New Customer",message="Adding Customer to Stripe Account.")

			time.sleep(10)

			stripe_entry_confirmation_message_2 = tk.messagebox.showinfo(title="Add New Customer",message="Retrieving New Customer Data.")

			time.sleep(10)

			new_customer_data = stripe.Customer.search(query=f"name: '{customer_name}'")

			for item in new_customer_data:

				print(item)

				print("\n\n\n\n\n")

				print(item["id"])

				customer_id = item["id"]

				print(f"customer id: {customer_id}")

			print(f"customer id: {customer_id}")

		except Exception as error:

			stripe_entry_error_message_1 = tk.messagebox.showinfo(title="Add New Customer",message=f"{error}")



class NEW_CUSTOMER_WINDOW(tk.Toplevel):

	alive = False

	def __init__(self,*args,**kwargs):

		super().__init__(*args,**kwargs)
		self.config(width=390,height=520)
		self.title("Add New Customer")
		self.focus()
		self.resizable,(0,0)
		self.__class__.alive = True

		self.customer_name_label = ttk.Label(self,text="Customer Name:*")
		self.customer_name_label.place(x=20,y=20)
		self.customer_name_entry = ttk.Entry(self)
		self.customer_name_entry.place(x=200,y=20)

		self.customer_address1_label = ttk.Label(self,text="Address 1:")
		self.customer_address1_label.place(x=20,y=60)
		self.customer_address1_entry = ttk.Entry(self)
		self.customer_address1_entry.place(x=200,y=60)

		self.customer_address2_label = ttk.Label(self,text="Address 2:")
		self.customer_address2_label.place(x=20,y=100)
		self.customer_address2_entry = ttk.Entry(self)
		self.customer_address2_entry.place(x=200,y=100)

		self.customer_city_label = ttk.Label(self,text="City:")
		self.customer_city_label.place(x=20,y=140)
		self.customer_city_entry = ttk.Entry(self)
		self.customer_city_entry.place(x=200,y=140)

		self.customer_state_label = ttk.Label(self,text="State/Province/Territory:")
		self.customer_state_label.place(x=20,y=180)
		self.customer_state_entry = ttk.Entry(self)
		self.customer_state_entry.place(x=200,y=180)

		self.customer_zip_postal_code_label = ttk.Label(self,text="ZIP Code/Postal Code:")
		self.customer_zip_postal_code_label.place(x=20,y=220)
		self.customer_zip_postal_code_entry = ttk.Entry(self)
		self.customer_zip_postal_code_entry.place(x=200,y=220)

		self.customer_country_label = ttk.Label(self,text="Country:")
		self.customer_country_label.place(x=20,y=260)
		self.customer_country_entry = ttk.Entry(self)
		self.customer_country_entry.place(x=200,y=260)

		self.customer_contact_name_label = ttk.Label(self,text="Customer Contact Name:")
		self.customer_contact_name_label.place(x=20,y=300)
		self.customer_contact_name_entry = ttk.Entry(self)
		self.customer_contact_name_entry.place(x=200,y=300)

		self.customer_contact_phone_label = ttk.Label(self,text="Customer Contact Phone:")
		self.customer_contact_phone_label.place(x=20,y=340)
		self.customer_contact_phone_entry = ttk.Entry(self)
		self.customer_contact_phone_entry.place(x=200,y=340)

		self.customer_contact_email_label = ttk.Label(self,text="Customer Contact Email:")
		self.customer_contact_email_label.place(x=20,y=380)
		self.customer_contact_email_entry = ttk.Entry(self)
		self.customer_contact_email_entry.place(x=200,y=380)

		self.customer_contact_notes_label = ttk.Label(self,text="Customer Contact Notes:")
		self.customer_contact_notes_label.place(x=20,y=420)
		self.customer_contact_notes_entry = ttk.Entry(self)
		self.customer_contact_notes_entry.place(x=200,y=420)

		self.get_customer_data_entries_button = ttk.Button(self,text="Create New Customer",command=self.create_new_customer)
		self.get_customer_data_entries_button.place(x=200,y=475)

		self.clear_entries_button = ttk.Button(self,text="Clear Data Entries",command=self.clear_customer_data)
		self.clear_entries_button.place(x=20,y=475)


	def create_new_customer(self):

		try:

			new_customer_data = []

			new_customer_name = self.customer_name_entry.get()
			new_customer_address1 = self.customer_address1_entry.get()
			new_customer_address2 = self.customer_address2_entry.get()
			new_customer_city = self.customer_city_entry.get()
			new_customer_state = self.customer_state_entry.get()
			new_customer_zip = self.customer_zip_postal_code_entry.get()
			new_customer_country = self.customer_country_entry.get()
			new_customer_contact_name = self.customer_contact_name_entry.get()
			new_customer_contact_phone = self.customer_contact_phone_entry.get()
			new_customer_contact_email = self.customer_contact_email_entry.get()
			new_customer_contact_notes = self.customer_contact_notes_entry.get()
			new_customer_stripe_id = None

			customer_names = []

			verify_customer_names_sql_script = '''SELECT CUSTOMER_NAME FROM customers;'''

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(verify_customer_names_sql_script)

				for item in cursor:

					customer_names.append(*item)

				connection.commit()

				cursor.close()

			if new_customer_name in customer_names:

				duplicate_customer_name_error_message_1 = tk.messagebox.showinfo(title="Add New Customer",message="Duplicate customer name:  please use a different name for new customer.")

			elif new_customer_name == "":

				new_customer_name_error_message_1 = tk.messagebox.showinfo(title="Add New Customer",message="Customer name cannot be blank.")

			else:

				new_customer_data.append(new_customer_name)
				new_customer_data.append(new_customer_address1)
				new_customer_data.append(new_customer_address2)
				new_customer_data.append(new_customer_city)
				new_customer_data.append(new_customer_state)
				new_customer_data.append(new_customer_zip)
				new_customer_data.append(new_customer_country)
				new_customer_data.append(new_customer_contact_name)
				new_customer_data.append(new_customer_contact_phone)
				new_customer_data.append(new_customer_contact_email)
				new_customer_data.append(new_customer_contact_notes)
				new_customer_data.append(new_customer_stripe_id)

				new_customer = NEW_CUSTOMER_ENTRY(new_customer_data)

				new_customer.enter_data()

				new_customer.stripe_entry(new_customer_name)

				customer_names.clear()

				new_customer_confirmation_message = tk.messagebox.showinfo(title="Add New Customer",message="New customer successfully created.")

		except Exception as error:

			error_message = tk.messagebox.showinfo(title="Add New Customer",message=f"{error}")


	def clear_customer_data(self):

		try:

			self.customer_name_entry.delete(0,tk.END)
			self.customer_address1_entry.delete(0,tk.END)
			self.customer_address2_entry.delete(0,tk.END)
			self.customer_city_entry.delete(0,tk.END)
			self.customer_state_entry.delete(0,tk.END)
			self.customer_zip_postal_code_entry.delete(0,tk.END)
			self.customer_country_entry.delete(0,tk.END)
			self.customer_contact_name_entry.delete(0,tk.END)
			self.customer_contact_phone_entry.delete(0,tk.END)
			self.customer_contact_email_entry.delete(0,tk.END)
			self.customer_contact_notes_entry.delete(0,tk.END)

		except Exception as error:

			clear_customer_data_error_message = tk.messagebox.showinfo(title="Add New Customer",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
