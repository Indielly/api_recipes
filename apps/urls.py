from rest_framework.routers import DefaultRouter

from apps.chief.views import ChiefViewSet
from apps.recipe.views import RecipeViewSet

router = DefaultRouter()
router.register(r"chiefs", ChiefViewSet)
router.register(r"recipes", RecipeViewSet)

urlpatterns = router.urls
