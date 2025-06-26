from django.urls import path
from card.views import (
    CreateCardView,
    UpdateCardView,
    DeleteCardView,
    GetUserCardsView,
    GetSingleCardView
)


urlpatterns = [
    path("card/", CreateCardView.as_view(), name="create_card"),
    path("card/list/", GetUserCardsView.as_view(), name="get_card_list"),
    path("card/update/<card_id>/", UpdateCardView.as_view(), name="update_card"),
    path("card/delete/<card_id>/", DeleteCardView.as_view(), name="delete_card"),
    path("card/<card_id>/", GetSingleCardView.as_view(), name="get_card")
]