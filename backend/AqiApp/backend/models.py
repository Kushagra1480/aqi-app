from django.db import models

# Create your models here.

class BaseModel(models.Model):
    #these two keep track of when a record is created and updated, useful in auditing
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        #this sets the class as an abstract class, making this the template for the classes that follow
        #marking this as abstract also ensures that this doesn't become an actual table in database
        abstract = True

class Location(BaseModel):
    name = models.CharField(max_length=255)
    coordinates = models.PointField()
    
    def __str__(self):
        return self.name