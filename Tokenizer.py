import nltk
import re
import json
from dicttoxml import dicttoxml
from Settings import *


with open(TEST_CORPUS, "r") as f:
    text_list = [line for line in f]
    text = ''.join(text_list)
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens, lang='rus')

result = []
for par in text.split("\n"):
    par_data = {"Paragraph": par, "sentences": []}
    result.append(par_data)
    for sent in re.split(PATTERN, par):
        sent_data = {"sentence": sent, "tokens": [{"value": v[0], "type": v[1], "ID": number} for number, v in enumerate(nltk.pos_tag(nltk.word_tokenize(sent), lang='rus'))]}
        par_data["sentences"].append(sent_data)


my_xml = dicttoxml(result, attr_type=False)

with open(XML_FILE, "w", encoding="UTF-8") as file:
    file.write(my_xml.decode("UTF-8"))

print(my_xml.decode("UTF-8"))
print(json.dumps(result, ensure_ascii=False))

# test_list = []
# for word in tokens:
#     test_list.append(word)
#     try:
#         test_list.append(morph.parse(word)[0].normal_form)
#     except AttributeError:
#         pass
# print(test_list)





