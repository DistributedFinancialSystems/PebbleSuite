import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class EDIT_CLIENT_WINDOW(tk.Toplevel):

	"""
	_______________________________________
	Define class variables and SQL scripts:
	_______________________________________
	"""
	client_sql_script = '''SELECT CLIENT_NAME FROM clients;'''

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
		self.title("Edit Client")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True
		"""
		_____________________________________________________________
		Retrieve client names from SQL.db, enter into listbox widget:
		_____________________________________________________________
		"""
		self.client_name_label = ttk.Label(self,text="Clients:")
		self.client_name_label.place(x=20,y=20)

		self.sort_clients_button = ttk.Button(self,text="Sort Clients A-Z",command=self.sort_clients)
		self.sort_clients_button.place(x=120,y=20)

		self.client_scrollbar = ttk.Scrollbar(self)
		self.client_scrollbar.place(x=240,y=60,width=20,height=380)
		self.client_listbox = tk.Listbox(self,yscrollcommand=self.client_scrollbar.set)
		self.client_listbox.place(x=20,y=60, width=220,height=380)
		self.client_scrollbar.config(command=self.client_listbox.yview)

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.client_sql_script)

			for item in cursor:

				self.client_listbox.insert(0," ".join(item))

			connection.commit()

			cursor.close()

		self.search_client_data_button = ttk.Button(self,text="Reterieve Client Data",command=self.search_client_data)
		self.search_client_data_button.place(x=20,y=460)

		self.client_name_label = ttk.Label(self,text="Client Name:")
		self.client_name_label.place(x=300,y=20)
		self.client_name = tk.StringVar()
		self.client_name_entry = ttk.Entry(self,textvariable=self.client_name,state=tk.DISABLED)
		self.client_name_entry.place(x=500,y=20)

		self.client_address1_label = ttk.Label(self,text="Address 1:")
		self.client_address1_label.place(x=300,y=60)
		self.client_address1_entry_text = tk.StringVar()
		self.client_address1_entry = ttk.Entry(self,textvariable=self.client_address1_entry_text)
		self.client_address1_entry.place(x=500,y=60)

		self.client_address2_label = tk.Label(self,text="Address 2:")
		self.client_address2_label.place(x=300,y=100)
		self.client_address2_entry_text = tk.StringVar()
		self.client_address2_entry = ttk.Entry(self,textvariable=self.client_address2_entry_text)
		self.client_address2_entry.place(x=500,y=100)

		self.client_city_label = ttk.Label(self,text="City:")
		self.client_city_label.place(x=300,y=140)
		self.client_city_entry_text = tk.StringVar()
		self.client_city_entry = tk.Entry(self,textvariable=self.client_city_entry_text)
		self.client_city_entry.place(x=500,y=140)

		self.client_state_label = ttk.Label(self,text="State/Province/Territory:")
		self.client_state_label.place(x=300,y=180)
		self.client_state_entry_text = tk.StringVar()
		self.client_state_entry = ttk.Entry(self,textvariable=self.client_state_entry_text)
		self.client_state_entry.place(x=500,y=180)

		self.client_zip_postal_code_label = ttk.Label(self,text="ZIP Code/Postal Code:")
		self.client_zip_postal_code_label.place(x=300,y=220)
		self.client_zip_postal_code_entry_text = tk.StringVar()
		self.client_zip_postal_code_entry = ttk.Entry(self,textvariable=self.client_zip_postal_code_entry_text)
		self.client_zip_postal_code_entry.place(x=500,y=220)

		self.client_country_label = ttk.Label(self,text="Country:")
		self.client_country_label.place(x=300,y=260)
		self.client_country_entry_text = tk.StringVar()
		self.client_country_entry = tk.Entry(self,textvariable=self.client_country_entry_text)
		self.client_country_entry.place(x=500,y=260)

		self.client_contact_name_label = ttk.Label(self,text="Client Contact Name:")
		self.client_contact_name_label.place(x=300,y=300)
		self.client_contact_name_entry_text = tk.StringVar()
		self.client_contact_name_entry = ttk.Entry(self,textvariable=self.client_contact_name_entry_text)
		self.client_contact_name_entry.place(x=500,y=300)

		self.client_contact_phone_label = ttk.Label(self,text="Client Contact Phone:")
		self.client_contact_phone_label.place(x=300,y=340)
		self.client_contact_phone_entry_text = tk.StringVar()
		self.client_contact_phone_entry = ttk.Entry(self,textvariable=self.client_contact_phone_entry_text)
		self.client_contact_phone_entry.place(x=500,y=340)

		self.client_contact_email_label = ttk.Label(self,text="Client Contact Email:")
		self.client_contact_email_label.place(x=300,y=380)
		self.client_contact_email_entry_text = tk.StringVar()
		self.client_contact_email_entry = ttk.Entry(self,textvariable=self.client_contact_email_entry_text)
		self.client_contact_email_entry.place(x=500,y=380)

		self.client_contact_notes_label = ttk.Label(self,text="Client Contact Notes:")
		self.client_contact_notes_label.place(x=300,y=420)
		self.client_contact_notes_entry_text = tk.StringVar()
		self.client_contact_notes_entry = ttk.Entry(self,textvariable=self.client_contact_notes_entry_text)
		self.client_contact_notes_entry.place(x=500,y=420)

		self.search_client_data_button = ttk.Button(self,text="Clear Data Entries",command=self.clear_data_entries)
		self.search_client_data_button.place(x=300,y=460)

		self.change_client_data_button = ttk.Button(self,text="Submit Data Changes",command=self.change_client_data)
		self.change_client_data_button.place(x=500,y=460)


	def sort_clients(self):

		try:

			pass

		except Exception as error:

			sort_clients_error_message_1 = tk.messagebox.showinfo(title="Edit Client",message=f"{error}")


	def search_client_data(self):

		try:

			collect = []

			search_clients_sql_script = '''SELECT * FROM clients WHERE CLIENT_NAME=?'''

			for item in self.client_listbox.curselection():

				select_vendor = self.client_listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(search_clients_sql_script,[select_vendor])

				for item in cursor:

					collect.append(item)

				self.client_name.set(f"{collect[0][0]}")
				self.client_address1_entry_text.set(f"{collect[0][1]}")
				self.client_address2_entry_text.set(f"{collect[0][2]}")
				self.client_city_entry_text.set(f"{collect[0][3]}")
				self.client_state_entry_text.set(f"{collect[0][4]}")
				self.client_zip_postal_code_entry_text.set(f"{collect[0][5]}")
				self.client_country_entry_text.set(f"{collect[0][6]}")
				self.client_contact_name_entry_text.set(f"{collect[0][7]}")
				self.client_contact_phone_entry_text.set(f"{collect[0][8]}")
				self.client_contact_email_entry_text.set(f"{collect[0][9]}")
				self.client_contact_notes_entry_text.set(f"{collect[0][10]}")

				connection.commit()

				cursor.close()

		except Exception as error:

			search_client_data_error_message_1 = tk.messagebox.showinfo(title="Edit Client",message=f"{error}")

	def clear_data_entries(self):

		try:

			self.client_name.set("")
			self.client_address1_entry_text.set("")
			self.client_address2_entry_text.set("")
			self.client_city_entry_text.set("")
			self.client_state_entry_text.set("")
			self.client_zip_postal_code_entry_text.set("")
			self.client_country_entry_text.set("")
			self.client_contact_name_entry_text.set("")
			self.client_contact_phone_entry_text.set("")
			self.client_contact_email_entry_text.set("")
			self.client_contact_notes_entry_text.set("")

		except Exception as error:

			clear_data_entries_error_message_1 = tk.messagebox.showinfo(title="Edit Client",message=f"{error}")


	def change_client_data(self):

		try:

			retrieve_clients_sql_script = '''SELECT * FROM clients;'''
			edit_client_address1_sql_script = '''UPDATE clients SET CLIENT_ADDRESS1=? WHERE CLIENT_NAME=?;'''
			edit_client_address2_sql_script = '''UPDATE clients SET CLIENT_ADDRESS2=? WHERE CLIENT_NAME=?;'''
			edit_client_city_sql_script = '''UPDATE clients SET CLIENT_CITY=? WHERE CLIENT_NAME=?;'''
			edit_client_state_sql_script = '''UPDATE clients SET CLIENT_STATE=? WHERE CLIENT_NAME=?;'''
			edit_client_zip_sql_script = '''UPDATE clients SET CLIENT_ZIP=? WHERE CLIENT_NAME=?;'''
			edit_client_country_sql_script = '''UPDATE clients SET CLIENT_COUNTRY=? WHERE CLIENT_NAME=?;'''
			edit_contact_name_sql_script = '''UPDATE clients SET CONTACT_NAME=? WHERE CLIENT_NAME=?;'''
			edit_contact_phone_sql_script = '''UPDATE clients SET CONTACT_PHONE=? WHERE CLIENT_NAME=?;'''
			edit_contact_email_sql_script = '''UPDATE clients SET CONTACT_EMAIL=? WHERE CLIENT_NAME=?;'''
			edit_client_notes_sql_script = '''UPDATE clients SET CONTACT_NOTES=? WHERE CLIENT_NAME=?;'''

			search_client_name = self.client_name.get()
			new_address1 = self.client_address1_entry.get()
			new_address2 = self.client_address2_entry.get()
			new_city = self.client_city_entry.get()
			new_state = self.client_state_entry.get()
			new_zip = self.client_zip_postal_code_entry.get()
			new_country = self.client_country_entry.get()
			new_contact_name = self.client_contact_name_entry.get()
			new_contact_phone = self.client_contact_phone_entry.get()
			new_contact_email = self.client_contact_email_entry.get()
			new_client_notes = self.client_contact_notes_entry.get()

			if search_client_name == "Select Client":

				change_client_data_error_message_1 = tk.messagebox.showinfo(title="Edit Client",message="Select a client to edit.")

			elif search_client_name == "":

				change_client_data_error_message_2 = tk.messagebox.showinfo(title="Edit Client",message="Select a client to edit.")

			else:

				with sqlite3.connect("SQL.db") as connection:

					cursor = connection.cursor()

					cursor.execute(edit_client_address1_sql_script,(new_address1,search_client_name))
					cursor.execute(edit_client_address2_sql_script,(new_address2,search_client_name))
					cursor.execute(edit_client_city_sql_script,(new_city,search_client_name))
					cursor.execute(edit_client_state_sql_script,(new_state,search_client_name))
					cursor.execute(edit_client_zip_sql_script,(new_zip,search_client_name))
					cursor.execute(edit_client_country_sql_script,(new_country,search_client_name))
					cursor.execute(edit_contact_name_sql_script,(new_contact_name,search_client_name))
					cursor.execute(edit_contact_phone_sql_script,(new_contact_phone,search_client_name))
					cursor.execute(edit_contact_email_sql_script,(new_contact_email,search_client_name))
					cursor.execute(edit_client_notes_sql_script,(new_client_notes,search_client_name))

					connection.commit()

					cursor.close()

				edit_client_confirmation_message_1 = tk.messagebox.showinfo(title="Edit Client",message="Client details successfully changed.")

				self.client_name.set("")
				self.client_address1_entry_text.set("")
				self.client_address2_entry_text.set("")
				self.client_city_entry_text.set("")
				self.client_state_entry_text.set("")
				self.client_zip_postal_code_entry_text.set("")
				self.client_country_entry_text.set("")
				self.client_contact_name_entry_text.set("")
				self.client_contact_phone_entry_text.set("")
				self.client_contact_email_entry_text.set("")
				self.client_contact_notes_entry_text.set("")

		except Exception as error:

			edit_client_error_message_1 = tk.messagebox.showinfo(title="Edit Client",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
