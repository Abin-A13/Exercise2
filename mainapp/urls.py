from .views import BookView
from rest_framework import routers
from authapp.views import UserView


router = routers.DefaultRouter()
router.register('books',BookView,basename="books/")
router.register('users',UserView,basename="Users/")

