from django.forms import ModelForm
from models import Format

class FormatForm(ModelForm):
	class Meta:
		model=Format
		fields=['username','title_of_paper','co_authors','journal','volume','year','impact_factor','file']