import urllib2
import sys
import re


def getPage(url,offset = '295'):
    realurl = "%s%s%s" %(url,offset,'.html')
    print realurl
    resp = urllib2.urlopen(realurl)
    content = resp.read()
    
    p = re.compile('<[^>]+>')
    
    #print content
    rematch = re.compile(r'(<h1.*</h1>)')
    h1 = rematch.findall(content)
    try:
        h1content = p.sub("",h1[0])
    except Exception,e:
        print str(e)
        return
    fp = open(r'renxingruanjian.txt','a')
    fp.write(h1content+ '\n')
    fp.flush()
    
    #print content
    content = content.replace('\r','')
    content = content.replace('\n','')
    content = content.replace(' ','')
    content = content.replace('     ','')
    #fp.write(content+'\n')
    cont = re.search('<divclass="txtC"id="txtBg">(.*)</p></div><divclass="boxA">', content, re.S)
    words = cont.group()
    p = re.compile('<[^>]+>')
    contTxt = p.sub("", words)
    #print recontent1
    
    fp.write(contTxt+'\n')
    fp.flush()
    fp.close()


def getBook(url, startoffset, endOffset):
    while startOffset < endOffset:
        getPage(offset = str(startOffset))
        startOffset += 1

if __name__ == '__main__':
    getBook(url = 'http://lz.book.sohu.com/chapter-21882-117887', startOffset = 294, endOffset = 395)