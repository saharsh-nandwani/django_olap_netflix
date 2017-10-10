from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


from. serializers import popularPlanSerializer,trendingMoviesSerializer,languageCountrySerializer
from. models import popularPlan,trendingMovies,languageCountry

class popularPlanViewSet (ModelViewSet):
    serializer_class = popularPlanSerializer
    queryset = popularPlan.objects.all()

class trendingMoviesViewSet (ModelViewSet):
    serializer_class = trendingMoviesSerializer
    queryset = trendingMovies.objects.all()

class languageCountryViewSet (ModelViewSet):
    serializer_class = languageCountrySerializer
    queryset = languageCountry.objects.all()
