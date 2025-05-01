#Python Standard Library modules.
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import stripe

#Accounts Payable Menu modules:
from AP_new_vendor import *
from AP_edit_vendor import *
from AP_delete_vendor import *
from AP_new_invoice import *
from AP_edit_invoice import *
from AP_delete_invoice import *
from AP_pay_invoice import *
from AP_print_invoice import *
from AP_new_credit_memo import *
from AP_edit_credit_memo import *
from AP_delete_credit_memo import *
from AP_apply_credit_memo import *
from AP_print_credit_memo import *

#Accounts Receivable Menu modules:
from AR_new_client import *
from AR_edit_client import *
from AR_delete_client import *
from AR_new_invoice import *
from AR_edit_invoice import *
from AR_delete_invoice import *
from AR_pay_invoice import *
from AR_print_invoice import *
from AR_new_credit_memo import *
from AR_edit_credit_memo import *
from AR_delete_credit_memo import *
from AR_apply_credit_memo import *
from AR_print_credit_memo import *

#Customers Menu modules:
from Customers_new_customer import *
from Customers_edit_customer import *
from Customers_delete_customer import *
from Customers_customer_summary import *

#Company Menu modules:
from Company_commands import *
from Export_database import *

#General Ledgers Menu modules:
from GL_new_GL import *
from GL_edit_GL import *
from GL_delete_GL import *
from GL_GL_summary import *

#Help Menu modules:
from Help_commands import *

#Inventory Menu modules:
from Inventory_new_product import *
from Inventory_edit_product import *
from Inventory_delete_product import *
from Inventory_new_inventory import *

#Journal Entries Menu modules:
from JE_new_journal_entry import *
from JE_JE_summary import *

#Reports Menu modules:
from Reports_commands import *
from Reports_AP_aging_report import *
from Reports_AR_aging_report import *
from Reports_vendor_summary import *
from Reports_client_summary import *

#Settings Menu modules:
from Settings_stripe_account import *




