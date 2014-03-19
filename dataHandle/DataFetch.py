import os

class DataHandle(object):
	"""Class to get the data"""
	def __init__(self, filename):
		super(DataHandle, self).__init__()
		self.filename = filename
		fileDir = os.path.dirname(os.getcwd())
		# fileDir = os.path.dirname(fileDir)
		self.dataDir = os.path.join(fileDir, 'data', self.filename)
		self.item = {}


	def loadData(self):
		with open(self.dataDir, 'r') as file:
			for line in file.readlines():
				data = line.split('\t')
				# print data
				userId = data[0]
				itemId = data[1]
				rate = data[2]
				item_rate = {}
				item_rate[itemId] = rate
				self.item[userId] = item_rate
				print userId, self.item[userId]

def main():
	data = DataHandle('sample.data')
	data.loadData()

if __name__ == '__main__':
	main()
