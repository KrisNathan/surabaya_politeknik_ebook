import re
import os

os.system(f'wget https://nscpolteksby.ac.id/ebook/book/computer-engineering/')

with open("index.html", "r") as f:
    title = ""
    for line in f:
        title_search = re.search(r'(?<=href=\"#\">).*(?=<b>)', line)
        pdf_search = re.search(r"(?<=href=\")files\/Ebook\/.*\.pdf(?=\")", line)
        if title_search:
            sstring = title_search.group()
            print(sstring)
            title = sstring.rstrip()

        if pdf_search:
            sstring_p = pdf_search.group()
            url = re.sub(r'files\/', 'https://nscpolteksby.ac.id/ebook/files/', sstring_p)
            print(url)
            os.system(f'wget -P "files/{title}" "{url}"')
