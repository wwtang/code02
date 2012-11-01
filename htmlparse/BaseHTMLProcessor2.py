from sgmllib import SGMLParser
import htmlentitydefs

class BaseHTMLProcessor(SGMLParser):
	def reset(self):
		# extend (called by SGMLParser.__init__)
		self.pieces = []
		SGMLParser.reset(self)
		
	def unknown_starttag(self, tag, attrs):
		# called for each start tag
		# attrs is a list of (attr, value) tuples
		# e.g. for <pre class="screen">, tag="pre", attrs=[("class", "screen")]
		# Ideally we would like to reconstruct original tag and attributes, but
		# we may end up quoting attribute values that weren't quoted in the source
		# document, or we may change the type of quotes around the attribute value
		# (single to double quotes).
		# Note that improperly embedded non-HTML code (like client-side Javascript)
		# may be parsed incorrectly by the ancestor, causing runtime script errors.
		# All non-HTML code must be enclosed in HTML comment tags (<!-- code -->)
		# to ensure that it will pass through this parser unaltered (in handle_comment).
		strattrs = "".join([' %s="%s"' % (key, value) for key, value in attrs])
		self.pieces.append("<%(tag)s%(strattrs)s>" % locals())
		
	def unknown_endtag(self, tag):
		# called for each end tag, e.g. for </pre>, tag will be "pre"
		# Reconstruct the original end tag.
		self.pieces.append("</%(tag)s>" % locals())
	def output(self):
		"""Return processed HTML as a single string"""
		return "".join(self.pieces)