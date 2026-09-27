from django.utils import timezone
from ..models import SentimentAnalysis, ModelLog

def save_sentiment(review, fusion_sentiment, confidence_score, text_sentiment="neutral", image_sentiment="good"):
    analysis = SentimentAnalysis.objects.create(
        review=review,
        text_sentiment=text_sentiment,
        image_sentiment=image_sentiment,
        fusion_sentiment=fusion_sentiment,
        confidence_score=confidence_score,
        analyzed_at=timezone.now()
    )

    ModelLog.objects.create(
        analysis=analysis,
        model_used="FusionNet",
        execution_time=0.123,  # placeholder
        status="success"
    )

    return analysis
