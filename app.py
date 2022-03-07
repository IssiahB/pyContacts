import scripts

def main():
	data = scripts.Database()
	data.connect()
	data.test()
	data.disconnect()

if __name__ == '__main__':
	main()