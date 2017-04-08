import urllib.request
import re
import csv


response = urllib.request.urlopen('http://www.codeabbey.com/index/user_ranking')
charset = response.info().get_content_charset()
if charset is not None:
    html = str(response.read(), encoding=str(charset))
else:
    html = str(response.read())
# read table header
pattern_th = re.compile(r'[<!--]*?\s <th.*?>([#|\w]*).*?</th>')
find_th = re.findall(pattern_th, html)
# read table content
pattern_td = re.compile(r'[<!--]*?\s <td.*?>(\b\w+/*\w?#?\+?\+?,?\s?\w*\.?\w*)')
find_td = re.findall(pattern_td, html)[2:]
# form resulting list
len_of_header = len(find_th)
alist = [find_td[i:i + len_of_header] for i in range(0, len(find_td), len_of_header)]
alist.insert(0, find_th)
# write data to csv file
output_file = open('user_ranking_codeabbey.csv', 'w', newline='')
wrtr = csv.writer(output_file, quoting=csv.QUOTE_MINIMAL)
for row in alist:
    wrtr.writerow(row)
output_file.close()
