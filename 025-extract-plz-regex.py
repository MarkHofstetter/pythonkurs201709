import re

a = 'Schulgasse 234; 1090 gars am kamp, Stiege 27'
# a = 'Schulgasse 234; 1090 gars am kamp'

# data = re.search(r'(.*); (\d{4})', a)

data = re.search(r'(\d{4})', a)
# print(data[0])
print(data[1])
# print(data[2])