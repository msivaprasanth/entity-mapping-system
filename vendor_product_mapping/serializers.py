from rest_framework import serializers # type: ignore
from .models import VendorProductMapping

class VendorProductMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProductMapping
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at'] 
    
    def validate(self, data):
        vendor = data.get('vendor')
        product = data.get('product')
        is_primary = data.get('primary_mapping')

        duplicate_check = VendorProductMapping.objects.filter(
            vendor=vendor,
            product=product
        )
        if self.instance:
            duplicate_check = duplicate_check.exclude(pk=self.instance.pk)
        if duplicate_check.exists():
            raise serializers.ValidationError("This product is already mapped to this vendor.")
        
        if is_primary:
            primary_check = VendorProductMapping.objects.filter(
                vendor=vendor,
                primary_mapping=True
            )
            if self.instance:
                primary_check = primary_check.exclude(pk=self.instance.pk)
            if primary_check.exists():
                raise serializers.ValidationError({
                    "primary_mapping": "This vendor already has a primary product."
                    })

        return data