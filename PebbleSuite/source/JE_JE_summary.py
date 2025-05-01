import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import pandas as pd
import time




class JE_SUMMARY_WINDOW(tk.Toplevel):

	alive = False

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.config(width=220,height=120)
		self.title("Journal Entry Summary")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.print_journal_entries_button = ttk.Button(self,text="Print Journal Entries",command=self.print_journal_entries)
		self.print_journal_entries_button.place(x=20,y=20)

		self.export_journal_entries_button = ttk.Button(self,text="Export Journal Entries",command=self.export_journal_entries)
		self.export_journal_entries_button.place(x=20,y=60)


	def print_journal_entries(self):

		print_journal_entries_sql_script = '''SELECT * FROM journal_entries;'''

		try:
			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(print_journal_entries_sql_script)

				for item in cursor:

					print(item)

				connection.commit()

				cursor.close()

		except Exception as error:

			print_journal_entries_error_message_1 = tk.messagebox.showinfo(title="Vendor Summary",message=f"{error}")


	def export_journal_entries(self):

		retrieve_journal_entries_sql_script = '''SELECT * FROM journal_entries;'''

		try:
			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(retrieve_journal_entries_sql_script)

				rows = cursor.fetchall()

				df = pd.DataFrame(rows,columns=[column[0] for column in cursor.description])

				df.to_csv(f'{time.time()}_export_journal_entries.csv',index=False)

				connection.commit()

				cursor.close()

			export_journal_entries_confirmation_message_1 = tk.messagebox.showinfo(title="Journal Entry Summary",message="Journal Entry data successfully exported.")

		except Exception as error:

			export_journal_entries_error_message_1 = tk.messagebox.showinfo(title="Journal Entry Summary",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
