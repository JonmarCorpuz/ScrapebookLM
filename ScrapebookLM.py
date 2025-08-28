# Requirements
#!pip install requests-html requests

# Import Libraries
import requests
from requests_html import HTML

# 
base_url = "https://stackoverflow.com/questions/tagged/"
tag = "python"
query_filter = "Votes"
url = f"{base_url}{tag}"

#
r = requests.get(url)
html_string = r.text

#
html = HTML(html=html_string)

#
question_summaries = html.find(".question-summary") # selenium
#print(question_summaries.text)
#print(question_summaries[0].text)

#
columns = [ "vote", "vote_title", "num_answers", "views", "question", "short_description", "tags", "date", "user", "user_details" ]

#
this_row = list(question_summaries[0].text.split("\n"))
print(this_row)

#
len(this_row) == len(columns)

# 
row_data = dict(zip(columns, this_row))
print(row_data)

# 
for column, row_v in zip(columns, this_row):
  print(column, row_v)

# 
key_names = ["question", "votes"]
classes_needed = [".question-hyperlink"]
this_question_element = question_summaries[0]
this_question_element.find(".question-hyperlink", first=True).text
#this_question_element.find(".vote", first=True).text.replace("\nvotes", "")

#
datas = []

for q_el in question_summaries:
  question_data = {}
  for _class in enumerate(classes_needed):
    sub_el = q_el.find(_class, first=True)
    #print(sub_el.text)
    keyname = key_names[i]
    question_data[keyname] = sub_el.tet
  datas.append(question_data)

datas[0]
