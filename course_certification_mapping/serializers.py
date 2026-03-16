from rest_framework import serializers  # type: ignore
from .models import CourseCertificationMapping

class CourseCertificationMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCertificationMapping
        fields = '__all__'
        read_only_fields = ['id','created_at','updated_at']

    def validate(self,data):
        course = data.get('course')
        certification = data.get('certification')
        is_primary = data.get('primary_mapping')

        duplicate_check = CourseCertificationMapping.objects.filter(
            course = course,
            certification = certification
        )
        if self.instance:
            duplicate_check = duplicate_check.exclude(pk=self.instance.pk)
        if duplicate_check.exists():
            raise serializers.ValidationError('This certification is already mapped to this course')
        
        if is_primary:
            primary_check = CourseCertificationMapping.objects.filter(
                course = course,
                primary_mapping = True
            )
            if self.instance:
                primary_check = primary_check.exclude(pk=self.instance.pk)
            if primary_check.exists():
                raise serializers.ValidationError({
                    "primary_mapping": "This course already has a certification"
                })
            
        return data