import re
import os
import urllib
import sys

def read_url(filename):
  
    underbar = filename.index("_")
    host = filename[underbar + 1:]

    url_dict = {}

    f = open(filename)
    for line in f:
        match = re.search(r'"GET (\S+)', line)

        if match:
            path = match.group(1)

            if "puzzle" in path:
                url_dict["http://" + host + path] = 1
    return url_dict

def url_sort_key(url):
    """Used to order the urls in increasing order by 2nd word if present."""
    match = re.search(r'-(\w+)-(\w+)\.\w+', url)
    if match:
      return match.group(2)
    else:
        return url

def download_images(img_urls, dest_dir):
 
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    index = file(os.path.join(dest_dir, 'index.html'), 'w')
    index.write('<html><body>\n')

    i = 0
    for img_url in img_urls:
        local_name = 'img%d' % i
        print 'Retrieving...', img_url
        urllib.urlretrieve(img_url, os.path.join(dest_dir, local_name))

        index.write('<img src="%s">' % (local_name,))
        i += 1

    index.write('\n</body></html>\n')
    index.close()
