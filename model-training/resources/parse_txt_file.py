import glob
import os
import csv
import re

# get file names from command prompt
keywords_file_name = raw_input("Keywords file name: ")
resume_directory = raw_input("Resume directory: ")
csv_file = raw_input("CSV file name to store data: ")

# returns an array with the number of times a keyword is found in resume_words
def count_matching_keywords(keywords, resume_words):
	match_count = []
	for i in range(len(keywords)):
		match_count.append(resume_words.count(keywords[i]))	
	return match_count



# read keywords from a file into a list
with open(keywords_file_name) as keywords_file:
	keywords = keywords_file.read()
keywords = keywords.split()


# create csv file to store data
csv_file_obj= open(csv_file, 'wb')
csv_writer=csv.writer(csv_file_obj, delimiter=',')
row=["Index", "Score"]
for i in range(len(keywords)):
	row.append("Keyword" + str(i+1)) 
csv_writer.writerow(row)

index = 1
for resume in glob.glob(os.path.join(resume_directory, '*txt')):
	with open(resume) as resume_file:
		# store words in resume as a list
		resume_words = resume_file.read()
		resume_words = resume_words.split()
		score = re.search('(?<=-)\s?\d+', resume)
		score = score.group(0).strip()
		print(str(resume) + " " + score)
		# find number of occurences of keywords in the resume
		key_match_count = count_matching_keywords(keywords, resume_words)
		#resume_list.append({'file_name': str(resume), 'word_list': resume_words, 'score' : score, 'keywords_match_count': key_match_count})
		csv_writer.writerow([index] + [score] + key_match_count)
	index+=1
		
		
csv_file_obj.close()
print('Done.')


		
		
	




	

