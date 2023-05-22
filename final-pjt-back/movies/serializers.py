from rest_framework import serializers
from .models import Movie, Review, Genre, Debate


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# 리뷰
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields=('user','movie','like_users')

# 리뷰 DB에서 뽑아오기 위해
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude=('like_users',)

# 토론
class DebateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debate
        fields = '__all__'

# 토론글을 DB에서 받아오기 위해
class DebateListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Debate
        fields = '__all__'