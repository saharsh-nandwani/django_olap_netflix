from rest_framework import serializers
from .models import popularPlan,trendingMovies,languageCountry

class popularPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = popularPlan
        fields = ('user_id', 'plan_name', 'plan_id')

class trendingMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = trendingMovies
        fields = ('count','rating','movie_id')

class languageCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = languageCountry
        fields = ('user_country','language_id')
