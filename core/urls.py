from django.urls import path

from core.views import editMember, listOfMembers, addMember

app_name = "core"
urlpatterns = [
    path("", listOfMembers, name="list-of-members"),
    path(
        "edit/<int:currentKey>/",
        editMember,
        name="edit-member",
    ),
    path("add/", addMember, name="add-member"),
]
