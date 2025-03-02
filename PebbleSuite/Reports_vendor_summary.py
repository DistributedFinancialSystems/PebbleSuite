#Python Standard Library dependencies
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class VENDOR_SUMMARY_WINDOW(tk.Toplevel):

	#Define class variables:
	alive = False


	#Define VENDOR_SUMMARY tkinter widgets:
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.config(width=220,height=120)
		self.title("Vendor Summary")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.print_vendors_button = ttk.Button(self,text="Print Vendors",command=self.print_vendors)
		self.print_vendors_button.place(x=20,y=20)

		self.export_vendors_button = ttk.Button(self,text="Export Vendors",command=self.export_vendors)
		self.export_vendors_button.place(x=20,y=60)


	def print_vendors(self):

		#Define SQL database scripts:
		print_vendors_sql_script = '''SELECT * FROM vendors;'''


		#Initialize SQL database connection:
		try:
			with sqlite3.connect("SQL.db") as connection:
				cursor = connection.cursor()
				cursor.execute(print_vendors_sql_script)

				for item in cursor:
					print(item)

				connection.commit()
				cursor.close()

		except sqlite3.Error as error:

			print_vendors_error_message = tk.messagebox.showinfo(title="Error Message",message=f"{error}")

	def export_vendors(self):

		#Define SQL.db scripts:

		#Initialize SQL.db connection:

		try:
			pass

		except sqlite3.Error as error:

			export_vendors_error_message = tk.messagebox.showinfo(title="Export Vendors",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False
		return super().destroy()
