#Python Standard Library dependencies
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class NEW_CLIENT_ENTRY:

	def __init__(self,new_client_entry):

		self.new_client_entry = new_client_entry

	def enter_data(self):

		new_client_sql_script = '''INSERT INTO clients(
					CLIENT_NAME,
					CLIENT_ADDRESS1,
					CLIENT_ADDRESS2,
					CLIENT_CITY,
					CLIENT_STATE,
					CLIENT_ZIP,
					CLIENT_COUNTRY,
					CONTACT_NAME,
					CONTACT_PHONE,
					CONTACT_EMAIL,
					CONTACT_NOTES)
					VALUES(?,?,?,?,?,?,?,?,?,?,?)'''

		with sqlite3.connect("SQL.db") as connection:

			try:
				cursor = connection.cursor()
				cursor.execute(new_client_sql_script,self.new_client_entry)
				connection.commit()
				cursor.close()
				new_client_confirmation_message = tk.messagebox.showinfo(title="Add New Client",message="New client successfully created.")

			except sqlite3.Error as error:
				new_client_error_message = tk.messagebox.showinfo(title="Add New Client",message=f"Error: {error}")



class NEW_CLIENT_WINDOW(tk.Toplevel):

	#Define class variables

	alive = False


	#Define class functions

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.config(width=390,height=520)
		self.title("Add New Client")
		self.focus()
		self.resizable,(0,0)
		self.__class__.alive = True

		self.client_name_label = ttk.Label(self,text="Client Name:*")
		self.client_name_label.place(x=20,y=20)
		self.client_name_entry = ttk.Entry(self)
		self.client_name_entry.place(x=200,y=20)

		self.client_address1_label = ttk.Label(self,text="Address 1:")
		self.client_address1_label.place(x=20,y=60)
		self.client_address1_entry = ttk.Entry(self)
		self.client_address1_entry.place(x=200,y=60)

		self.client_address2_label = ttk.Label(self,text="Address 2:")
		self.client_address2_label.place(x=20,y=100)
		self.client_address2_entry = ttk.Entry(self)
		self.client_address2_entry.place(x=200,y=100)

		self.client_city_label = ttk.Label(self,text="City:")
		self.client_city_label.place(x=20,y=140)
		self.client_city_entry = ttk.Entry(self)
		self.client_city_entry.place(x=200,y=140)

		self.client_state_label = ttk.Label(self,text="State/Province/Territory:")
		self.client_state_label.place(x=20,y=180)
		self.client_state_entry = ttk.Entry(self)
		self.client_state_entry.place(x=200,y=180)

		self.client_zip_postal_code_label = ttk.Label(self,text="ZIP Code/Postal Code:")
		self.client_zip_postal_code_label.place(x=20,y=220)
		self.client_zip_postal_code_entry = ttk.Entry(self)
		self.client_zip_postal_code_entry.place(x=200,y=220)

		self.client_country_label = ttk.Label(self,text="Country:")
		self.client_country_label.place(x=20,y=260)
		self.client_country_entry = ttk.Entry(self)
		self.client_country_entry.place(x=200,y=260)

		self.client_contact_name_label = ttk.Label(self,text="Client Contact Name:")
		self.client_contact_name_label.place(x=20,y=300)
		self.client_contact_name_entry = ttk.Entry(self)
		self.client_contact_name_entry.place(x=200,y=300)

		self.client_contact_phone_label = ttk.Label(self,text="Client Contact Phone:")
		self.client_contact_phone_label.place(x=20,y=340)
		self.client_contact_phone_entry = ttk.Entry(self)
		self.client_contact_phone_entry.place(x=200,y=340)

		self.client_contact_email_label = ttk.Label(self,text="Client Contact Email:")
		self.client_contact_email_label.place(x=20,y=380)
		self.client_contact_email_entry = ttk.Entry(self)
		self.client_contact_email_entry.place(x=200,y=380)

		self.client_contact_notes_label = ttk.Label(self,text="Client Contact Notes:")
		self.client_contact_notes_label.place(x=20,y=420)
		self.client_contact_notes_entry = ttk.Entry(self)
		self.client_contact_notes_entry.place(x=200,y=420)

		self.get_client_data_entries_button = ttk.Button(self,text="Create New Client",command=self.create_new_client)
		self.get_client_data_entries_button.place(x=200,y=475)

		self.clear_entries_button = ttk.Button(self,text="Clear Data Entries",command=self.clear_client_data)
		self.clear_entries_button.place(x=20,y=475)


	def create_new_client(self):

		#Define function variables:
		new_client_data = []

		new_client_name = self.client_name_entry.get()
		new_client_address1 = self.client_address1_entry.get()
		new_client_address2 = self.client_address2_entry.get()
		new_client_city = self.client_city_entry.get()
		new_client_state = self.client_state_entry.get()
		new_client_zip = self.client_zip_postal_code_entry.get()
		new_client_country = self.client_country_entry.get()
		new_client_contact_name = self.client_contact_name_entry.get()
		new_client_contact_phone = self.client_contact_phone_entry.get()
		new_client_contact_email = self.client_contact_email_entry.get()
		new_client_contact_notes = self.client_contact_notes_entry.get()


		#Define create_new_client error message:
		if new_client_name == "":

			new_client_name_error_message = tk.messagebox.showinfo(title="Error",message="Client name cannot be blank.")


		#Format SQL.db entry data:
		else:

			new_client_data.append(new_client_name)
			new_client_data.append(new_client_address1)
			new_client_data.append(new_client_address2)
			new_client_data.append(new_client_city)
			new_client_data.append(new_client_state)
			new_client_data.append(new_client_zip)
			new_client_data.append(new_client_country)
			new_client_data.append(new_client_contact_name)
			new_client_data.append(new_client_contact_phone)
			new_client_data.append(new_client_contact_email)
			new_client_data.append(new_client_contact_notes)

			try:

				new_client = NEW_CLIENT_ENTRY(new_client_data)
				new_client.enter_data()


			except sqlite3.Error as error:

				error_message = tk.messagebox.showinfo(title="Error Message",message=f"{error}")


	def clear_client_data(self):

		try:

			self.client_name_entry.delete(0,tk.END)
			self.client_address1_entry.delete(0,tk.END)
			self.client_address2_entry.delete(0,tk.END)
			self.client_city_entry.delete(0,tk.END)
			self.client_state_entry.delete(0,tk.END)
			self.client_zip_postal_code_entry.delete(0,tk.END)
			self.client_country_entry.delete(0,tk.END)
			self.client_contact_name_entry.delete(0,tk.END)
			self.client_contact_phone_entry.delete(0,tk.END)
			self.client_contact_email_entry.delete(0,tk.END)
			self.client_contact_notes_entry.delete(0,tk.END)

		except ValueError as error:

			clear_client_data_error_message = tk.messagebox.showinfo(f"{error}")


	def destroy(self):

		self.__class__.alive = False
		return super().destroy()
