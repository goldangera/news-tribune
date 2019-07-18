from django.db import models
import datetime as dt 
# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    #phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name  
    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/')
    
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news
    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news