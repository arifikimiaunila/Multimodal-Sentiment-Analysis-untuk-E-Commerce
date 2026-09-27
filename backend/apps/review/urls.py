from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .controllers.review_controller import create_review

@api_view(["POST"])
def review_endpoint(request):
    user_id = request.data.get("user_id")
    product_id = request.data.get("product_id")
    review_text = request.data.get("review_text")
    rating = request.data.get("rating")
    image_file = request.FILES.get("image")

    result = create_review(user_id, product_id, review_text, rating, image_file)
    return Response(result)

urlpatterns = [
    path("reviews/", review_endpoint, name="create_review"),
]
