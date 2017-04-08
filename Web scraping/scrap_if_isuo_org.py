import urllib.request
import re
import html
import csv

output_file = open('schools_Ivano-Frankivsk.csv', 'w',  newline='')
wrtr = csv.writer(output_file,  quotechar=' ', quoting=csv.QUOTE_MINIMAL)
# CSV header
header = ['#', 'School name', 'Phone', 'E-mail']
# write header
wrtr.writerow(header)

response = urllib.request.urlopen('https://if.isuo.org/koatuu/schools-list/id/2610100000')
charset = response.info().get_content_charset()
if charset is not None:
    html_resp = str(response.read(), encoding=str(charset))
else:
    html_resp = str(response.read())

# Get list of school's urls
pattern_list_of_urls = re.compile(r'<a href="/schools/view/id/(\d+).*?')
find_hrefs = re.findall(pattern_list_of_urls, html_resp)
url_mask = 'https://if.isuo.org/schools/view/id/'
urls = []
for i in range(len(find_hrefs)):
    urls.append(url_mask + str(find_hrefs[i]))

i = 1
# Get information about each school from urls
for url in urls:
    res = urllib.request.urlopen(url)
    html_res = str(res.read(), encoding=str(charset))
    # Regex patterns:
    pattern_school_name = re.compile(r'[\n]?<td>([^\d][-\w &;№]+)?[^\d][\\\n\r]?[\n]?([-\w\s&;]+)?[<]?')
    pattern_school_phone = re.compile(r'Телефони:</th>[ \n]*<td>([()\d-]*[\d]{2}[-]?[\d]{2})')
    pattern_school_mail = re.compile(r'unescape\(\'(.*)?\'')
    pattern_email = re.compile(r'mailto:["\']?([\w.\-@\w]+)["\']?')
    # Search
    # School name
    find_school_name = re.search(pattern_school_name, html_res)
    school_name = ''
    for gr in find_school_name.groups():
        if gr is not None:
            school_name = school_name + ' ' + str(gr).strip()
    school_name = html.unescape(school_name)
    # School phone number
    find_school_phone = re.findall(pattern_school_phone, html_res)
    if len(find_school_phone):
        find_school_phone = find_school_phone[0]
    else:
        find_school_phone = ''
    # School e-mail
    find_school_mail = re.findall(pattern_school_mail, html_res)
    if len(find_school_mail):
        email = ''.join([chr((int(i, 16))) for i in find_school_mail[0].replace('%', ' 0x').split()])
        find_emails = re.findall(pattern_email, email)[0]
    else:
        find_emails = ''
    # Form resulting data row
    row = [str(i), school_name.strip(), find_school_phone, find_emails]
    i += 1
    # write row to CSV file
    wrtr.writerow(row)

output_file.close()
