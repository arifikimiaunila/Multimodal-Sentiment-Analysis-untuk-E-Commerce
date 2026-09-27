import tensorflow as tf
import numpy as np
from ..controllers.sentiment_controller import save_sentiment

# Load model sekali saat startup
model = tf.keras.models.load_model("models/sentiment_model")

def analyze_sentiment(review):
    # Dummy preprocessing (ganti dengan pipeline BERT + CNN)
    text_embedding = np.random.rand(1, 768)  # contoh dummy
    image_array = np.random.rand(1, 224, 224, 3)  # contoh dummy

    prediction = model.predict([text_embedding, image_array])
    sentiment_label = np.argmax(prediction, axis=1)[0]

    labels = ["negative", "neutral", "positive"]
    fusion_sentiment = labels[sentiment_label]

    confidence_score = float(np.max(prediction))

    # Simpan hasil ke DB
    analysis = save_sentiment(review, fusion_sentiment, confidence_score)

    return {
        "fusion_sentiment": fusion_sentiment,
        "confidence_score": confidence_score
    }
