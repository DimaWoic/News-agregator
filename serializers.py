from rest_framework import serializers
from .models import News, Category


class CategorySerilazer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class NewsSerializer(serializers.ModelSerializer):

    category = CategorySerilazer()

    class Meta:
        model = News
        fields = ('id', 'title', 'published', 'category')