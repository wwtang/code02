from sgmllib import SGMLParser
import htmlentitydefs

class BaseHTMLProcessor(SGMLParser):
    def reser(self):
        self.pieces = []
        SGMLParser.reset(self)
        

    def unknown_starttag(self, tag, attrs):
        #attrs
        strattrs = "".join(['%s="%s"'%(key, value)for key, value in attrs])
        self.pieces.append("<%(tag)s%(strattrs)s>" %locals())
        
#####################################################################
#class BaseHTMLProcessor(SGMLParser):
#	def reset(self):
#		# extend (called by SGMLParser.__init__)
#		self.pieces = []
#		SGMLParser.reset(self)
#		
#	def unknown_starttag(self, tag, attrs):		
#		
#		strattrs = "".join([' %s="%s"' % (key, value) for key, value in attrs])
#		self.pieces.append("<%(tag)s%(strattrs)s>" % locals())
#####################################################################
    def unknown_endtag(self, tag):
        self.pieces.append("</%(tag)s>"%locals())

if __name__ == "__main__":
	for k, v in globals().items():
		print k, "=", v