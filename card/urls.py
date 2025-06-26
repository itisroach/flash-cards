from django.urls import path
from card.views import (
    CreateCardView,
    UpdateCardView,
    DeleteCardView,
    GetUserCardsView,
)


urlpatterns = [
    path("card/", CreateCardView.as_view(), name="create_card"),
    path("card/list/", GetUserCardsView.as_view(), name="get_card"),
    path("card/update/<id>/", UpdateCardView.as_view(), name="update_card"),
    path("card/delete/<id>/", DeleteCardView.as_view(), name="delete_card"),
]