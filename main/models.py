from django.db import models
from datetime import datetime
# models.py is how you communicate to the database
#we write models.Model in classmparameters because it 
#inherits from the base model of django and we are extending it 



# a class in models maps to a table in the database through django ORM

class TutorialCategory(models.Model):
    category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length = 200)
    category_slug = models.CharField(max_length=200, default=1) #url for category

    class Meta:
         # Gives the proper plural name for admin
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.category

class TutorialSeries(models.Model):
    
    series = models.CharField(max_length=200)
    tutorialcategory  = models.ForeignKey(TutorialCategory, default = 1, 
                                    on_delete = models.SET_DEFAULT,verbose_name ="Category")
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
            return self.series

class Tutorial(models.Model):
    tutorials_title = models.CharField(max_length=200)
    tutorials_content = models.TextField()
    
    tutorials_published = models.DateTimeField("Date Published", default= datetime.now())
    tutorialseries =  models.ForeignKey(TutorialSeries, default = 1, 
                                    on_delete = models.SET_DEFAULT,verbose_name ="series")
    tutorials_slug = models.CharField(max_length=200, default=1)
   
    def __str__(self): #overriding the string method, helps in printing out the object
        return self.tutorials_title


