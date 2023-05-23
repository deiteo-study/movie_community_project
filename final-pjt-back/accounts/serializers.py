from .models import User
from rest_framework import serializers
from movies.serializers import ReviewSerializer, MovieSerializer, CommentSerializer

class UserSerializer(serializers.ModelSerializer):
    # 내가 좋아한 리뷰
    like_reviews = ReviewSerializer(many=True, read_only=True)
    # 내가 좋아한 영화
    like_movies=MovieSerializer(many=True, read_only=True)
    # 내가 작성한 리뷰
    write_reviews=ReviewSerializer(many=True, read_only=True)
    # 내가 작성한 댓글
    write_comments=CommentSerializer(many=True, read_only=True)
    followers=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id','username','like_reviews','like_movies','write_comments','write_reviews','followings','followers')