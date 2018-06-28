print(__doc__)

import pickle

import pandas as pd
from sklearn import linear_model

def read_csv(path):
    return pd.read_csv("../resources/" + path, sep=',')


def save_to_file(data, file_name):
    df = pd.DataFrame(data)
    df.to_csv("../resources/" + file_name, sep=',', encoding='utf-8')


# Load the dataset


resumes = read_csv('resume_data.csv').values

# Split the data into training/testing sets
resumes_X_train = resumes[:, 2:]
resumes_X_test = resumes_X_train

# Split the targets into training/testing sets
resumes_y_train = resumes[:, 1]
resumes_y_test = resumes_y_train

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(resumes_X_train, resumes_y_train)


# save the model to disk
filename = '../model/finalized_model.sav'
pickle.dump(regr, open(filename, 'wb'))


# # Plot outputs
# plt.scatter(resumes_X_test, resumes_y_test, color='black')
# plt.plot(resumes_X_test, resumes_y_pred, color='blue', linewidth=3)
#
# plt.xticks(())
# plt.yticks(())
#
# plt.show()
