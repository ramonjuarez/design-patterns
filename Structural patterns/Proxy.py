import time

class Producer:
	"""Define the 'resource-intensive' objecto ton instantiate"""
	def produce(self):
		print('Producer is worrking hard')

	def meet(self):
		print('Producer has time to meet you now')

class Proxy:
	"""Define the 'relatively less resource-intensive' proxy to instantiate as a middelman"""
	def __init__(self):
		self.occupied = "No"
		self.producer = None

	def produce (self):
		"""Check if the Producer is available"""
		print("Artist checking if Producer is available")

		if self.occupied == 'No':
			self.producer = Producer()
			time.sleep(2)

			self.producer.meet()

		else:
			time.sleep(2)
			print("Producer is busy")

#Instantiate a proxy
p = Proxy()
#Make the proxy: Artist produce untill Produces is available
p.produce()
#Change the state to occupied
p.occupied = "Yes"

#Make the Producer produce
p.produce()