from rest_framework import serializers

from portfolio.models import UserProfile
class ProfileSerializer(serializers.ModelSerializer):
    url  =serializers.SerializerMethodField(read_only=True)
    class Meta():
        model = UserProfile
        fields = [
            'url',
            'pk',
            'user',
            'about',
            'img',
            'github',
            'linkedin',      
        ]
        read_only_field = [ 'pk', 'user', ]
        
    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)    
    
    def validate_github(self, value):
        qs = UserProfile.object.filter(github__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("link must be potani hovi joie")
    