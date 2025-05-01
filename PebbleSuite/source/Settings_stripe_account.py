import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import stripe


class STRIPE_ACCOUNT_WINDOW(tk.Toplevel):

	alive = False

	def __init__(self,*args,**kwargs):

		super().__init__(*args,**kwargs)
		self.config(width=400,height=140)
		self.title("Stripe Account Settings")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.stripe_api_key_label = ttk.Label(self,text="Stripe API Key:")
		self.stripe_api_key_label.place(x=20,y=20)

		self.stripe_api_key_entry_text = tk.StringVar()
		self.stripe_api_key_entry = ttk.Entry(self,textvariable=self.stripe_api_key_entry_text)
		self.stripe_api_key_entry.place(x=20,y=60)

		self.stripe_api_key_button = ttk.Button(self,text="Update Stripe API Key",command=self.enter_api_key)
		self.stripe_api_key_button.place(x=20,y=100)

	def enter_api_key(self):

		try:

			stripe_api_key_sql_script = '''UPDATE stripe_api_key SET STRIPE_API_KEY=?;'''

			new_api_key = self.stripe_api_key_entry.get()

			if new_api_key == "":

				new_api_key_error_message_1 = tk.messagebox.showinfo(title="Stripe Account Settings",message="Stripe API key cannot be blank.")

			else:

				with sqlite3.connect("SQL.db") as connection:

					cursor = connection.cursor()

					cursor.execute(stripe_api_key_sql_script,[new_api_key])

					connection.commit()

					cursor.close()

				enter_api_key_confirmation_message_1 = tk.messagebox.showinfo(title="Stripe Account Settings",message="Stripe API key successfully updated.")


		except Exception as error:

			enter_api_key_error_message_1 = tk.messagebox.showinfo(title="Stripe Account Settings",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
