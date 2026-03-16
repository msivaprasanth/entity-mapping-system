from rest_framework import serializers # type: ignore
from .models import ProductCourseMapping

class ProductCourseMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCourseMapping
        fields = '__all__'
        read_only_fields = ['id','created_at','updated_at'] 

    def validate(self,data):
        product = data.get('product')
        course = data.get('course')
        is_primary = data.get('primary_mapping')

        duplicate_check = ProductCourseMapping.objects.filter(
            product = product,
            course = course
        )
        if self.instance:
            duplicate_check = duplicate_check.exclude(pk=self.instance.pk)
        if duplicate_check.exists():
            raise serializers.ValidationError('This course is already mapped to this product')
        
        if is_primary:
            primary_check = ProductCourseMapping.objects.filter(
                product = product,
                primary_mapping = True
            )
            if self.instance:
                primary_check = primary_check.exclude(pk=self.instance.pk)
            if primary_check.exists():
                raise serializers.ValidationError({
                    "primary_mapping": "This product already has a course"
                })
            
        return data
        