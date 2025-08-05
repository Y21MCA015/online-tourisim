from rest_framework.views import APIView
from rest_framework.response import Response

class FirstApiView(APIView):
    def get(self, request):
        return Response({"message": "First API created successfully"})