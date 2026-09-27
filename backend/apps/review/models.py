from django.db import models
import uuid

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class ReviewImage(models.Model):
    image_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class SentimentAnalysis(models.Model):
    analysis_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    review = models.OneToOneField(Review, on_delete=models.CASCADE)
    text_sentiment = models.CharField(max_length=20)
    image_sentiment = models.CharField(max_length=20)
    fusion_sentiment = models.CharField(max_length=20)
    confidence_score = models.FloatField()
    analyzed_at = models.DateTimeField(auto_now_add=True)

class ModelLog(models.Model):
    log_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    analysis = models.ForeignKey(SentimentAnalysis, on_delete=models.CASCADE)
    model_used = models.CharField(max_length=50)
    execution_time = models.FloatField()
    status = models.CharField(max_length=20)
