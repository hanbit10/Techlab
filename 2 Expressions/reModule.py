import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

# This search only letter s
pattern = re.compile(r'\s')
text_to_search
# Serach words
pattern = re.compile(r'\bHa')
pattern = re.compile(r'\BHa')

#search for beginning word
pattern = re.compile(r'^Start')
pattern = re.compile(r'end$')
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
pattern = re.compile(r'[1-5a-zA-Z]')

#everything that is not in the set
pattern = re.compile(r'[^1-5a-zA-Z]')
pattern = re.compile(r'[^b]at')
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

matches = pattern.finditer(text_to_search)

for matching in matches:
  print(matching)
# matches = pattern.search(sentence)

with open('data.txt', 'r', encoding='utf-8') as f:
  contents = f.read()

  matches = pattern.finditer(contents)

  # for matching in matches:
  #   print(matching)
