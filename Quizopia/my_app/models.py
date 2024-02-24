from django.db import models

# Create your models here.

class User_info(models.Model):
    username= models.CharField(max_length =50 )
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length =10)


class Quiz(models.Model):
    quiz_name=models.CharField(max_length=50)
    username=models.ForeignKey(User_info, on_delete=models.CASCADE)
    quiz_code=models.CharField(max_length=50)
    total_marks=models.IntegerField()
    description=models.TextField()

class Quetions(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    que=models.CharField(max_length=1000)
    op1 = models.CharField(max_length=100)
    op2 = models.CharField(max_length=100)
    op3 = models.CharField(max_length=100)
    op4 = models.CharField(max_length=100)
    ans = models.CharField(max_length=100)

class Participants(models.Model):
    username=models.ForeignKey(User_info, on_delete=models.CASCADE)
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default = 0 )
    
    

