import pandas as pd

train_path = 'data/train.csv'
test_path = 'data/test.csv'

training_data = pd.read_csv(train_path)
test_data = pd.read_csv(test_path)
test_data = test_data.drop('is_fraud', axis=1)
test_data = pd.merge(test_data, training_data, on='Id', how='left')
# drop is_fraud is NaN
training_data = training_data.dropna(subset=['is_fraud'])

training_data_X = training_data.drop(['is_fraud'], axis=1)
training_data_Y = training_data['is_fraud']
test_data_X = test_data.drop(['is_fraud'], axis=1)

# write to file
training_data_X.to_csv('training_data_X.csv', index=False)
training_data_Y.to_csv('training_data_Y.csv', index=False)
test_data_X.to_csv('test_data_X.csv', index=False)

