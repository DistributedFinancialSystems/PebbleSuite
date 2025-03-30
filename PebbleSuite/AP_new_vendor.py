#Python Standard Library dependencies
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




"""
		NEW VENDOR SECTION.
"""




class NEW_VENDOR_ENTRY:


	def __init__(self,new_vendor_entry):

		self.new_vendor_entry = new_vendor_entry


	def enter_data(self):

		new_vendor_sql_script = '''INSERT INTO vendors(
					VENDOR_NAME,
					VENDOR_ADDRESS1,
					VENDOR_ADDRESS2,
					VENDOR_CITY,
					VENDOR_STATE,
					VENDOR_ZIP,
					VENDOR_COUNTRY,
					CONTACT_NAME,
					CONTACT_PHONE,
					CONTACT_EMAIL,
					VENDOR_1099)
					VALUES(?,?,?,?,?,?,?,?,?,?,?);'''

		with sqlite3.connect("SQL.db") as connection:

			try:
				cursor = connection.cursor()
				cursor.execute(new_vendor_sql_script,self.new_vendor_entry)
				connection.commit()
				cursor.close()

			except sqlite3.Error as error:
				error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")


class NEW_VENDOR_WINDOW(tk.Toplevel):

	alive = False

	vendor_1099_options = ["Select 1099 option","Select 1099 option","N/A","1099-MISC","1099-NEC"]


	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.config(width=390,height=520)
		self.title("Add New Vendor")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.vendor_name_label = ttk.Label(self,text="Vendor Name:*")
		self.vendor_name_label.place(x=20,y=20)
		self.vendor_name_entry = ttk.Entry(self)
		self.vendor_name_entry.place(x=200,y=20)

		self.vendor_address1_label = ttk.Label(self,text="Address 1:")
		self.vendor_address1_label.place(x=20,y=60)
		self.vendor_address1_entry = ttk.Entry(self)
		self.vendor_address1_entry.place(x=200,y=60)

		self.vendor_address2_label = ttk.Label(self,text="Address 2:")
		self.vendor_address2_label.place(x=20,y=100)
		self.vendor_address2_entry = ttk.Entry(self)
		self.vendor_address2_entry.place(x=200,y=100)

		self.vendor_city_label = ttk.Label(self,text="City:")
		self.vendor_city_label.place(x=20,y=140)
		self.vendor_city_entry = ttk.Entry(self)
		self.vendor_city_entry.place(x=200,y=140)

		self.vendor_state_label = ttk.Label(self,text="State/Province/Territory:")
		self.vendor_state_label.place(x=20,y=180)
		self.vendor_state_entry = ttk.Entry(self)
		self.vendor_state_entry.place(x=200,y=180)

		self.vendor_zip_postal_code_label = ttk.Label(self,text="ZIP Code/Postal Code:")
		self.vendor_zip_postal_code_label.place(x=20,y=220)
		self.vendor_zip_postal_code_entry = ttk.Entry(self)
		self.vendor_zip_postal_code_entry.place(x=200,y=220)

		self.vendor_country_label = ttk.Label(self,text="Country:")
		self.vendor_country_label.place(x=20,y=260)
		self.vendor_country_entry = ttk.Entry(self)
		self.vendor_country_entry.place(x=200,y=260)

		self.vendor_contact_name_label = ttk.Label(self,text="Vendor Contact Name:")
		self.vendor_contact_name_label.place(x=20,y=300)
		self.vendor_contact_name_entry = ttk.Entry(self)
		self.vendor_contact_name_entry.place(x=200,y=300)

		self.vendor_contact_phone_label = ttk.Label(self,text="Vendor Contact Phone:")
		self.vendor_contact_phone_label.place(x=20,y=340)
		self.vendor_contact_phone_entry = ttk.Entry(self)
		self.vendor_contact_phone_entry.place(x=200,y=340)

		self.vendor_contact_email_label = ttk.Label(self,text="Vendor Contact Email:")
		self.vendor_contact_email_label.place(x=20,y=380)
		self.vendor_contact_email_entry = ttk.Entry(self)
		self.vendor_contact_email_entry.place(x=200,y=380)

		self.vendor_1099_label = ttk.Label(self,text="1099 Form Required?*")
		self.vendor_1099_label.place(x=20,y=420)
		self.vendor_1099_entry_text = tk.StringVar()
		self.vendor_1099_entry_text.set(f"{self.vendor_1099_options[0]}")
		self.vendor_1099_option_menu = ttk.OptionMenu(self,self.vendor_1099_entry_text,*self.vendor_1099_options)
		self.vendor_1099_option_menu.place(x=200,y=420)

		self.get_vendor_data_entries_button = ttk.Button(self,text="Create New Vendor",command=self.create_new_vendor)
		self.get_vendor_data_entries_button.place(x=200,y=475)

		self.clear_entries_button = ttk.Button(self,text="Clear Data Entries",command=self.clear_vendor_data)
		self.clear_entries_button.place(x=20,y=475)


	def create_new_vendor(self):

		new_vendor_data = []

		new_vendor_name = self.vendor_name_entry.get()
		new_vendor_data.append(new_vendor_name)

		new_vendor_address1 = self.vendor_address1_entry.get()
		new_vendor_data.append(new_vendor_address1)

		new_vendor_address2 = self.vendor_address2_entry.get()
		new_vendor_data.append(new_vendor_address2)

		new_vendor_city = self.vendor_city_entry.get()
		new_vendor_data.append(new_vendor_city)

		new_vendor_state = self.vendor_state_entry.get()
		new_vendor_data.append(new_vendor_state)

		new_vendor_zip = self.vendor_zip_postal_code_entry.get()
		new_vendor_data.append(new_vendor_zip)

		new_vendor_country = self.vendor_country_entry.get()
		new_vendor_data.append(new_vendor_country)

		new_vendor_contact_name = self.vendor_contact_name_entry.get()
		new_vendor_data.append(new_vendor_contact_name)

		new_vendor_contact_phone = self.vendor_contact_phone_entry.get()
		new_vendor_data.append(new_vendor_contact_phone)

		new_vendor_contact_email = self.vendor_contact_email_entry.get()
		new_vendor_data.append(new_vendor_contact_email)

		new_vendor_1099 = self.vendor_1099_entry_text.get()
		new_vendor_data.append(new_vendor_1099)

		#Verify vendor names in SQL.db:

		vendor_names = []

		verify_vendor_names_sql_script = '''SELECT VENDOR_NAME FROM vendors;'''

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(verify_vendor_names_sql_script)

			for item in cursor:

				vendor_names.append(*item)

			connection.commit()

			cursor.close()


		if new_vendor_name in vendor_names:

			duplicate_vendor_names_error_message = tk.messagebox.showinfo(title="New Vendor",message="Duplicate vendor name:  please use different name for new vendor.")

		elif new_vendor_name == "":

			new_vendor_name_error_message = tk.messagebox.showinfo(title="Error",message="Vendor name cannot be blank.")

		elif new_vendor_1099 == "Select 1099 option":

			new_vendor_1099_error_message = tk.messagebox.showinfo(title="Error",message="Select vendor 1099 form option.")

		else:

			try:

				new_vendor = NEW_VENDOR_ENTRY(new_vendor_data)

				new_vendor.enter_data()

				vendor_names.clear()

				create_new_vendor_confirmation_message = tk.messagebox.showinfo(title="New Vendor Entry",message="New Vendor Successfully Created!")

			except sqlite3.Error as error:

				create_new_vendor_error_message = tk.messagebox.showinfo(title="Error",message=f"{error}")


	def clear_vendor_data(self):

		try:
			self.vendor_name_entry.delete(0,tk.END)
			self.vendor_address1_entry.delete(0,tk.END)
			self.vendor_address2_entry.delete(0,tk.END)
			self.vendor_city_entry.delete(0,tk.END)
			self.vendor_state_entry.delete(0,tk.END)
			self.vendor_zip_postal_code_entry.delete(0,tk.END)
			self.vendor_country_entry.delete(0,tk.END)
			self.vendor_contact_name_entry.delete(0,tk.END)
			self.vendor_contact_phone_entry.delete(0,tk.END)
			self.vendor_contact_email_entry.delete(0,tk.END)

			vendor_names.clear()

		except ValueError as error:

			clear_vendor_data_error_message = tk.messagebox.showinfo(f"{error}")


	def destroy(self):

		self.__class__.alive = False
		return super().destroy()
