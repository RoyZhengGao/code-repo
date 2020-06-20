import pandas as pd
from sklearn.model_selection import train_test_split

def load_csv(file):
	df = pd.read_csv(file)
	return df

def df_transform(df):
	# to ndarray
	y = df["Classification"].values
	print(type(df["Classification"]),type(y))
	X = df["Age"].values
	X_train, X_test, y_train, y_test = train_test_split(
										X, y, test_size=0.2, random_state=42)
	# print(X_train,X_train.shape,X_test,X_test.shape)
	print(X.shape)
	return X_train, X_test, y_train, y_test

def model(X_train, X_test, y_train, y_test):
	clf = LogisticRegression(random_state=0).fit(X_train, y_train)
	y_pred = clf.predict(X_test)
	return y_pred

def evaluation(y_test, y_pred):
	
if __name__ == "__main__": 
	data_file = "../../dataset/dataR2.csv"
	df = load_csv(data_file) 
	X_train, X_test, y_train, y_test = df_transform(df)