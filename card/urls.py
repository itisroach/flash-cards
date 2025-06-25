from django.urls import path
from card.views import CreateCardView


urlpatterns = [
    path("card/", CreateCardView.as_view(), name="create_card"),
]