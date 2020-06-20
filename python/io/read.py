import pandas as pd

def load_csv(file):
	df = pd.read_csv(file)
	return df

def df_transform(df):
	ndarray = df.values

if __name__ == "__main__": 
	data_file = "../../dataset/dataR2.csv"
	df = load_csv(data_file)