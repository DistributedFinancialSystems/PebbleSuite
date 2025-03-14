"""
[ ]
[ ]
[ ]
[ ]	AR_print_credit_memo.py
[ ]
[ ]
[ ]
"""
"""
[ ]
[ ]
[ ]
[ ]	IMPORT PYTHON MODULES:
[ ]
[ ]
[ ]
"""

import datetime
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class AR_PRINT_CREDIT_MEMO_WINDOW(tk.Toplevel):

	#Define class variables:
	alive = False

	#Define __init__ tkinter widgets:
	def __init__(self,*args,**kwargs):

		#Define class tkinter widgets:
		super().__init__(*args,**kwargs)
		self.config(height=100,width=170)
		self.title("New Credit Memo")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.credit_memo_report_button = ttk.Button(self,text="Print Credit Memos",command=self.credit_memo_report)
		self.credit_memo_report_button.place(x=20,y=20)


	def credit_memo_report(self):

		credit_memo_report_sql_script = '''SELECT * FROM client_credit_memos;'''

		try:
			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()
				cursor.execute(credit_memo_report_sql_script)

				for item in cursor:
					print(item)

				connection.commit()

				cursor.close()

		except sqlite3.Error as error:

			print(error)


	def destroy(self):
		self.__class__.alive = False
		return super().destroy()
