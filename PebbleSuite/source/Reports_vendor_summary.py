import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import pandas as pd
import time
import os




class VENDOR_SUMMARY_WINDOW(tk.Toplevel):

	alive = False

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

		print_vendors_sql_script = '''SELECT * FROM vendors;'''

		try:
			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(print_vendors_sql_script)

				for item in cursor:

					print(item)

				connection.commit()

				cursor.close()

		except Exception as error:

			print_vendors_error_message_1 = tk.messagebox.showinfo(title="Vendor Summary",message=f"{error}")


	def export_vendors(self):

		retrieve_vendors_sql_script = '''SELECT * FROM vendors;'''

		retrieve_working_directory = '''SELECT WORKING_DIRECTORY FROM working_directory;'''

		retrieve_permanent_directory = '''SELECT PERMANENT_DIRECTORY FROM permanent_directory;'''

		directory = []

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor_1 = connection.cursor()

				cursor_1.execute(retrieve_vendors_sql_script)

				rows = cursor_1.fetchall()

				df = pd.DataFrame(rows,columns=[column[0] for column in cursor_1.description])

				connection.commit()

				cursor_1.close()

				cursor_2 = connection.cursor()

				cursor_2.execute(retrieve_working_directory)

				for item in cursor_2:

					directory.append(*item)

				connection.commit()

				cursor_2.close()

				os.chdir(f"{directory[0]}")

				df.to_csv(f'{time.time()}_export_vendors.csv',index=False)

				directory.clear()

				cursor_3 = connection.cursor()

				cursor_3.execute(retrieve_permanent_directory)

				for item in cursor_3:

					directory.append(*item)

				os.chdir(f"{directory[0]}")

				directory.clear()

				connection.commit()

				cursor_3.close()

			export_vendors_confirmation_message_1 = tk.messagebox.showinfo(title="Vendor Summary",message="Vendor data successfully exported.")

		except Exception as error:

			export_vendors_error_message_1 = tk.messagebox.showinfo(title="Vendor Summary",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
