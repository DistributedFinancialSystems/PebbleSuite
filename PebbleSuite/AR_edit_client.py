#Python Standard Library dependencies
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class EDIT_CLIENT_WINDOW(tk.Toplevel):

	#Define SQL database scripts:
	client_sql_script = '''SELECT CLIENT_NAME FROM clients;'''

	#Define class variables
	alive = False

	#Define class functions
	def __init__(self,*args,**kwargs):

		client_data = []

		options = ["Select Client"]

		#Initialize SQL.db connection:
		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.client_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()

		#Define EDIT_CLIENT tkinter widgets:
		super().__init__(*args,**kwargs)
		self.config(width=390,height=520)
		self.title("Edit Client")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.client_name_label = ttk.Label(self,text="Client Name")
		self.client_name_label.place(x=20,y=20)
		self.client_option_menu = ttk.OptionMenu(self,self.clicked,options[0],*options)
		self.client_option_menu.place(x=200,y=20)

		self.client_address1_label = ttk.Label(self,text="Address 1:")
		self.client_address1_label.place(x=20,y=60)
		self.client_address1_entry_text = tk.StringVar()
		self.client_address1_entry = ttk.Entry(self,textvariable=self.client_address1_entry_text)
		self.client_address1_entry.place(x=200,y=60)

		self.client_address2_label = tk.Label(self,text="Address 2:")
		self.client_address2_label.place(x=20,y=100)
		self.client_address2_entry_text = tk.StringVar()
		self.client_address2_entry = ttk.Entry(self,textvariable=self.client_address2_entry_text)
		self.client_address2_entry.place(x=200,y=100)

		self.client_city_label = ttk.Label(self,text="City:")
		self.client_city_label.place(x=20,y=140)
		self.client_city_entry_text = tk.StringVar()
		self.client_city_entry = tk.Entry(self,textvariable=self.client_city_entry_text)
		self.client_city_entry.place(x=200,y=140)

		self.client_state_label = ttk.Label(self,text="State/Province/Territory:")
		self.client_state_label.place(x=20,y=180)
		self.client_state_entry_text = tk.StringVar()
		self.client_state_entry = ttk.Entry(self,textvariable=self.client_state_entry_text)
		self.client_state_entry.place(x=200,y=180)

		self.client_zip_postal_code_label = ttk.Label(self,text="ZIP Code/Postal Code:")
		self.client_zip_postal_code_label.place(x=20,y=220)
		self.client_zip_postal_code_entry_text = tk.StringVar()
		self.client_zip_postal_code_entry = ttk.Entry(self,textvariable=self.client_zip_postal_code_entry_text)
		self.client_zip_postal_code_entry.place(x=200,y=220)

		self.client_country_label = ttk.Label(self,text="Country:")
		self.client_country_label.place(x=20,y=260)
		self.client_country_entry_text = tk.StringVar()
		self.client_country_entry = tk.Entry(self,textvariable=self.client_country_entry_text)
		self.client_country_entry.place(x=200,y=260)

		self.client_contact_name_label = ttk.Label(self,text="Client Contact Name:")
		self.client_contact_name_label.place(x=20,y=300)
		self.client_contact_name_entry_text = tk.StringVar()
		self.client_contact_name_entry = ttk.Entry(self,textvariable=self.client_contact_name_entry_text)
		self.client_contact_name_entry.place(x=200,y=300)

		self.client_contact_phone_label = ttk.Label(self,text="Client Contact Phone:")
		self.client_contact_phone_label.place(x=20,y=340)
		self.client_contact_phone_entry_text = tk.StringVar()
		self.client_contact_phone_entry = ttk.Entry(self,textvariable=self.client_contact_phone_entry_text)
		self.client_contact_phone_entry.place(x=200,y=340)

		self.client_contact_email_label = ttk.Label(self,text="Client Contact Email:")
		self.client_contact_email_label.place(x=20,y=380)
		self.client_contact_email_entry_text = tk.StringVar()
		self.client_contact_email_entry = ttk.Entry(self,textvariable=self.client_contact_email_entry_text)
		self.client_contact_email_entry.place(x=200,y=380)

		self.client_contact_notes_label = ttk.Label(self,text="Client Contact Notes:")
		self.client_contact_notes_label.place(x=20,y=420)
		self.client_contact_notes_entry_text = tk.StringVar()
		self.client_contact_notes_entry = ttk.Entry(self,textvariable=self.client_contact_notes_entry_text)
		self.client_contact_notes_entry.place(x=200,y=420)

		self.search_client_data_button = ttk.Button(self,text="Retrieve Client Data",command=self.search_client_data)
		self.search_client_data_button.place(x=20,y=460)

		self.change_client_data_button = ttk.Button(self,text="Submit Data Changes",command=self.change_client_data)
		self.change_client_data_button.place(x=200,y=460)


	def search_client_data(self):

		#Define SQL.db scripts:
		search_clients_sql_script = '''SELECT * FROM clients WHERE CLIENT_NAME=?'''

		#Retrieve client name from data form:
		search_client_name = self.clicked.get()

		#Define search_client_data error message:
		if search_client_name == "Select Client":

			search_client_data_error_message = tk.messagebox.showinfo(title="Edit Client",message="Select a client to edit.")

		#Initialized SQL.db connection:
		else:

			with sqlite3.connect("SQL.db") as connection:

				collect = []

				cursor = connection.cursor()

				cursor.execute(search_clients_sql_script,[search_client_name])

				for item in cursor:

					collect.append(item)

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


	def change_client_data(self):

		#Define SQL.db database scripts:
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

		#Retrieve client data from entry form:
		search_client_name = self.clicked.get()
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

		#Define change_client_data error message:
		if search_client_name == "Select Client":

			change_client_data_error_message = tk.messagebox.showinfo(title="Edit Client",message="Select a client to edit.")

		#Initialize SQL.db connection:
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

			edit_client_confirmation_message = tk.messagebox.showinfo(title="Edit Client",message="Changes successfully entered")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
