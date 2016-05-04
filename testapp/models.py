from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=20)
	tag_line = models.CharField(max_length=140)
	description = models.TextField()

	def __str__(self):
		return self.titles

class Input(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	title = models.CharField(max_length=20)
	content = models.CharField(max_length=140)

	def __str__(self):
		return self.title

class Output(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	title = models.CharField(max_length=20)
	content = models.CharField(max_length=140)

	def __str__(self):
		return self.title
