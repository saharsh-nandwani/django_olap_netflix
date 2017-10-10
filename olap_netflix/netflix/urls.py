from rest_framework.routers import SimpleRouter
from. views import popularPlanViewSet,trendingMoviesViewSet,languageCountryViewSet

router= SimpleRouter()
router.register("popularPlan",popularPlanViewSet)
router.register("trendingMovies",trendingMoviesViewSet)
router.register("languageCountry",languageCountryViewSet)

urlpatterns = router.urls
