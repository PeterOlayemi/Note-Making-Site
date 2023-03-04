from django.db import models
from account.models import User

# Create your models here.

STATUS=(
    (0, 'DRAFT'),
    (1, 'PUBLISH'),
)

class Note(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    topic=models.CharField(max_length=100, unique=True)
    entry=models.TextField(help_text="Enter Note's Entry")
    status=models.IntegerField(choices=STATUS, default=1, help_text='Select Either Draft or Publish')
    date=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic