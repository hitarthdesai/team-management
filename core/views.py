from django.shortcuts import render

from .models import Member


def listOfMembers(request):
    if request.method == "POST":
        ID = Member.objects.all().count() + 1
        FIRST_NAME = request.POST["firstName"]
        LAST_NAME = request.POST["lastName"]
        EMAIL = request.POST["email"]
        PHONE = request.POST["phoneNumber"]
        IS_ADMIN = request.POST["isAdmin"] == "yes"
        if request.POST.get("addButton"):
            doesMemberExist = Member.objects.all().filter(
                firstName=FIRST_NAME, lastName=LAST_NAME, email=EMAIL
            )
            if doesMemberExist.exists():
                pass
            else:
                newMember = Member(
                    id=ID,
                    firstName=FIRST_NAME,
                    lastName=LAST_NAME,
                    email=EMAIL,
                    phone=PHONE,
                    isAdmin=IS_ADMIN,
                )
                newMember.save()

        elif request.POST.get("updateButton"):
            memberToBeEdited = Member.objects.all().filter(id=request.POST["identity"])
            memberToBeEdited.update(firstName=FIRST_NAME)
            memberToBeEdited.update(lastName=LAST_NAME)
            memberToBeEdited.update(email=EMAIL)
            memberToBeEdited.update(phone=PHONE)
            memberToBeEdited.update(isAdmin=IS_ADMIN)

        elif request.POST.get("deleteButton"):
            memberToBeDeleted = Member.objects.all().filter(id=request.POST["identity"])
            memberToBeDeleted.delete()

    context = {"members": Member.objects.all()}
    return render(request, "listOfMembers.html", context)


def addMember(request):
    return render(request, "addMember.html")


def editMember(request, currentKey):
    context = {"currentMember": Member.objects.all().filter(id=currentKey)}
    return render(request, "editMember.html", context)
