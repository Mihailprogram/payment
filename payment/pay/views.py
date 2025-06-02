from rest_framework import viewsets
from .models import BalanceOrganizations, Payment
from .serializers import BalanceOrganizationsSerializer, PaymentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BalacneAPI(APIView):
    def get(self, request, inn, format=None):
        try:
            organization = BalanceOrganizations.objects.get(inn=inn)
            serializer = BalanceOrganizationsSerializer(organization)
            return Response(serializer.data)
        except BalanceOrganizations.DoesNotExist:
            return Response(
                {"error": "Organization with this INN not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class PaymentAPI(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            balance = BalanceOrganizations.objects.filter(inn=serializer.data['payer_inn'])
            if balance.exists():
                balance = balance.first()
                balance.balance += serializer.data['amount']
                balance.save()
                print("баланс изменен", balance.balance)
            else:
                BalanceOrganizations.objects.create(inn=serializer.data['payer_inn'],
                                                    balance=serializer.data['amount'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
