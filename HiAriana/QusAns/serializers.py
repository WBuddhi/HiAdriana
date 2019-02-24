from rest_framework import serializers
from QusAns.models import FileUpload

class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
    '''
        File upload serilization, access model
    '''

    class Meta:
        model = FileUpload
        fields = ('Upload',)

class QA_data(serializers.Serializer):
    '''
        Serialization of QA variables for out
    '''

    pk = serializers.IntegerField()
    Statement = serializers.CharField()
    Answers = serializers.ChoiceField(choices = [],allow_blank=True)

class QA_input(serializers.Serializer):
    '''
        Serilization of Answer variables from input
    '''
    pk = serializers.IntegerField()
    Answer = serializers.CharField()

