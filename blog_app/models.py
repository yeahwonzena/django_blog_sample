from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=255, default='전체')
    publish = models.CharField(max_length=1, default='Y')
    views = models.IntegerField(default=0)
    author_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # '..' 문자열이 포함된 content 필드를 변경
        self.content = self.content.replace('"..', '"')
        super().save(*args, **kwargs)



class ImageId(models.Model):
    pass

class TitleImageId(models.Model):
    pass


