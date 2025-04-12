#Python Standard Library dependencies
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class EDIT_CUSTOMER_WINDOW(tk.Toplevel):

	customer_sql_script = '''SELECT CUSTOMER_NAME FROM customers;'''

	alive = False

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
		self.config(width=390,height=520)
		self.title("Edit Customer")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.customer_name_label = ttk.Label(self,text="Customer Name")
		self.customer_name_label.place(x=20,y=20)
		self.customer_option_menu = ttk.OptionMenu(self,self.clicked,options[0],*options)
		self.customer_option_menu.place(x=200,y=20)

		self.customer_address1_label = ttk.Label(self,text="Address 1:")
		self.customer_address1_label.place(x=20,y=60)
		self.customer_address1_entry_text = tk.StringVar()
		self.customer_address1_entry = ttk.Entry(self,textvariable=self.customer_address1_entry_text)
		self.customer_address1_entry.place(x=200,y=60)

		self.customer_address2_label = tk.Label(self,text="Address 2:")
		self.customer_address2_label.place(x=20,y=100)
		self.customer_address2_entry_text = tk.StringVar()
		self.customer_address2_entry = ttk.Entry(self,textvariable=self.customer_address2_entry_text)
		self.customer_address2_entry.place(x=200,y=100)

		self.customer_city_label = ttk.Label(self,text="City:")
		self.customer_city_label.place(x=20,y=140)
		self.customer_city_entry_text = tk.StringVar()
		self.customer_city_entry = tk.Entry(self,textvariable=self.customer_city_entry_text)
		self.customer_city_entry.place(x=200,y=140)

		self.customer_state_label = ttk.Label(self,text="State/Province/Territory:")
		self.customer_state_label.place(x=20,y=180)
		self.customer_state_entry_text = tk.StringVar()
		self.customer_state_entry = ttk.Entry(self,textvariable=self.customer_state_entry_text)
		self.customer_state_entry.place(x=200,y=180)

		self.customer_zip_postal_code_label = ttk.Label(self,text="ZIP Code/Postal Code:")
		self.customer_zip_postal_code_label.place(x=20,y=220)
		self.customer_zip_postal_code_entry_text = tk.StringVar()
		self.customer_zip_postal_code_entry = ttk.Entry(self,textvariable=self.customer_zip_postal_code_entry_text)
		self.customer_zip_postal_code_entry.place(x=200,y=220)

		self.customer_country_label = ttk.Label(self,text="Country:")
		self.customer_country_label.place(x=20,y=260)
		self.customer_country_entry_text = tk.StringVar()
		self.customer_country_entry = tk.Entry(self,textvariable=self.customer_country_entry_text)
		self.customer_country_entry.place(x=200,y=260)

		self.customer_contact_name_label = ttk.Label(self,text="customer Contact Name:")
		self.customer_contact_name_label.place(x=20,y=300)
		self.customer_contact_name_entry_text = tk.StringVar()
		self.customer_contact_name_entry = ttk.Entry(self,textvariable=self.customer_contact_name_entry_text)
		self.customer_contact_name_entry.place(x=200,y=300)

		self.customer_contact_phone_label = ttk.Label(self,text="Customer Contact Phone:")
		self.customer_contact_phone_label.place(x=20,y=340)
		self.customer_contact_phone_entry_text = tk.StringVar()
		self.customer_contact_phone_entry = ttk.Entry(self,textvariable=self.customer_contact_phone_entry_text)
		self.customer_contact_phone_entry.place(x=200,y=340)

		self.customer_contact_email_label = ttk.Label(self,text="Customer Contact Email:")
		self.customer_contact_email_label.place(x=20,y=380)
		self.customer_contact_email_entry_text = tk.StringVar()
		self.customer_contact_email_entry = ttk.Entry(self,textvariable=self.customer_contact_email_entry_text)
		self.customer_contact_email_entry.place(x=200,y=380)

		self.customer_contact_notes_label = ttk.Label(self,text="Customer Contact Notes:")
		self.customer_contact_notes_label.place(x=20,y=420)
		self.customer_contact_notes_entry_text = tk.StringVar()
		self.customer_contact_notes_entry = ttk.Entry(self,textvariable=self.customer_contact_notes_entry_text)
		self.customer_contact_notes_entry.place(x=200,y=420)

		self.search_customer_data_button = ttk.Button(self,text="Retrieve Customer Data",command=self.search_customer_data)
		self.search_customer_data_button.place(x=20,y=460)

		self.change_customer_data_button = ttk.Button(self,text="Submit Data Changes",command=self.change_customer_data)
		self.change_customer_data_button.place(x=200,y=460)


	def search_customer_data(self):

		search_customers_sql_script = '''SELECT * FROM customers WHERE CUSTOMER_NAME=?'''

		search_customer_name = self.clicked.get()

		collect = []

		try:

			if search_customer_name == "Select Customer":

				search_customer_data_error_message = tk.messagebox.showinfo(title="Edit Customer",message="Select a customer to edit.")

			else:

				with sqlite3.connect("SQL.db") as connection:

					cursor = connection.cursor()

					cursor.execute(search_customers_sql_script,[search_customer_name])

					for item in cursor:

						collect.append(item)

					connection.commit()

					cursor.close()

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

		except Exception as error:

			search_customer_data_error_message_1 = tk.messagebox.showinfo(title="Edit Customer",message=f"{error}")


	def change_customer_data(self):

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

		search_customer_name = self.clicked.get()
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

		try:

			if search_customer_name == "Select Customer":

				edit_customer_error_message_1 = tk.messagebox.showinfo(title="Edit Customer",message="Select a customer to edit.")

			else:

				with sqlite3.connect("SQL.db") as connection:

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

					connection.commit()

					cursor.close()

				edit_customer_confirmation_message_1 = tk.messagebox.showinfo(title="Edit Customer",message="Customer details successfully changed.")

		except Exception as error:

			edit_customer_error_message_1 = tk.messagebox.showinfo(title="Edit Customer",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
