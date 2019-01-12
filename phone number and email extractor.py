import pyperclip
import re

phoneRegEx = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.verbose)


emailRegEx = re.compile(r'''
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z](2,4))
''', re.verbose)

phone = re.compile('''(
text = str(pyperclip.paste())
matches = []
for groups in phoneRegEx.findall(text):
    phonenumb = '-'.join(groups[1], groups[3], groups[5]
    if group[8] != '':
        phonenumb += ' x' + group[8]
    matches.append(phonenumb)
for groups in emailRegEx.findall(text):
    matches.append(groups[0])
)''')

for groups in emailRegEx.findall(text):
    matches.append(groups[0])
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')