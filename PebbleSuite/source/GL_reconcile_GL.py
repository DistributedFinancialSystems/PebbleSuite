import datetime
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo




class RECONCILE_GL_WINDOW(tk.Toplevel):

	alive = False

	delete_selection_temporary_memory = []

	general_ledger_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers;'''

	def __init__(self,*args,**kwargs):

		options = ["Select General Ledger"]

		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(self.general_ledger_sql_script)

			for item in cursor:

				options.append(" ".join(item))

			connection.commit()

			cursor.close()

		super().__init__(*args,**kwargs)
		self.config(width=800,height=775)
		self.title("Reconcile General Ledger")
		self.focus()
		self.resizable(0,0)
		self.__class__.alive = True

		self.clicked = tk.StringVar()
		self.clicked.set(f"{options[0]}")

		self.general_ledger_name_label = ttk.Label(self,text="General Ledger Name:")
		self.general_ledger_name_label.place(x=20,y=15)

		self.select_general_ledger_scrollbar = ttk.Scrollbar(self)
		self.select_general_ledger_scrollbar.place(x=353,y=45,width=20,height=170)
		self.select_general_ledger_listbox = tk.Listbox(self,yscrollcommand=self.select_general_ledger_scrollbar.set)
		self.select_general_ledger_listbox.place(x=20,y=45,width=333,height=170)
		self.select_general_ledger_scrollbar.config(command=self.select_general_ledger_listbox.yview)

		search_general_ledger_name_sql_script = '''SELECT GENERAL_LEDGER_NAME FROM general_ledgers;'''


		with sqlite3.connect("SQL.db") as connection:

			cursor = connection.cursor()

			cursor.execute(search_general_ledger_name_sql_script)

			connection.commit()

			for item in cursor:

				self.select_general_ledger_listbox.insert(0," ".join(item))

			cursor.close()


		self.select_general_ledger_button = ttk.Button(self,text="Select General Ledger",command=self.select_general_ledger)
		self.select_general_ledger_button.place(x=20,y=230)

		self.general_ledger_name_label = ttk.Label(self,text="General Ledger Name:")
		self.general_ledger_name_label.place(x=400,y=15)
		self.general_ledger_name_entry_text = tk.StringVar()
		self.general_ledger_name_entry = ttk.Entry(self,textvariable=self.general_ledger_name_entry_text,width=21,state=tk.DISABLED)
		self.general_ledger_name_entry.place(x=400,y=45)

		self.general_ledger_number_label = ttk.Label(self,text="General Ledger Number:")
		self.general_ledger_number_label.place(x=400,y=85)
		self.general_ledger_number_entry_text = tk.StringVar()
		self.general_ledger_number_entry = ttk.Entry(self,textvariable=self.general_ledger_number_entry_text,state=tk.DISABLED,width=21)
		self.general_ledger_number_entry.place(x=400,y=115)

		self.general_ledger_type_label = ttk.Label(self,text="General Ledger Type:")
		self.general_ledger_type_label.place(x=400,y=155)
		self.general_ledger_type_entry_text = tk.StringVar()
		self.general_ledger_type_entry = ttk.Entry(self,textvariable=self.general_ledger_type_entry_text,state=tk.DISABLED,width=21)
		self.general_ledger_type_entry.place(x=400,y=185)

		self.previous_general_ledger_reconcile_date_label = ttk.Label(self,text="Previous Close Date:")
		self.previous_general_ledger_reconcile_date_label.place(x=600,y=15)
		self.previous_general_ledger_reconcile_date_entry_text = tk.StringVar()
		self.previous_general_ledger_reconcile_date_entry = ttk.Entry(self,textvariable=self.previous_general_ledger_reconcile_date_entry_text,state=tk.DISABLED)
		self.previous_general_ledger_reconcile_date_entry.place(x=600,y=45)

		self.previous_general_ledger_reconcile_balance_label = ttk.Label(self,text="Previous Close Balance:")
		self.previous_general_ledger_reconcile_balance_label.place(x=600,y=85)
		self.previous_general_ledger_reconcile_balance_entry_text = tk.StringVar()
		self.previous_general_ledger_reconcile_balance_entry = ttk.Entry(self,textvariable=self.previous_general_ledger_reconcile_balance_entry_text,state=tk.DISABLED)
		self.previous_general_ledger_reconcile_balance_entry.place(x=600,y=115)

		self.new_general_ledger_reconcile_date_label = ttk.Label(self,text="New Close Date:")
		self.new_general_ledger_reconcile_date_label.place(x=600,y=155)
		self.new_general_ledger_reconcile_date_entry_text = tk.StringVar()
		self.new_general_ledger_reconcile_date_entry = ttk.Entry(self,textvariable=self.new_general_ledger_reconcile_date_entry_text)
		self.new_general_ledger_reconcile_date_entry.place(x=600,y=185)

		self.new_general_ledger_reconcile_balance_label = ttk.Label(self,text="New Close Balance:")
		self.new_general_ledger_reconcile_balance_label.place(x=600,y=225)
		self.new_general_ledger_reconcile_balance_entry_text = tk.StringVar()
		self.new_general_ledger_reconcile_balance_entry = ttk.Entry(self,textvariable=self.new_general_ledger_reconcile_balance_entry_text)
		self.new_general_ledger_reconcile_balance_entry.place(x=600,y=255)

		self.cancel_general_ledger_changes_button = ttk.Button(self,text="Cancel",command=self.cancel_changes)
		self.cancel_general_ledger_changes_button.place(x=490,y=230)

		self.submit_general_ledger_changes_button = ttk.Button(self,text="Delete",command=self.submit_changes)
		self.submit_general_ledger_changes_button.place(x=400,y=230)

		self.debits_label = ttk.Label(self,text="Debits:")
		self.debits_label.place(x=20,y=320)

		self.debits_scrollbar = ttk.Scrollbar(self)
		self.debits_scrollbar.place(x=353,y=350,width=20,height=170)
		self.debits_listbox = tk.Listbox(self,yscrollcommand=self.debits_scrollbar)
		self.debits_listbox.place(x=20,y=350,width=333,height=170)
		self.debits_scrollbar.config(command=self.debits_listbox.yview)

		self.credits_label = ttk.Label(self,text="Credits:")
		self.credits_label.place(x=20,y=550)

		self.credits_scrollbar = ttk.Scrollbar(self)
		self.credits_scrollbar.place(x=353,y=570,width=20,height=170)
		self.credits_listbox = tk.Listbox(self,yscrollcommand=self.credits_scrollbar)
		self.credits_listbox.place(x=20,y=570,width=333,height=170)
		self.credits_scrollbar.config(command=self.credits_listbox.yview)

		self.selected_values_label = ttk.Label(self,text="Selected Values:")
		self.selected_values_label.place(x=400,y=320)

		self.selected_values_scrollbar = ttk.Scrollbar(self)
		self.selected_values_scrollbar.place(x=753,y=350,width=20,height=390)
		self.selected_values_listbox = tk.Listbox(self,yscrollcommand=self.selected_values_scrollbar)
		self.selected_values_listbox.place(x=400,y=350,width=353,height=390)
		self.selected_values_scrollbar.config(command=self.selected_values_listbox.yview)


	def select_general_ledger(self):

		try:

			self.debits_listbox.delete(0,tk.END)

			self.credits_listbox.delete(0,tk.END)

			general_ledger = None

			debits_script = '''SELECT JOURNAL_ENTRY_DATE, JOURNAL_ENTRY_DEBIT_AMOUNT FROM journal_entries WHERE DEBIT_GENERAL_LEDGER_NAME=? ORDER BY JOURNAL_ENTRY_DATE DESC;'''

			credits_script = '''SELECT JOURNAL_ENTRY_DATE, JOURNAL_ENTRY_CREDIT_AMOUNT FROM journal_entries WHERE CREDIT_GENERAL_LEDGER_NAME=? ORDER BY JOURNAL_ENTRY_DATE DESC;'''

			for item in self.select_general_ledger_listbox.curselection():

				general_ledger = self.select_general_ledger_listbox.get(item)

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(debits_script,[general_ledger])

				for item in cursor:

					self.debits_listbox.insert(0,item)

				connection.commit()

				cursor.close()

			with sqlite3.connect("SQL.db") as connection:

				cursor = connection.cursor()

				cursor.execute(credits_script,[general_ledger])

				for item in cursor:

					self.credits_listbox.insert(0,item)

				connection.commit()

				cursor.close()

		except Exception as error:

			reconcile_general_ledger_error_message_1 = tk.messagebox.showinfo(title="Reconcile General Ledger",message=f"{error}")


	def submit_changes(self):

		try:

			pass

		except Exception as error:

			submit_changes_error_message_1 = tk.messagebox.showinfo(title="Reconcile General Ledger",message=f"{error}")


	def cancel_changes(self):

		try:

			pass

		except Exception as error:

			cancel_changes_error_message_1 = tk.messagebox.showinfo(title="Reconcile General Ledger",message=f"{error}")


	def destroy(self):

		self.__class__.alive = False

		return super().destroy()
