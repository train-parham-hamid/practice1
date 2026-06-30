
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

from users.serializer import InputUserSerializer, OutputUserModelSerializer
from users.models import User


class ListCreateUserAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request: Request) -> Response:
        user = User.objects.all()

        return Response(
            data=OutputUserModelSerializer(instance=user, many=True).data,
            status=status.HTTP_200_OK,
        )

    def post(self, request: Request) -> Response:
        serializer = InputUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(**serializer.validated_data)

        return Response(
            data=OutputUserModelSerializer(instance=user).data,
            status=status.HTTP_201_CREATED,
        )


class RetrieveUpdateDestroyUserAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request: Request, user_id: int) -> Response:
        user = User.objects.filter(id=user_id).first()

        if not user:
            raise NotFound("User not found !")

        return Response(
            data=OutputUserModelSerializer(instance=user).data,
            status=status.HTTP_200_OK
        )

    def put(self, request: Request, user_id: int) -> Response:
        serializer = InputUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.filter(id=user_id).first()

        if not user:
            raise NotFound("User not found !")

        validated_data = serializer.validated_data

        for key, value in validated_data.items():
            setattr(user, key, value)

        user.save(update_fields=validated_data.keys())

        return Response(
            data=OutputUserModelSerializer(instance=user).data,
            status=status.HTTP_201_CREATED
        )

    def patch(self, request: Request, user_id: int) -> Response:
        serializer = InputUserSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        user = User.objects.filter(id=user_id).first()

        if not user:
            raise NotFound("User not found !")

        validated_data = serializer.validated_data

        for key, value in validated_data.items():
            setattr(user, key, value)

        user.save(update_fields=validated_data.keys())

        return Response(
            data=OutputUserModelSerializer(instance=user).data,
            status=status.HTTP_201_CREATED
        )

    def delete(self, request: Request, user_id: int) -> Response:
        user = User.objects.filter(id=user_id).first()

        if not user:
            raise NotFound("User not found !")

        user.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
