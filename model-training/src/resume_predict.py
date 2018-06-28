import glob
import os
import csv
import re

# get file names from command prompt
keywords_file_name = "../resources/keywords.txt"
csv_file = "../resources/predict_resume_data.csv"


# class resume_preprocessing:
# HELPER FUNCTION
# returns an array with the number of times a keyword is found in resume_words


def count_matching_keywords(keywords, resume_words):
    match_count = []
    resume_words = [x.lower() for x in resume_words]
    keywords = [x.lower() for x in keywords]
    for i in range(len(keywords)):
        match_count.append(resume_words.count(keywords[i]))
    return match_count


# MAIN FUNCTION
resume_directory="../resources/resumes-to-predict"
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
for resume in glob.glob(os.path.join(resume_directory, '*txt')):
    with open(resume) as resume_file:
        # store words in resume as a list
        resume_words = resume_file.read()
        resume_words = re.findall(r"[\w']+", resume_words)
        # score = re.search('(?<=_)\d+', resume)
        # score = score.group(0)
        # find number of occurences of keywords in the resume
        key_match_count = count_matching_keywords(keywords, resume_words)
        # resume_list.append({'file_name': str(resume), 'word_list': resume_words, 'score' : score, 'keywords_match_count': key_match_count})
        candidate = resume.split('/')
        candidate = candidate[len(candidate)-1]
        csv_writer.writerow([index] + [candidate] + key_match_count)
    index += 1

csv_file_obj.close()
print('Done.')



import pickle
import pandas as pd

file_name = "/Users/yixuanchen/go-candidate/model-training/resources/predict_resume_data.csv"

model_file = "/Users/yixuanchen/go-candidate/model-training/model/finalized_model.sav"
loaded_model = pickle.load(open(model_file, 'rb'))

data = pd.read_csv(file_name, sep=',').values
data_to_predict = data[:, 1:]
predit = loaded_model.predict(data_to_predict)

index = 0
for candidate in data:
    print(candidate[0] + "," + str(predit[index]))
    index+1

