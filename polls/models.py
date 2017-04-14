from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length = 140)
    #body = models.TextField()
    date = models.DateTimeField('date published')
   # def was_published_recently(self):
       # return

    def __unicode__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.choice_text
