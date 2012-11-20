"""
this is the example from python oop 3
"""

class ContactList(list):
	def search(self, name):
		"""
		return all contacts that
		contain the search value 
		in their name.
		"""
		matching_contacts = []
		for contact in self:
			if name in contact.name:
				matching_contacts.append(contact)	
		return matching_contacts	


class Contact:
	all_contacts = ContactList()

	def __init__(self,name,email):
		self.name = name
		self.email = email
		Contact.all_contacts.append(self)


class Supplier(Contact):
	def order(self,order):
		print("If this were a real system we could send"
			"{} order to {}".format(order, self.name))


class LongNameDict(dict):
	def longest_key(self):
		longest = None
		for key in self:
			if not longest or len(key) > len(longest):
				longest = key
		return longest


class Friend(Contact):
	def __init__(self, name, email, phone):
		super().__init__(name, email)
		self.phone = phone
		
