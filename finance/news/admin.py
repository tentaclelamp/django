from django.contrib import admin

# Register your models here.
class Artcile(object):
	"""docstring for ClassName"""
	def __init__(self, Tittle):
		super(Artcile, self).__init__()
		self.Tittle = Tittle

