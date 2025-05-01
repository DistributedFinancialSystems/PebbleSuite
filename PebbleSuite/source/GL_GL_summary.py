import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import pandas as pd
import time




class GL_SUMMARY_WINDOW(tk.Toplevel):

	alive = False

	def __init__(self,*args,**kwargs):

		super().__init__(*args,**kwargs)
		self.config(width=220,height=120)
		self.title("General Ledger Summary")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.print_general_ledger_button = ttk.Button(self,text="Print General Ledgers",command=self.print_general_ledgers)
		self.print_general_ledger_button.place(x=20,y=20)

		self.export_general_ledgers_button = ttk.Button(self,text="Export General Ledgers",command=self.export_general_ledgers)
		self.export_general_ledgers_button.place(x=20,y=60)


	def print_general_ledgers(self):

		print_general_ledgers_sql_script = '''SELECT * FROM general_ledgers;'''

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(print_general_ledgers_sql_script)

				for item in cursor:

					print(item)

				connection.commit()

				cursor.close()

		except Exception as error:

			print_general_ledgers_error_message_1 = tk.messagebox.showinfo(title="General Ledger Summary",message=f"{error}")


	def export_general_ledgers(self):

		retrieve_general_ledgers_sql_script = '''SELECT * FROM general_ledgers;'''

		try:

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(retrieve_general_ledgers_sql_script)

				rows = cursor.fetchall()

				df = pd.DataFrame(rows,columns=[column[0] for column in cursor.description])

				df.to_csv(f"{time.time()}_export_general_ledgers.csv",index=False)

				connection.commit()

				cursor.close()

			export_general_ledgers_confirmation_message_1 = tk.messagebox.showinfo(title="General Ledger Summary",message="General Ledger data successfully exported.")

		except Exception as error:

			export_general_ledgers_error_message_1 = tk.messagebox.showinfo(title="General Ledger Summary",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
