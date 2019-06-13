from rest_framework import serializers

from .models import Album, Track

class TrackSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'order', 'title', 'duration')

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializerModel(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'album_name', 'artist', 'tracks')



class TrackSerializer(serializers.Serializer):
    order = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    duration = serializers.IntegerField(required=False)
    album_id = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Serie` instance, given the validated data.
        """
        return Track.objects.create(**validated_data)

    def update(self, instance, validated_data):
   
        instance.order = validated_data.get('order', instance.order)
        instance.title = validated_data.get('title', instance.title)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.album_id = validated_data.get('album_id', instance.album_id)
        instance.save()
        return instance

