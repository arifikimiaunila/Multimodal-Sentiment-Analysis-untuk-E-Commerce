from rest_framework import serializers
from .models import User, Product, Review, ReviewImage, SentimentAnalysis, ModelLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id", "name", "email", "created_at"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product_id", "name", "category", "price", "created_at"]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["review_id", "user_id", "product_id", "review_text", "rating", "created_at"]

class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ["image_id", "review_id", "image_url", "uploaded_at"]

class SentimentAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentimentAnalysis
        fields = ["analysis_id", "review_id", "text_sentiment", "image_sentiment", "fusion_sentiment", "confidence_score", "analyzed_at"]

class ModelLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelLog
        fields = ["log_id", "analysis_id", "model_used", "execution_time", "status"]
