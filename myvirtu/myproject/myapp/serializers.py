from rest_framework import serializers
from .models import Stock
from django.db.models import Q  
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import (
	CharField,
	EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
	)


User = get_user_model()

class UserCreateSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
            'username',
            'password',
            'email',
		]

		extra_kwargs = {"password":
                        {"write_only":True}
                       
		            } 

	def create(self,validated_data):
	   	username = validated_data['username']
	   	email = validated_data['email']
	   	password = validated_data['password']
	   	user_obj = User(username = username,email = email)
	   	user_obj.set_password(password)
	   	user_obj.save()
	   	return validated_data
# class StockSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Stock
# 		fields = '__all__'

# class StockSerializer1(serializers.ModelSerializer):
# 	class Meta:
# 		model = Stock
# 		fields=['ticker','open1','close','volume']

# class UserSerializer(serializers.ModelSerializer):
# 	password = serializers.CharField(write_only=True)

# 	def create(self, validated_data):
# 		user = get_user_model().objects.create(
#              username = validated_data['username']
# 			)
# 		user.set_password(validated_data['password'])
# 		user.save()
# 		return user

# 	class Meta:
# 		model = get_user_model()
# 		fields = ('username', 'password')
class UserLoginSerializer(ModelSerializer):
	token = CharField(allow_blank= True, read_only=True)
	username = CharField(allow_blank= True,required=True)
	email  = EmailField(label="Email-Address",allow_blank= True,required=True)
	class Meta:
		model = User
		fields = [
            'username',
            'password',
            'email',
            'token',
		]

		extra_kwargs = {"password":
                        {"write_only":True}
                       
		            } 

	def validate(self,data):
		user_obj = None
		username = data.get("username",None)
		email = data.get("email ",None)
		password = data['password']
		if not email and not username:
			raise ValidationError("username or email is required to login")
		user = User.objects.filter(Q(email=email)|Q(username=username)).distinct()
		if user.exists() and user.count() == 1:
			user_obj = user.first()
		else:
			raise ValidationError("This username/email is not valid")

		if user_obj:
		    if not user_obj.check_password(password):
		       	raise ValidationError("wrong")
		data["token"]="Some random token"
		return data




