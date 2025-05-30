import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class EDIT_VENDOR_WINDOW(tk.Toplevel):

	"""
	_______________________________________
	Define class variables and SQL scripts:
	_______________________________________
	"""
	vendor_sql_script = '''SELECT VENDOR_NAME FROM vendors;'''

	alive = False
	"""
	___________________________________
	Retrieve customer data from SQL.db:
	___________________________________
	"""

	def __init__(self,*args,**kwargs):
		"""
		_______________________
		Define Tkinter widgets:
		_______________________
		"""
		super().__init__(*args,**kwargs)
		self.config(width=700,height=505)
		self.title("Edit Vendor")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True
		"""
		_____________________________________________________________
		Retrieve vendor names from SQL.db, enter into listbox widget:
		_____________________________________________________________
		"""
		self.vendor_name_label = ttk.Label(self,text="Vendors:")
		self.vendor_name_label.place(x=20,y=20)

		self.sort_vendors_button = ttk.Button(self,text="Sort Vendors A-Z",command=self.sort_vendors)
		self.sort_vendors_button.place(x=120,y=20)

		self.vendor_scrollbar = ttk.Scrollbar(self)
		self.vendor_scrollbar.place(x=240,y=60,width=20,height=380)
		self.vendor_listbox = tk.Listbox(self,yscrollcommand=self.vendor_scrollbar.set)
		self.vendor_listbox.place(x=20,y=60,width=220,height=380)
		self.vendor_scrollbar.config(command=self.vendor_listbox.yview)

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.vendor_sql_script)

			for item in cursor:

				self.vendor_listbox.insert(0," ".join(item))

			connection.commit()

			cursor.close()

		self.search_vendor_data_button = ttk.Button(self,text="Retrieve Vendor Data",command=self.search_vendor_data)
		self.search_vendor_data_button.place(x=20,y=460)

		self.vendor_name_label = ttk.Label(self,text="Vendor Name:")
		self.vendor_name_label.place(x=300,y=20)
		self.vendor_name = tk.StringVar()
		self.vendor_name_entry = ttk.Entry(self,textvariable=self.vendor_name,state=tk.DISABLED)
		self.vendor_name_entry.place(x=500,y=20)

		self.vendor_address1_label = ttk.Label(self,text="Address 1:")
		self.vendor_address1_label.place(x=300,y=60)
		self.vendor_address1_entry_text = tk.StringVar()
		self.vendor_address1_entry = ttk.Entry(self,textvariable=self.vendor_address1_entry_text)
		self.vendor_address1_entry.place(x=500,y=60)

		self.vendor_address2_label = ttk.Label(self,text="Address 2:")
		self.vendor_address2_label.place(x=300,y=100)
		self.vendor_address2_entry_text = tk.StringVar()
		self.vendor_address2_entry = ttk.Entry(self,textvariable=self.vendor_address2_entry_text)
		self.vendor_address2_entry.place(x=500,y=100)

		self.vendor_city_label = ttk.Label(self,text="City:")
		self.vendor_city_label.place(x=300,y=140)
		self.vendor_city_entry_text = tk.StringVar()
		self.vendor_city_entry = ttk.Entry(self,textvariable=self.vendor_city_entry_text)
		self.vendor_city_entry.place(x=500,y=140)

		self.vendor_state_label = ttk.Label(self,text="State/Province/Territory:")
		self.vendor_state_label.place(x=300,y=180)
		self.vendor_state_entry_text = tk.StringVar()
		self.vendor_state_entry = ttk.Entry(self,textvariable=self.vendor_state_entry_text)
		self.vendor_state_entry.place(x=500,y=180)

		self.vendor_zip_postal_code_label = ttk.Label(self,text="ZIP Code/Postal Code:")
		self.vendor_zip_postal_code_label.place(x=300,y=220)
		self.vendor_zip_postal_code_entry_text = tk.StringVar()
		self.vendor_zip_postal_code_entry = ttk.Entry(self,textvariable=self.vendor_zip_postal_code_entry_text)
		self.vendor_zip_postal_code_entry.place(x=500,y=220)

		self.vendor_country_label = ttk.Label(self,text="Country:")
		self.vendor_country_label.place(x=300,y=260)
		self.vendor_country_entry_text = tk.StringVar()
		self.vendor_country_entry = ttk.Entry(self,textvariable=self.vendor_country_entry_text)
		self.vendor_country_entry.place(x=500,y=260)

		self.vendor_contact_name_label = ttk.Label(self,text="Vendor Contact Name:")
		self.vendor_contact_name_label.place(x=300,y=300)
		self.vendor_contact_name_entry_text = tk.StringVar()
		self.vendor_contact_name_entry = ttk.Entry(self,textvariable=self.vendor_contact_name_entry_text)
		self.vendor_contact_name_entry.place(x=500,y=300)

		self.vendor_contact_phone_label = ttk.Label(self,text="Vendor Contact Phone:")
		self.vendor_contact_phone_label.place(x=300,y=340)
		self.vendor_contact_phone_entry_text = tk.StringVar()
		self.vendor_contact_phone_entry = ttk.Entry(self,textvariable=self.vendor_contact_phone_entry_text)
		self.vendor_contact_phone_entry.place(x=500,y=340)

		self.vendor_contact_email_label = ttk.Label(self,text="Vendor Contact Email:")
		self.vendor_contact_email_label.place(x=300,y=380)
		self.vendor_contact_email_entry_text = tk.StringVar()
		self.vendor_contact_email_entry = ttk.Entry(self,textvariable=self.vendor_contact_email_entry_text)
		self.vendor_contact_email_entry.place(x=500,y=380)

		self.vendor_1099_label = ttk.Label(self,text="1099 Form Required?")
		self.vendor_1099_label.place(x=300,y=420)
		self.vendor_1099_entry_text = tk.StringVar()
		self.vendor_1099_entry = ttk.Entry(self,textvariable=self.vendor_1099_entry_text,state=tk.DISABLED)
		self.vendor_1099_entry.place(x=500,y=420)

		self.search_vendor_data_button = ttk.Button(self,text="Clear Data Entries",command=self.clear_data_entries)
		self.search_vendor_data_button.place(x=300,y=460)

		self.change_vendor_data_button = ttk.Button(self,text="Submit Data Changes",command=self.change_vendor_data)
		self.change_vendor_data_button.place(x=500,y=460)

	def sort_vendors(self):

		try:

			pass

		except Exception as error:

			sort_vendors_error_message_1 = tk.messagebox.showinfo(title="Edit Vendor",message=f"{error}")


	def search_vendor_data(self):

		try:

			collect = []

			search_vendors_sql_script = '''SELECT * FROM vendors WHERE VENDOR_NAME=?'''

			for item in self.vendor_listbox.curselection():

				select_vendor = self.vendor_listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(search_vendors_sql_script,[select_vendor])

				for item in cursor:

					collect.append(item)

				self.vendor_name.set(f"{collect[0][0]}")
				self.vendor_address1_entry_text.set(f"{collect[0][1]}")
				self.vendor_address2_entry_text.set(f"{collect[0][2]}")
				self.vendor_city_entry_text.set(f"{collect[0][3]}")
				self.vendor_state_entry_text.set(f"{collect[0][4]}")
				self.vendor_zip_postal_code_entry_text.set(f"{collect[0][5]}")
				self.vendor_country_entry_text.set(f"{collect[0][6]}")
				self.vendor_contact_name_entry_text.set(f"{collect[0][7]}")
				self.vendor_contact_phone_entry_text.set(f"{collect[0][8]}")
				self.vendor_contact_email_entry_text.set(f"{collect[0][9]}")
				self.vendor_1099_entry_text.set(f"{collect[0][10]}")

				connection.commit()

				cursor.close()

		except Exception as error:

			search_vendor_error_message_2 = tk.messagebox.showinfo(title="Edit Vendor",message=f"{error}")


	def clear_data_entries(self):

		try:

			self.vendor_name.set("")
			self.vendor_address1_entry_text.set("")
			self.vendor_address2_entry_text.set("")
			self.vendor_city_entry_text.set("")
			self.vendor_state_entry_text.set("")
			self.vendor_zip_postal_code_entry_text.set("")
			self.vendor_country_entry_text.set("")
			self.vendor_contact_name_entry_text.set("")
			self.vendor_contact_phone_entry_text.set("")
			self.vendor_contact_email_entry_text.set("")
			self.vendor_1099_entry_text.set("")

		except Exception as error:

			clear_data_entries_error_message_1 = tk.messagebox.showinfo(title="Edit Vendor",message=f"{error}")


	def change_vendor_data(self):

		try:

			retrieve_vendors_sql_script = '''SELECT * FROM vendors;'''
			edit_vendor_address1_sql_script = '''UPDATE vendors SET VENDOR_ADDRESS1=? WHERE VENDOR_NAME=?;'''
			edit_vendor_address2_sql_script = '''UPDATE vendors SET VENDOR_ADDRESS2=? WHERE VENDOR_NAME=?;'''
			edit_vendor_city_sql_script = '''UPDATE vendors SET VENDOR_CITY=? WHERE VENDOR_NAME=?;'''
			edit_vendor_state_sql_script = '''UPDATE vendors SET VENDOR_STATE=? WHERE VENDOR_NAME=?;'''
			edit_vendor_zip_sql_script = '''UPDATE vendors SET VENDOR_ZIP=? WHERE VENDOR_NAME=?;'''
			edit_vendor_country_sql_script = '''UPDATE vendors SET VENDOR_COUNTRY=? WHERE VENDOR_NAME=?;'''
			edit_contact_name_sql_script = '''UPDATE vendors SET CONTACT_NAME=? WHERE VENDOR_NAME=?;'''
			edit_contact_phone_sql_script = '''UPDATE vendors SET CONTACT_PHONE=? WHERE VENDOR_NAME=?;'''
			edit_contact_email_sql_script = '''UPDATE vendors SET CONTACT_EMAIL=? WHERE VENDOR_NAME=?;'''
			edit_vendor_1099_sql_script = '''UPDATE vendors SET VENDOR_1099=? WHERE VENDOR_NAME=?;'''

			search_vendor_JE_name = '''SELECT * FROM journal_entries WHERE JOURNAL_ENTRY_VENDOR_NAME=?;'''

			search_vendor_name = self.vendor_name.get()
			new_address1 = self.vendor_address1_entry.get()
			new_address2 = self.vendor_address2_entry.get()
			new_city = self.vendor_city_entry.get()
			new_state = self.vendor_state_entry.get()
			new_zip = self.vendor_zip_postal_code_entry.get()
			new_country = self.vendor_country_entry.get()
			new_contact_name = self.vendor_contact_name_entry.get()
			new_contact_phone = self.vendor_contact_phone_entry.get()
			new_contact_email = self.vendor_contact_email_entry.get()
			new_vendor_1099 = self.vendor_1099_entry.get()

			if search_vendor_name == "":

				edit_vendor_error_message_1 = tk.messagebox.showinfo(title="Edit Vendor",message="Select a vendor to edit.")

			else:

				with sqlite3.connect("SQL.db") as connection:

					cursor = connection.cursor()

					cursor.execute(edit_vendor_address1_sql_script,(new_address1,search_vendor_name))
					cursor.execute(edit_vendor_address2_sql_script,(new_address2,search_vendor_name))
					cursor.execute(edit_vendor_city_sql_script,(new_city,search_vendor_name))
					cursor.execute(edit_vendor_state_sql_script,(new_state,search_vendor_name))
					cursor.execute(edit_vendor_zip_sql_script,(new_zip,search_vendor_name))
					cursor.execute(edit_vendor_country_sql_script,(new_country,search_vendor_name))
					cursor.execute(edit_contact_name_sql_script,(new_contact_name,search_vendor_name))
					cursor.execute(edit_contact_phone_sql_script,(new_contact_phone,search_vendor_name))
					cursor.execute(edit_contact_email_sql_script,(new_contact_email,search_vendor_name))
					cursor.execute(edit_vendor_1099_sql_script,(new_vendor_1099,search_vendor_name))

					connection.commit()

					cursor.close()

				edit_vendor_confirmation_message_1 = tk.messagebox.showinfo(title="Edit Vendor",message="Vendor detail successfully changed.")

				self.vendor_name.set("")
				self.vendor_address1_entry_text.set("")
				self.vendor_address2_entry_text.set("")
				self.vendor_city_entry_text.set("")
				self.vendor_state_entry_text.set("")
				self.vendor_zip_postal_code_entry_text.set("")
				self.vendor_country_entry_text.set("")
				self.vendor_contact_name_entry_text.set("")
				self.vendor_contact_phone_entry_text.set("")
				self.vendor_contact_email_entry_text.set("")
				self.vendor_1099_entry_text.set("")

		except Exception as error:

			edit_vendor_error_message_2 = tk.messagebox.showinfo(title="Edit Vendor",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
