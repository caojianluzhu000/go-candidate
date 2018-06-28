# # Make predictions using the testing set
# resumes_y_pred = regr.predict(resumes_X_test)
#
# data_size = len(resumes_X_train)
# data = np.concatenate((resumes_X_train, resumes_y_train.reshape(data_size,1)), axis=1)
# save_to_file(data, "predict-result.txt")
#
# # The coefficients
# print('Coefficients: \n', regr.coef_)
# save_to_file(regr.coef_, "coefficients.txt")
#
import pickle
import resume_preprocessing

filename = "../model/finalized_model.sav"
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

input = resume_preprocessing.preprocess("../resources/resumes-to-predict")

y = loaded_model.predict(input)

print(y)