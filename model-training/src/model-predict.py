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
import glob
import os
import csv
import re

# get file names from command prompt
keywords_file_name = "../resources/keywords.txt"
csv_file = "../resources/predict_resume_data.csv"

absolute_dir = "/Users/yixuanchen/go-candidate/model-training/resources/resumes-to-predict"
relative_dir = "../resources/resumes-to-predict"

# digest input data from web

def count_matching_keywords(keywords, resume_words):
    match_count = []
    resume_words = [x.lower() for x in resume_words]
    keywords = [x.lower() for x in keywords]
    for i in range(len(keywords)):
        match_count.append(resume_words.count(keywords[i]))
    return match_count


# MAIN FUNCTION
# def preprocess(absolute_dir):
# read keywords from a file into a list
with open(keywords_file_name) as keywords_file:
    keywords = keywords_file.read()
keywords = keywords.split()

# create csv file to store data
csv_file_obj = open(csv_file, 'w')
csv_writer = csv.writer(csv_file_obj, delimiter=',')
row = ["Index"]
for i in range(len(keywords)):
    row.append("Keyword" + str(i + 1))
csv_writer.writerow(row)

index = 1
for resume in os.listdir(absolute_dir):
    #if resume
    with open(os.path.join(absolute_dir,resume)) as resume_file:
        # store words in resume as a list
        resume_words = resume_file.read()
        resume_words = re.findall(r"[\w']+", resume_words)
        # score = re.search('(?<=-)\s?\d+', resume)
        # score = score.group(0).strip()
        # print(str(resume) + " " + score)
        # find number of occurences of keywords in the resume
        key_match_count = count_matching_keywords(keywords, resume_words)
        # resume_list.append({'file_name': str(resume), 'word_list': resume_words, 'score' : score, 'keywords_match_count': key_match_count})
        csv_writer.writerow([index] + key_match_count)
    index += 1

csv_file_obj.close()
print('Done.')
# return

# filename = "../model/finalized_model.sav"
# load the model from disk
# loaded_model = pickle.load(open(filename, 'rb'))

# y = loaded_model.predict(input)

# print(y)
