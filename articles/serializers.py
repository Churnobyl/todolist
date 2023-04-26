from rest_framework import serializers
from articles.models import Article
from django.utils import timezone


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'image',
            'is_complete',
            'created_at',
            'updated_at',
            'completion_at',
            'user',
            ]
        
class ArticleCreateSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'image',
            'is_complete',
            'user',
            ]
    

class ArticleDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'image',
            'is_complete',
            'created_at',
            'updated_at',
            'completion_at',
            'user',
            ]
        
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.image = validated_data.get('image', instance.image)
        instance.is_complete = validated_data.get('is_complete', instance.is_complete)
        
        try:
            if validated_data['is_complete'] is True:
                    instance.completion_at = timezone.now()
        except KeyError:
            pass
        
        instance.save()
        return instance