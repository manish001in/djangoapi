from rest_framework import serializers
from REST.models import REST
from django.contrib.auth.models import User


class RESTSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = REST
        fields = ('url', 'owner', 'name', 'designation', 'alive', 'data')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    details = serializers.HyperlinkedRelatedField(many=True, view_name='rest-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'details')


# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=REST.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets')
#
#
# class RESTSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = REST
#         fields = ('owner', 'id', 'title', 'code', 'linenos', 'language', 'style')
