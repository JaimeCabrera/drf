from rest_framework import serializers

from apps.users.models import User


# model-serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    # para encriptar la contrasena al crear el user
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    # al actualizar encriptar la contrasena
    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data["password"])
        update_user.save()
        return update_user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    # para listas solo algunos campos
    def to_representation(self, instance):
        # data  = super().to_representation(instance)
        return {
            "id": instance["id"],
            "username": instance["username"],
            "email": instance["email"],
            "password": instance["password"],
        }

# class TestUserSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     email = serializers.EmailField()
#
#     # validate necesita la palabra validate_campo, pasa el metodo valiadte()
#     def validate_name(self, value):
#         # custom validation
#         if 'developer' in value:
#             raise serializers.ValidationError('Error')
#         return value
#
#     def validate_email(self, value):
#         # custom validation
#         if value == '':
#             raise serializers.ValidationError("Este campo no puede ir vacio")
#
#         # if  self.context["name"] in value:
#         # aplicando la validacion del name
#         if self.validate_name(self.context["name"]) in value:
#             raise serializers.ValidationError("No se puede usar el nombre en el correo")
#         return value
#
#     def validate(self, data):
#         # if data["name"] in data["email"]:
#         #     raise serializers.ValidationError("No se puede usar el nombre en el correo")
#         return data
#
#
#     # def create(self, validated_data):
