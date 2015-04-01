from django.db import models

def get_upload_file_name(instance,filename):
	return "uploaded_files/%s" %(filename)

class Format(models.Model):
	title_of_paper=models.CharField(max_length=40)
	co_authors=models.CharField(max_length=40)
	journal=models.CharField(max_length=40)
	volume=models.IntegerField()
	year=models.IntegerField()
	impact_factor=models.FloatField()	
	file=models.FileField(upload_to=get_upload_file_name)
	username=models.CharField(max_length=40)
	
	def __unicode__(self):
		return self.title_of_paper
