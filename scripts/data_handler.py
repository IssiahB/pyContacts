import psycopg2

def _connection_data():
	data = {}
	with open('data/connection_data', 'r') as file:
		for line in file:
			values = line.split()
			data[values[0]] = values[1]

	return data


class Database:
	def __init__(self):
		pass

	def connect(self):
		data = _connection_data()
		self.conn = psycopg2.connect(
		 	database=data['database'],
		 	user=data['user'],
		 	password=data['password'],
		 	host=data['host'],
		 	port=data['port']
		 	)

		self.cur = self.conn.cursor()

	def test(self):
		self.cur.execute('select version()')
		data = self.cur.fetchone()
		print(data)

	def disconnect(self):
		self.conn.close()