import os
import sqlite3


database_name = "SQL.db"


class database:


	def __init__(self,connection):

		self.connection = connection


	def create_pebblesuite_tables(self):

		permanent_directory = ('''CREATE TABLE IF NOT EXISTS permanent_directory(
					PERMANENT_DIRECTORY TEXT);''')

		working_directory = ('''CREATE TABLE IF NOT EXISTS working_directory(
					WORKING_DIRECTORY TEXT);''')

		stripe_api_script = ('''CREATE TABLE IF NOT EXISTS stripe_api_key(
					STRIPE_API_KEY TEXT);''')

		journal_entry_chronology = ('''CREATE TABLE IF NOT EXISTS journal_entry_chronology(
						JOURNAL_ENTRY_CHRONOLOGY INTEGER);''')

		tasks_sql_script = ('''CREATE TABLE IF NOT EXISTS tasks(
					TASK_DATE TEXT,
					TASK_NAME TEXT,
					TASK_NOTE TEXT);''')

		vendors_sql_script = ('''CREATE TABLE IF NOT EXISTS vendors(
					VENDOR_NAME TEXT,
					VENDOR_ADDRESS1 TEXT,
					VENDOR_ADDRESS2 TEXT,
					VENDOR_CITY TEXT,
					VENDOR_STATE TEXT,
					VENDOR_ZIP TEXT,
					VENDOR_COUNTRY TEXT,
					CONTACT_NAME TEXT,
					CONTACT_PHONE TEXT,
					CONTACT_EMAIL TEXT,
					VENDOR_1099 TEXT);''')

		clients_sql_script = ('''CREATE TABLE IF NOT EXISTS clients(
					CLIENT_NAME TEXT,
					CLIENT_ADDRESS1 TEXT,
					CLIENT_ADDRESS2 TEXT,
					CLIENT_CITY TEXT,
					CLIENT_STATE TEXT,
					CLIENT_ZIP TEXT,
					CLIENT_COUNTRY TEXT,
					CONTACT_NAME TEXT,
					CONTACT_PHONE TEXT,
					CONTACT_EMAIL TEXT,
					CONTACT_NOTES TEXT);''')

		vendor_invoices_sql_script = ('''CREATE TABLE IF NOT EXISTS vendor_invoices(
					INVOICE_NAME TEXT,
					INVOICE_ISSUE_DATE TEXT,
					INVOICE_DUE_DATE TEXT,
					INVOICE_NUMBER INTEGER,
					INVOICE_LIABILITY_ACCOUNT TEXT,
					INVOICE_EXPENSE_ACCOUNT TEXT,
					INVOICE_AMOUNT REAL,
					INVOICE_NOTES TEXT,
					INVOICE_STATUS TEXT,
					INVOICE_PAID_DATE TIMESTAMP);''')

		client_invoices_sql_script = ('''CREATE TABLE IF NOT EXISTS client_invoices(
					INVOICE_NAME TEXT,
					INVOICE_ISSUE_DATE TEXT,
					INVOICE_DUE_DATE TEXT,
					INVOICE_NUMBER INTEGER,
					INVOICE_ASSET_ACCOUNT TEXT,
					INVOICE_INCOME_ACCOUNT TEXT,
					INVOICE_AMOUNT REAL,
					INVOICE_NOTES TEXT,
					INVOICE_STATUS TEXT,
					INVOICE_PAID_DATE TIMESTAMP);''')

		vendor_credit_memos_sql_script = ('''CREATE TABLE IF NOT EXISTS vendor_credit_memos(
						CREDIT_MEMO_NAME TEXT,
						CREDIT_MEMO_ISSUE_DATE TEXT,
						CREDIT_MEMO_DUE_DATE TEXT,
						CREDIT_MEMO_NUMBER INTEGER,
						CREDIT_MEMO_ASSET_ACCOUNT TEXT,
						CREDIT_MEMO_INCOME_ACCOUNT TEXT,
						CREDIT_MEMO_AMOUNT REAL,
						CREDIT_MEMO_NOTES TEXT,
						CREDIT_MEMO_STATUS TEXT,
						CREDIT_MEMO_PAID_DATE TIMESTAMP);''')

		client_credit_memos_sql_script = ('''CREATE TABLE IF NOT EXISTS client_credit_memos(
						CREDIT_MEMO_NAME TEXT,
						CREDIT_MEMO_ISSUE_DATE TEXT,
						CREDIT_MEMO_DUE_DATE TEXT,
						CREDIT_MEMO_NUMBER INTEGER,
						CREDIT_MEMO_LIABILITY_ACCOUNT TEXT,
						CREDIT_MEMO_EXPENSE_ACCOUNT TEXT,
						CREDIT_MEMO_AMOUNT REAL,
						CREDIT_MEMO_NOTES TEXT,
						CREDIT_MEMO_STATUS TEXT,
						CREDIT_MEMO_PAID_DATE TIMESTAMP);''')

		customers_sql_script = ('''CREATE TABLE IF NOT EXISTS customers(
					CUSTOMER_NAME TEXT,
					ADDRESS_1 TEXT,
					ADDRESS_2 TEXT,
					CITY TEXT,
					STATE TEXT,
					POSTAL_CODE TEXT,
					COUNTRY TEXT,
					CONTACT_NAME TEXT,
					CONTACT_PHONE TEXT,
					CONTACT_EMAIL TEXT,
					CUSTOMER_NOTES TEXT,
					STRIPE_ID TEXT);''')

		customer_sales_sql_script = ('''CREATE TABLE IF NOT EXISTS customer_sales(
						SALE_DATE TIMESTAMP,
						SALE_CUSTOMER_NAME TEXT,
						SALE_INVENTORY_1_NAME TEXT,
						SALE_INVENTORY_1_QUANTITY INTEGER,
						SALE_TOTAL_AMOUNT REAL,
						SALE_RECEIPT_NUMBER INTEGER);''')

		products_sql_script = ('''CREATE TABLE IF NOT EXISTS products(
					PRODUCT_NAME TEXT,
					PRODUCT_NUMBER INTEGER,
					PRODUCT_VENDOR_NAME TEXT,
					PRODUCT_SALES_PRICE REAL);''')

		inventory_sql_script = ('''CREATE TABLE IF NOT EXISTS inventory(
					PRODUCT_VENDOR_NAME TEXT,
					PRODUCT_NAME TEXT,
					PRODUCT_PURCHASE_DATE TIMESTAMP,
					PRODUCT_TOTAL_PURCHASE_PRICE REAL,
					PRODUCT_EXPIRATION_DATE TIMESTAMP,
					PRODUCT_UNIT_QUANTITY INTEGER,
					PRODUCT_UNIT_WHOLESALE_PRICE REAL);''')

		general_ledger_sql_script = ('''CREATE TABLE IF NOT EXISTS general_ledgers(
						GENERAL_LEDGER_NAME TEXT,
						GENERAL_LEDGER_NUMBER INTEGER,
						GENERAL_LEDGER_TYPE TEXT);''')

		journal_entry_sql_script = ('''CREATE TABLE IF NOT EXISTS journal_entries(
						JOURNAL_ENTRY_TIMESTAMP TIMESTAMP,
						JOURNAL_ENTRY_NUMBER INTEGER,
						JOURNAL_ENTRY_DATE TIMESTAMP,
						VENDOR_INVOICE_NUMBER INTEGER,
						VENDOR_CREDIT_MEMO_NUMBER INTEGER,
						CLIENT_INVOICE_NUMBER INTEGER,
						CLIENT_CREDIT_MEMO_NUMBER INTEGER,
						DEBIT_GENERAL_LEDGER_NAME TEXT,
						DEBIT_GENERAL_LEDGER_NUMBER INTEGER,
						DEBIT_GENERAL_LEDGER_TYPE TEXT,
						CREDIT_GENERAL_LEDGER_NAME TEXT,
						CREDIT_GENERAL_LEDGER_NUMBER INTEGER,
						CREDIT_GENERAL_LEDGER_TYPE TEXT,
						JOURNAL_ENTRY_DEBIT_AMOUNT REAL,
						JOURNAL_ENTRY_CREDIT_AMOUNT REAL,
						JOURNAL_ENTRY_VENDOR_NAME TEXT,
						JOURNAL_ENTRY_CLIENT_NAME TEXT,
						JOURNAL_ENTRY_NOTES TEXT,
						RECONCILIATION_STATUS INTEGER);''')


		with sqlite3.connect(f"{self.connection}") as connection:

			cursor = connection.cursor()

			cursor.execute(permanent_directory)
			cursor.execute(working_directory)
			cursor.execute(stripe_api_script)
			cursor.execute(journal_entry_chronology)
			cursor.execute(tasks_sql_script)
			cursor.execute(vendors_sql_script)
			cursor.execute(clients_sql_script)
			cursor.execute(vendor_invoices_sql_script)
			cursor.execute(client_invoices_sql_script)
			cursor.execute(vendor_credit_memos_sql_script)
			cursor.execute(client_credit_memos_sql_script)
			cursor.execute(customers_sql_script)
			cursor.execute(customer_sales_sql_script)
			cursor.execute(products_sql_script)
			cursor.execute(inventory_sql_script)
			cursor.execute(general_ledger_sql_script)
			cursor.execute(journal_entry_sql_script)

			connection.commit()

			cursor.close()




if __name__ == "__main__":

	connect_database = database(database_name)
	connect_database.create_pebblesuite_tables()

	permanent_directory_key_default = '''INSERT INTO permanent_directory(
						PERMANENT_DIRECTORY)
						VALUES(?)'''

	directory = os.getcwd()

	working_directory_key_default = '''INSERT INTO working_directory(
					WORKING_DIRECTORY)
					VALUES(0);'''

	stripe_API_key_default = '''INSERT INTO stripe_api_key(
				STRIPE_API_KEY)
				VALUES(0);'''

	journal_entry_script = '''INSERT INTO journal_entry_chronology(
				JOURNAL_ENTRY_CHRONOLOGY)
				VALUES(1);'''

	with sqlite3.connect("SQL.db") as connection:

		cursor = connection.cursor()
		cursor.execute(permanent_directory_key_default,[directory])
		cursor.execute(working_directory_key_default)
		cursor.execute(stripe_API_key_default)
		cursor.execute(journal_entry_script)
		connection.commit()
		cursor.close()

	print("PebbleSuite database tables created!")
