from django.db import models


class Contact(models.Model):
	groups = (
		('Family', 'Family'),
		('Friends', 'Friends'),
		('Co-Workers', 'Co-Workers'),
		('other', 'other'),
	)

	picture = models.ImageField(null=False, blank=True)
	firstName = models.CharField(max_length=100, null=False, blank=False)
	lastName = models.CharField(max_length=100, blank=True)
	nickName = models.CharField(max_length=100, blank=True)
	phone = models.CharField(max_length=15, null=False, blank=False)
	email = models.EmailField(blank=True)
	groups = models.CharField(
		max_length=100,
		choices=groups,
		blank=True
	)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		if self.nickName == '' or None:
			return f'{self.firstName} {self.lastName}'
		return f'{self.firstName} {self.lastName} ({self.nickName})'

	class Meta:
		ordering = ['firstName']
