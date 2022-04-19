from django.db import models
from django.utils import timezone
# Create your models here.
class Faq(models.Model):
    #질문, 카테고리, 답변, 생성자, 생성일시, 최종 수정자, 최종 수정일
    question = models.CharField(max_length=50)
    faq_choices = [
        (NORMOL, '일반'),
        (ACCOUNT,'계정'),
        (ETC, '기타'),
        ]
    category = models.CharField(max_length=3, choices=faq_choices, default=NORMOL)
    answer = models.TextField()
    creater = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_auther = models.CharField(max_length=50)
    updated_at = models.DateTimeField(blank=True, null=True)

    def edit(self):
        self.edit_auther = models.CharField(max_length=50)
        self.edit_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.question
    