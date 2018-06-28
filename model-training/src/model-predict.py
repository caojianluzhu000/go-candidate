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


filename = "../model/finalized_model.sav"
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

loaded_model.predict()

result = loaded_model.score(X_test, Y_test)