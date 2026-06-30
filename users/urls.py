from django.urls import path
from users.apis import ListCreateUserAPIView, RetrieveUpdateDestroyUserAPIView


urlpatterns = [
    path(
        route="list-create/",
        view=ListCreateUserAPIView.as_view(),
    ),
    path(
        route="user-detail<int:user_id>/",
        view=RetrieveUpdateDestroyUserAPIView.as_view(),
    ),
]
