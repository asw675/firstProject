from rest_framework import serializers

from first.models import user, dishes, evaluation, dishing


class firstSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id','user_id', 'user_name','password','price','cuisine','taste','healthy','orders','menu')

class dishesSerializer(serializers.ModelSerializer):
    class Meta:
        model=dishes
        fields=('dishes_number','dishes_name','dishes_img','dishes_price','dishes_cursine','dishes_taste','dishes_healthy','dishes_hot')

class evaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model=evaluation
        fields=('user_id','user_name','comment')

class dishingSerializer(serializers.ModelSerializer):
    class Meta:
        model=dishing
        fields=('id','order_number','user_id','order')