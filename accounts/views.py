from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Competition
from .serializers import CompetitionSerializer


from .serializers import (
    SignupSerializer,
    UserSerializer,
    EmailTokenObtainPairSerializer,
)


class SignupView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "message": "Account created successfully",
                "user": UserSerializer(user).data,
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
            },
            status=status.HTTP_201_CREATED,
        )


class SigninView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EmailTokenObtainPairSerializer


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        return Response(
            {"message": "Logout successful. Remove tokens on client side."},
            status=status.HTTP_200_OK,
        )


class CompetitionListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        competitions = Competition.objects.all().order_by("-created_at")
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompetitionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)

        return Response(
            {
                "message": "Competition created successfully",
                "competition": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


class CompetitionDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Competition.objects.get(pk=pk)
        except Competition.DoesNotExist:
            return None

    def get(self, request, pk):
        competition = self.get_object(pk)

        if competition is None:
            return Response(
                {"error": "Competition not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = CompetitionSerializer(competition)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        competition = self.get_object(pk)

        if competition is None:
            return Response(
                {"error": "Competition not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = CompetitionSerializer(competition, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Competition updated successfully",
                "competition": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def patch(self, request, pk):
        competition = self.get_object(pk)

        if competition is None:
            return Response(
                {"error": "Competition not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = CompetitionSerializer(
            competition,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Competition updated successfully",
                "competition": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request, pk):
        competition = self.get_object(pk)

        if competition is None:
            return Response(
                {"error": "Competition not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        competition.delete()

        return Response(
            {"message": "Competition deleted successfully"},
            status=status.HTTP_200_OK,
        )
