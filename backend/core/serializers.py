from rest_framework import serializers
from core.models import Branch, Link, BranchPhone

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"
  

class BranchPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchPhone
        fields = "__all__"

class BranchSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True)
    phones = BranchPhoneSerializer(many=True)
    class Meta:
        model = Branch
        fields = "__all__"
