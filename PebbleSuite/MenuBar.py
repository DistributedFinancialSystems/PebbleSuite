"""
[ ]
[ ]
[ ]
[ ]	MENUBAR.PY
[ ]
[ ]
[ ]
"""
"""
[ ]
[ ]
[ ]
[ ]	IMPORT PYTHON MODULES
[ ]
[ ]
[ ]
"""


#Python Standard Library modules.
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo

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
from AP_print_credit_memo import *

#Accounts Receivable Menu modules:
from AR_new_client import *
from AR_edit_client import *
from AR_delete_client import *
from AR_new_invoice import *
from AR_edit_invoice import *
from AR_delete_invoice import *
from AR_print_invoice import *
from AR_new_credit_memo import *
from AR_edit_credit_memo import *
from AR_delete_credit_memo import *
from AR_print_credit_memo import *

#Company Menu modules:
from Company_commands import *
from Export_database import *

#General Ledgers Menu modules:
from GL_new_GL import *
from GL_edit_GL import *
from GL_delete_GL import *

#Help Menu modules:
from Help_commands import *

#Journal Entries Menu modules:
from JE_new_journal_entry import *

#Reports Menu modules:
from Reports_commands import *
from Reports_AP_aging_report import *
from Reports_AR_aging_report import *
from Reports_vendor_summary import *
from Reports_client_summary import *


"""
[ ]
[ ]
[ ]
[ ]	MENU_BAR CLASS:
[ ]
[ ]
[ ]
"""