class MENU_BAR(tk.Menu):

	def __init__(self,root):

		#Initialize Menu Bar Tkinter widget
		super().__init__(root)

		#AP Menu Tkinter widgets
		self.AP_menu = tk.Menu(self)
		self.AP_menu.add_command(label="New Vendor",command=self.new_vendor)
		self.AP_menu.add_command(label="Edit Vendor",command=self.edit_vendor)
		self.AP_menu.add_command(label="Delete Vendor",command=self.delete_vendor)
		self.AP_menu.add_command(label="Vendor Summary",command=self.vendor_summary)
		self.AP_menu.add_separator()
		self.AP_menu.add_command(label="New Invoice",command=self.new_vendor_invoice)
		self.AP_menu.add_command(label="Edit Invoice",command=self.edit_vendor_invoice)
		self.AP_menu.add_command(label="Delete Invoice",command=self.delete_vendor_invoice)
		self.AP_menu.add_command(label="Pay Invoice",command=self.pay_vendor_invoice)
		self.AP_menu.add_command(label="Print Invoice",command=self.print_vendor_invoice)
		self.AP_menu.add_separator()
		self.AP_menu.add_command(label="New Credit Memo",command=self.new_vendor_credit_memo)
		self.AP_menu.add_command(label="Edit Credit Memo",command=self.edit_vendor_credit_memo)
		self.AP_menu.add_command(label="Delete Credit Memo",command=self.delete_vendor_credit_memo)
		self.AP_menu.add_command(label="Apply Credit Memo",command=self.apply_vendor_credit_memo)
		self.AP_menu.add_command(label="Print Credit Memo",command=self.print_vendor_credit_memo)
		self.add_cascade(label="Accounts Payable",menu=self.AP_menu)

		#AR Menu Tkinter widgets
		self.AR_menu = tk.Menu(self)
		self.AR_menu.add_command(label="New Client",command=self.new_client)
		self.AR_menu.add_command(label="Edit Client",command=self.edit_client)
		self.AR_menu.add_command(label="Delete Client",command=self.delete_client)
		self.AR_menu.add_command(label="Client Summary",command=self.client_summary)

		self.AR_menu.add_separator()
		self.AR_menu.add_command(label="New Invoice",command=self.new_client_invoice)
		self.AR_menu.add_command(label="Edit Invoice",command=self.edit_client_invoice)
		self.AR_menu.add_command(label="Delete Invoice",command=self.delete_client_invoice)
		self.AR_menu.add_command(label="Pay Invoice",command=self.pay_client_invoice)
		self.AR_menu.add_command(label="Print Invoice",command=self.print_client_invoice)
		self.AR_menu.add_separator()
		self.AR_menu.add_command(label="New Credit Memo",command=self.new_client_credit_memo)
		self.AR_menu.add_command(label="Edit Credit Memo",command=self.edit_client_credit_memo)
		self.AR_menu.add_command(label="Delete Credit Memo",command=self.delete_client_credit_memo)
		self.AR_menu.add_command(label="Apply Credit Memo",command=self.apply_client_credit_memo)
		self.AR_menu.add_command(label="Print Credit Memo",command=self.print_client_credit_memo)
		self.add_cascade(label="Accounts Receivable",menu=self.AR_menu)

		#Customer Sales Tkinter widgets
		self.customer_sales_menu = tk.Menu(self)
		self.customer_sales_menu.add_command(label="New Customer",command=self.new_customer)
		self.customer_sales_menu.add_command(label="Edit Customer",command=self.edit_customer)
		self.customer_sales_menu.add_command(label="Delete Customer",command=self.delete_customer)
		self.customer_sales_menu.add_command(label="Customer Summary",command=self.customer_summary)
		self.add_cascade(label="Customers",menu=self.customer_sales_menu)

		#GL Menu Tkinter widgets
		self.GL_menu = tk.Menu(self)
		self.GL_menu.add_command(label="New General Ledger",command=self.new_GL_entry)
		self.GL_menu.add_command(label="Edit General Ledger",command=self.edit_GL)
		self.GL_menu.add_command(label="Delete General Ledger",command=self.delete_GL)
		self.GL_menu.add_separator()
		self.GL_menu.add_command(label="General Ledger Summary",command=self.GL_summary)
		self.GL_menu.add_command(label="Reconcile General Ledger",command=self.new_GL)
		self.add_cascade(label="General Ledgers",menu=self.GL_menu)

		#Help Menu Tkinter widgets
		self.help_menu = tk.Menu(self)
		self.help_menu.add_command(label="NULL",command=self.new_help)
		self.add_cascade(label="Help",menu=self.help_menu)

		#Inventory Menu
		self.inventory_menu = tk.Menu(self)
		self.inventory_menu.add_command(label="New Product",command=self.new_product)
		self.inventory_menu.add_command(label="Edit Product",command=self.edit_product)
		self.inventory_menu.add_command(label="Delete Product",command=self.delete_product)
		self.inventory_menu.add_separator()
		self.inventory_menu.add_command(label="Add Inventory",command=self.add_inventory)
		self.inventory_menu.add_command(label="Edit Inventory",command=self.new_inventory)
		self.inventory_menu.add_command(label="Delete Inventory",command=self.new_inventory)
		self.inventory_menu.add_command(label="Inventory Stock",command=self.new_inventory)
		self.inventory_menu.add_separator()
		self.inventory_menu.add_command(label="Sales Tax",command=self.new_inventory)
		self.add_cascade(label="Inventory",menu=self.inventory_menu)

		#Journal Entries Menu Tkinter widgets
		self.JE_menu = tk.Menu(self)
		self.JE_menu.add_command(label="New Journal Entry",command=self.new_JE_entry)
		self.JE_menu.add_command(label="Edit Journal Entry",command=self.new_JE)
		self.JE_menu.add_command(label="Delete Journal Entry",command=self.new_JE)
		self.JE_menu.add_separator()
		self.JE_menu.add_command(label="Journal Entry Summary",command=self.JE_summary)
		self.JE_menu.add_command(label="Multi-Journal Entry",command=self.new_JE)
		self.add_cascade(label="Journal Entries",menu=self.JE_menu)

		#Month-End Menu Tkinter widgets:
		self.month_end_menu = tk.Menu(self)
		self.month_end_menu.add_command(label="Amortizations",command=self.new_ME)
		self.month_end_menu.add_command(label="Close Books",command=self.new_ME)
		self.month_end_menu.add_command(label="Fixed Assets",command=self.new_ME)
		self.month_end_menu.add_command(label="Reconcile",command=self.new_ME)
		self.add_cascade(label="Monthly Close",menu=self.month_end_menu)

		#Financial Reports Menu Tkinter widgets
		self.financial_reports_menu = tk.Menu(self)
		self.financial_reports_menu.add_command(label="AP Aging Report",command=self.new_reports)
		self.financial_reports_menu.add_command(label="AR Aging Report",command=self.new_reports)
		self.financial_reports_menu.add_command(label="Balance Sheet",command=self.new_reports)
		self.financial_reports_menu.add_command(label="Cash Flows",command=self.new_reports)
		self.financial_reports_menu.add_command(label="Charts of Accounts",command=self.new_reports)
		self.financial_reports_menu.add_command(label="Profit & Loss",command=self.new_reports)
		self.financial_reports_menu.add_separator()
		self.financial_reports_menu.add_command(label="1099 Forms",command=self.new_reports)
		self.add_cascade(label="Reporting",menu=self.financial_reports_menu)

		#Sales Menu Tkinter widgets:
		self.sales_menu = tk.Menu(self)
		self.sales_menu.add_command(label="New Transaction",command=self.new_sales)
		self.sales_menu.add_command(label="Delete Transaction",command=self.new_sales)
		self.sales_menu.add_command(label="Print Receipt",command=self.new_sales)
		self.sales_menu.add_command(label="Void Transaction",command=self.new_sales)
		self.add_cascade(label="Sales",menu=self.sales_menu)

		#Settings Menu Tkinter widgets:
		self.settings_menu = tk.Menu(self)
		self.settings_menu.add_command(label="Company",command=self.new_settings)
		self.settings_menu.add_command(label="Database Settings",command=self.new_settings)
		self.settings_menu.add_command(label="Passwords",command=self.new_settings)
		self.settings_menu.add_command(label="Working Directory",command=self.new_settings)
		self.settings_menu.add_command(label="Stripe Account",command=self.update_stripe_API_key)
		self.add_cascade(label="Settings",menu=self.settings_menu)


	"""
	[ ]
	[ ]
	[ ]
	[ ]	ACCOUNTS PAYABLE MENU FUNCTIONS:
	[ ]
	[ ]
	[ ]
	"""


	def new_AP(self):

		showinfo(title="AP Menu",message="This is the Accounts Payable menu!")

	def new_vendor(self):

		if not NEW_VENDOR_WINDOW.alive:
			self.secondary_window = NEW_VENDOR_WINDOW()

	def edit_vendor(self):

		if not EDIT_VENDOR_WINDOW.alive:
			self.secondary_window = EDIT_VENDOR_WINDOW()

	def delete_vendor(self):

		if not DELETE_VENDOR_WINDOW.alive:
			self.secondary_window = DELETE_VENDOR_WINDOW()

	def new_vendor_invoice(self):

		if not NEW_INVOICE_WINDOW.alive:
			self.secondary_window = NEW_INVOICE_WINDOW()

	def edit_vendor_invoice(self):

		if not AP_EDIT_INVOICE_WINDOW.alive:
			self.secondary_window = AP_EDIT_INVOICE_WINDOW()

	def delete_vendor_invoice(self):

		if not DELETE_INVOICE_WINDOW.alive:
			self.secondary_window = DELETE_INVOICE_WINDOW()

	def pay_vendor_invoice(self):

		if not AP_PAY_INVOICE_WINDOW.alive:
			self.secondary_window = AP_PAY_INVOICE_WINDOW()

	def print_vendor_invoice(self):

		if not AP_PRINT_INVOICE_WINDOW.alive:
			self.secondary_window = AP_PRINT_INVOICE_WINDOW()

	def new_vendor_credit_memo(self):

		if not NEW_VENDOR_CREDIT_MEMO_WINDOW.alive:
			self.secondary_window = NEW_VENDOR_CREDIT_MEMO_WINDOW()

	def edit_vendor_credit_memo(self):

		if not AP_EDIT_CREDIT_MEMO_WINDOW.alive:
			self.secondary_window = AP_EDIT_CREDIT_MEMO_WINDOW()

	def delete_vendor_credit_memo(self):

		if not DELETE_VENDOR_CREDIT_MEMO_WINDOW.alive:
			self.secondary_window = DELETE_VENDOR_CREDIT_MEMO_WINDOW()

	def apply_vendor_credit_memo(self):

		if not AP_PAY_CREDIT_MEMO_WINDOW.alive:
			self.secondary_window = AP_PAY_CREDIT_MEMO_WINDOW()

	def print_vendor_credit_memo(self):
		if not AP_PRINT_CREDIT_MEMO_WINDOW.alive:
			self.secondary_window = AP_PRINT_CREDIT_MEMO_WINDOW()


	"""
	[ ]
	[ ]
	[ ]
	[ ]	ACCOUNTS RECEIVABLE MENU FUNCTIONS:
	[ ]
	[ ]
	[ ]
	"""


	def new_AR(self):

		showinfo(title="AP Menu",message="This is the AR menu!")

	def new_client(self):

		if not NEW_CLIENT_WINDOW.alive:
			self.secondary_window = NEW_CLIENT_WINDOW()

	def edit_client(self):

		if not EDIT_CLIENT_WINDOW.alive:
			self.secondary_window = EDIT_CLIENT_WINDOW()

	def delete_client(self):

		if not DELETE_CLIENT_WINDOW.alive:
			self.secondary_window = DELETE_CLIENT_WINDOW()

	def new_client_invoice(self):

		if not AR_NEW_INVOICE_WINDOW.alive:
			self.secondary_window = AR_NEW_INVOICE_WINDOW()

	def edit_client_invoice(self):

		if not AR_EDIT_INVOICE_WINDOW.alive:
			self.secondary_window = AR_EDIT_INVOICE_WINDOW()

	def delete_client_invoice(self):

		if not AR_DELETE_INVOICE_WINDOW.alive:
			self.secondary_window = AR_DELETE_INVOICE_WINDOW()

	def pay_client_invoice(self):

		if not AR_PAY_INVOICE_WINDOW.alive:
			self.secondary_window = AR_PAY_INVOICE_WINDOW()

	def print_client_invoice(self):

		if not AR_PRINT_INVOICE_WINDOW.alive:
			self.secondary_window = AR_PRINT_INVOICE_WINDOW()

	def new_client_credit_memo(self):

		if not NEW_CLIENT_CREDIT_MEMO_WINDOW.alive:
			self.secondary_window = NEW_CLIENT_CREDIT_MEMO_WINDOW()

	def edit_client_credit_memo(self):

		if not AR_EDIT_CREDIT_MEMO_WINDOW.alive:
			self.secondary_window = AR_EDIT_CREDIT_MEMO_WINDOW()

	def delete_client_credit_memo(self):

		if not DELETE_CLIENT_CREDIT_MEMO_WINDOW.alive:
			self.secondary_window = DELETE_CLIENT_CREDIT_MEMO_WINDOW()

	def apply_client_credit_memo(self):

		if not AR_PAY_CREDIT_MEMO_WINDOW.alive:
			self.secondary_window = AR_PAY_CREDIT_MEMO_WINDOW()

	def print_client_credit_memo(self):

		if not AR_PRINT_CREDIT_MEMO_WINDOW.alive:

			self.secondary_window = AR_PRINT_CREDIT_MEMO_WINDOW()

	"""
	[ ]
	[ ]
	[ ]
	[ ]	CUSTOMER SALES FUNCTIONS:
	[ ]
	[ ]
	[ ]
	"""

	def new_sale(self):

		showinfo(title="Customer Sales",message="This is the Customer Sales menu.")

	def new_customer(self):

		if not NEW_CUSTOMER_WINDOW.alive:

			self.secondary_window = NEW_CUSTOMER_WINDOW()

	def edit_customer(self):

		if not EDIT_CUSTOMER_WINDOW.alive:

			self.secondary_window = EDIT_CUSTOMER_WINDOW()

	def delete_customer(self):

		if not DELETE_CUSTOMER_WINDOW.alive:

			self.secondary_window = DELETE_CUSTOMER_WINDOW()

	def customer_summary(self):

		if not CUSTOMER_SUMMARY_WINDOW.alive:

			self.secondary_window = CUSTOMER_SUMMARY_WINDOW()


	"""
	[ ]
	[ ]
	[ ]
	[ ]	GENERAL LEDGER FUNCTIONS:
	[ ]
	[ ]
	[ ]
	"""


	def new_GL(self):

		showinfo(title="GL Menu",message="This is the GL menu!")

	def new_GL_entry(self):

		if not NEW_GL_WINDOW.alive:

			self.secondary_window = NEW_GL_WINDOW()

	def edit_GL(self):

		if not EDIT_GL_WINDOW.alive:

			self.secondary_window = EDIT_GL_WINDOW()

	def delete_GL(self):

		if not DELETE_GL_WINDOW.alive:

			self.secondary_window = DELETE_GL_WINDOW()

	def GL_summary(self):

		if not GL_SUMMARY_WINDOW.alive:

			self.secondary_window = GL_SUMMARY_WINDOW()


	"""
	[ ]
	[ ]
	[ ]
	[ ]	HELP MENU FUNCTIONS:
	[ ]
	[ ]
	[ ]
	"""


	def new_help(self):

		showinfo(title="Help Menu",message="This is the Help menu!")


	"""
	[ ]
	[ ]
	[ ]
	[ ]	INVENTORY MENU FUNCTIONS:
	[ ]
	[ ]
	[ ]
	"""

	def new_inventory(self):

		showinfo(title="Inventory Menu",message="This is the Inventory menu!")

	def new_product(self):

		if not NEW_PRODUCT_WINDOW.alive:

			self.secondary_window = NEW_PRODUCT_WINDOW()

	def edit_product(self):

		if not EDIT_PRODUCT_WINDOW.alive:

			self.secondary_window = EDIT_PRODUCT_WINDOW()

	def delete_product(self):

		if not DELETE_PRODUCT_WINDOW.alive:

			self.secondary_window = DELETE_PRODUCT_WINDOW()

	def add_inventory(self):

		if not NEW_INVENTORY_WINDOW.alive:

			self.secondary_window = NEW_INVENTORY_WINDOW()

	"""
	[ ]
	[ ]
	[ ]
	[ ]	JOURNAL ENTRIES MENU FUNCTIONS:
	[ ]
	[ ]
	[ ]
	"""


	def new_JE(self):

		showinfo(title="Journal Entries Menu",message="This is the Journal Entries menu!")


	def new_JE_entry(self):

		if not NEW_JE_WINDOW.alive:
			self.secondary_window = NEW_JE_WINDOW()

	def JE_summary(self):

		if not JE_SUMMARY_WINDOW.alive:
			self.secondary_window = JE_SUMMARY_WINDOW()

	def new_ME(self):

		showinfo(title="Month-End Menu",message="This is the Month-End menu!")


	"""
	[ ]
	[ ]
	[ ]
	[ ]	REPORTS MENU FUNCTIONS:
	[ ]
	[ ]
	[ ]
	"""


	def new_reports(self):

		showinfo(title="Reports Menu",message="This is the Reports menu!")


	def vendor_summary(self):

		if not VENDOR_SUMMARY_WINDOW.alive:
			self.secondary_window = VENDOR_SUMMARY_WINDOW()


	def client_summary(self):

		if not CLIENT_SUMMARY_WINDOW.alive:
			self.secondary_window = CLIENT_SUMMARY_WINDOW()

	"""
	[ ]
	[ ]
	[ ]
	[ ]	SALES MENU FUNCTIONS:
	[ ]
	[ ]
	[ ]
	"""

	def new_sales(self):

		showinfo(title="Sales Menu",message="This is the sales menu.")

	"""
	[ ]
	[ ]
	[ ]
	[ ]	SETTINGS MENU FUNCTIONS:
	[ ]
	[ ]
	[ ]
	"""

	def new_settings(self):

		showinfo(title="Settings Menu",message="This is the Settings menu!")

	def update_stripe_API_key(self):

		if not STRIPE_ACCOUNT_WINDOW.alive:
			self.secondary_window = STRIPE_ACCOUNT_WINDOW()


#End of MenuBar.py file.
