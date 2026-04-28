from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    skills = models.TextField()
    experience = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.name