class MENU_BAR(tk.Menu):


	"""
	[ ]
	[ ]
	[ ]
	[ ]	INITIALIZE CLASS WIDGETS:
	[ ]
	[ ]
	[ ]
	"""


	def __init__(self,root):

		#Initialize Menu Bar Tkinter widget
		super().__init__(root)

		#AP Menu Tkinter widgets
		self.AP_menu = tk.Menu(self)
		self.AP_menu.add_command(label="New Vendor",command=self.new_vendor)
		self.AP_menu.add_command(label="Edit Vendor",command=self.edit_vendor)
		self.AP_menu.add_command(label="Delete Vendor",command=self.delete_vendor)
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
		self.AP_menu.add_command(label="Apply Credit Memo",command=self.new_AP)
		self.AP_menu.add_command(label="Print Credit Memo",command=self.print_vendor_credit_memo)
		self.add_cascade(label="Accounts Payable",menu=self.AP_menu)

		#AR Menu Tkinter widgets
		self.AR_menu = tk.Menu(self)
		self.AR_menu.add_command(label="New Client",command=self.new_client)
		self.AR_menu.add_command(label="Edit Client",command=self.edit_client)
		self.AR_menu.add_command(label="Delete Client",command=self.delete_client)
		self.AR_menu.add_separator()
		self.AR_menu.add_command(label="New Invoice",command=self.new_client_invoice)
		self.AR_menu.add_command(label="Edit Invoice",command=self.edit_client_invoice)
		self.AR_menu.add_command(label="Delete Invoice",command=self.delete_client_invoice)
		self.AR_menu.add_command(label="Pay Invoice",command=self.new_AR)
		self.AR_menu.add_command(label="Print Invoice",command=self.print_client_invoice)
		self.AR_menu.add_separator()
		self.AR_menu.add_command(label="New Credit Memo",command=self.new_client_credit_memo)
		self.AR_menu.add_command(label="Edit Credit Memo",command=self.edit_client_credit_memo)
		self.AR_menu.add_command(label="Delete Credit Memo",command=self.delete_client_credit_memo)
		self.AR_menu.add_command(label="Apply Credit Memo",command=self.new_AR)
		self.AR_menu.add_command(label="Print Credit Memo",command=self.print_client_credit_memo)
		self.add_cascade(label="Accounts Receivable",menu=self.AR_menu)

		#Export Menu Tkinter widgets:
		self.company_menu = tk.Menu(self)
		self.company_menu.add_command(label="Company Information",command=self.new_company)
		self.company_menu.add_command(label="Export Database",command=self.new_company)
		self.add_cascade(label="Company",menu=self.company_menu)

		#Financial Reports Menu Tkinter widgets
		self.financial_reports_menu = tk.Menu(self)
		self.financial_reports_menu.add_command(label="AP Aging Report",command=self.new_reports)
		self.financial_reports_menu.add_command(label="AR Aging Report",command=self.new_reports)
		self.financial_reports_menu.add_command(label="Balance Sheet",command=self.new_reports)
		self.financial_reports_menu.add_command(label="Cash Flows",command=self.new_reports)
		self.financial_reports_menu.add_command(label="Charts of Accounts",command=self.new_reports)
		self.financial_reports_menu.add_command(label="Profit & Loss",command=self.new_reports)
		self.financial_reports_menu.add_separator()
		self.financial_reports_menu.add_command(label="Vendor Summary",command=self.vendor_summary)
		self.financial_reports_menu.add_command(label="Client Summary",command=self.client_summary)
		self.add_cascade(label="Financial Reports",menu=self.financial_reports_menu)

		#Financial Tools Menu Tkinter widgets:
		self.financial_tools_menu = tk.Menu(self)
		self.financial_tools_menu.add_command(label="Calculator",command=self.calculator)
		self.add_cascade(label="Financial Tools",menu=self.financial_tools_menu)

		#GL Menu Tkinter widgets
		self.GL_menu = tk.Menu(self)
		self.GL_menu.add_command(label="New General Ledger",command=self.new_GL_entry)
		self.GL_menu.add_command(label="Edit General Ledger",command=self.edit_GL)
		self.GL_menu.add_command(label="Delete General Ledger",command=self.delete_GL)
		self.GL_menu.add_separator()
		self.GL_menu.add_command(label="Export General Ledgers",command=self.new_GL)
		self.GL_menu.add_command(label="General Ledger Summary",command=self.new_GL)
		self.GL_menu.add_command(label="Reconcile General Ledger",command=self.new_GL)
		self.add_cascade(label="General Ledgers",menu=self.GL_menu)

		#Help Menu Tkinter widgets
		self.help_menu = tk.Menu(self)
		self.help_menu.add_command(label="Accounts Payable",command=self.new_help)
		self.help_menu.add_command(label="Accounts Receivable",command=self.new_help)
		self.help_menu.add_command(label="Billing",command=self.new_help)
		self.help_menu.add_command(label="General Ledgers",command=self.new_help)
		self.help_menu.add_command(label="Journal Entries",command=self.new_help)
		self.help_menu.add_command(label="Reports",command=self.new_help)
		self.help_menu.add_command(label="Taxes",command=self.new_help)
		self.add_cascade(label="Help",menu=self.help_menu)

		#Journal Entries Menu Tkinter widgets
		self.JE_menu = tk.Menu(self)
		self.JE_menu.add_command(label="New Journal Entry",command=self.new_JE_entry)
		self.JE_menu.add_command(label="Edit Journal Entry",command=self.new_JE)
		self.JE_menu.add_command(label="Delete Journal Entry",command=self.new_JE)
		self.JE_menu.add_separator()
		self.JE_menu.add_command(label="Journal Entry Summary",command=self.new_JE)
		self.JE_menu.add_command(label="Export Journal Entries",command=self.new_JE)
		self.JE_menu.add_command(label="Multi-Journal Entry",command=self.new_JE)
		self.add_cascade(label="Journal Entries",menu=self.JE_menu)

		#Settings Menu Tkinter widgets:
		self.settings_menu = tk.Menu(self)
		self.settings_menu.add_command(label="Settings",command=self.new_settings)
		self.add_cascade(label="Settings",menu=self.settings_menu)

		#Taxes Menu Tkinter widgets
		self.taxes_menu = tk.Menu(self)
		self.taxes_menu.add_command(label="Company Taxes",command=self.new_taxes)
		self.taxes_menu.add_separator()
		self.taxes_menu.add_command(label="Create 1099-MISC Forms",command=self.new_taxes)
		self.taxes_menu.add_command(label="Create 1099-NEC Forms",command=self.new_taxes)
		self.taxes_menu.add_command(label="Create Schedule C",command=self.new_taxes)
		self.add_cascade(label="Taxation",menu=self.taxes_menu)


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

	def print_client_credit_memo(self):

		if not AR_PRINT_CREDIT_MEMO_WINDOW.alive:

			self.secondary_window = AR_PRINT_CREDIT_MEMO_WINDOW()


	"""
	[ ]
	[ ]
	[ ]
	[ ]	COMPANY MENU FUNCTIONS:
	[ ]
	[ ]
	[ ]
	"""


	def new_company(self):

		new_company_message = tk.messagebox.showinfo(title="New Company",message="This is the Company Menu.")


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
	[ ]	SETTINGS MENU FUNCTIONS:
	[ ]
	[ ]
	[ ]
	"""

	def new_settings(self):

		showinfo(title="Settings Menu",message="This is the Settings menu!")


	"""
	[ ]
	[ ]
	[ ]
	[ ]	TAXATION MENU FUNCTIONS:
	[ ]
	[ ]
	[ ]
	"""


	def new_taxes(self):

		showinfo(title="Taxes Menu",message="This is the Taxes menu!")


	"""
	[ ]
	[ ]
	[ ]
	[ ]	TOOLS MENU FUNCTIONS:
	[ ]
	[ ]
	[ ]
	"""


	def calculator(self):

		calculator = tk.messagebox.showinfo(title="Tools",message="Calculator")


"""
[ ]
[ ]
[ ]
[ ]	END OF FILE
[ ]
[ ]
[ ]
"""
