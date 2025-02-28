#Python Standard Library dependencies
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class VENDOR_SUMMARY(tk.Toplevel):

	#Define class variables:
	alive = False


	#Define VENDOR_SUMMARY tkinter widgets:
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.config(width=390,height=520)
		self.title("Vendor Summary")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True
		self.print_all_vendors_button = ttk.Button(self,text="Print All Vendors",command=self.print_all_vendors)
		self.print_all_vendors_button.place(x=200,y=480)


	def print_all_vendors(self):

		#Define SQL database scripts:
		print_all_vendors_sql_script = '''SELECT * FROM vendors;'''


		#Initialize SQL database connection:
		try:
			with sqlite3.connect("SQL.db") as connection:
				cursor = connection.cursor()
				cursor.execute(print_all_vendors_sql_script)

				for item in cursor:
					print(item)

				connection.commit()
				cursor.close()
				confirmation_message = tk.messagebox.showinfo(title="Print All Vendors",message="All Vendors Printed.")

		except sqlite3.Error as error:

			error_message = tk.messagebox.showinfo(title="Error Message",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False
		return super().destroy()
