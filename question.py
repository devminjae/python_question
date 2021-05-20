import pandas as pd

class map_class:
	def __init__(self, variable1):
		self.variable1 = variable1
		self.variable2 = self.createVariable()
		self.variable_df = self.createDF()
		self.img = self.createImg()
	def createVariable(self, ):
		variable1 = self.variable1
		return variable1 + '_extended'

	def createDF(self, ):
		variable2 = self.variable2
		v_df = pd.read_csv(variable2+'.csv')
		return v_df

	def createImg(self, ):
		import numpy as np
		from matplotlib import pyplot as plt
		plt.scatter(self.variable_df['X'], self.variable_df['Y'])
		plt.savefig(variable1+'.png')
		print('image is generated')
