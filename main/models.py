from django.db import models

class Category(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title

class Work(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=221)
    url = models.URLField(max_length=221)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Teacher(models.Model):
    name = models.CharField(max_length=221)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to="teacher_image/")
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField()
    subject = models.CharField(max_length=221)
    text = models.TextField()

class Article(models.Model):
    image = models.ImageField(upload_to="article_images")
    title = models.CharField(max_length=221)
    description = models.TextField()
    tag = models.ManyToManyField(Tag)
    view = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    image = models.ImageField(upload_to="author_image", null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name="comments")
    author_name = models.CharField(max_length=221)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Email(models.Model):
    mail = models.EmailField()
