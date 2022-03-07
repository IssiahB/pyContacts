import psycpg2

def get_connection_data():
	

class Database:
	def __init__(self):
		pass

	def connect(self):
		self.conn = sqlite3.connect('data/contacts.db')
		self.cur = self.conn.cursor()

	def disconnect(self):
		self.conn.close()