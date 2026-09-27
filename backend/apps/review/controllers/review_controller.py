from django.utils import timezone
from ..models import Review, ReviewImage
from ..services.tensorflow_service import analyze_sentiment

def create_review(user_id, product_id, review_text, rating, image_file=None):
    # Simpan review
    review = Review.objects.create(
        user_id=user_id,
        product_id=product_id,
        review_text=review_text,
        rating=rating,
        created_at=timezone.now()
    )

    # Simpan gambar jika ada
    if image_file:
        ReviewImage.objects.create(
            review=review,
            image_url=image_file,
            uploaded_at=timezone.now()
        )

    # Analisis sentiment dengan TensorFlow
    sentiment_result = analyze_sentiment(review)

    return {
        "review_id": str(review.review_id),
        "sentiment": sentiment_result
    }
