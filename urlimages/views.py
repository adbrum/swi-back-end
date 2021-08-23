from .models import Lead
import jwt
from .serializers import LeadSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view


@api_view(['GET'])
def leadList(request, pk):
    print(f'===### {request.GET} - {pk}')
    leads = Lead.objects.filter(user_id=pk)
    # print(f'===### {leads}')
    serializer = LeadSerializer(leads, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def leadDetail(request, pk):
    lead = Lead.objects.get(id=pk)
    serializer = LeadSerializer(lead, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def leadCreate(request):
    data = {}

    for key in request.data:
        value = request.data[key]
        for i in value:
            for k, v in i.items():
                if k == "id":
                    data['image_id'] = v
                elif k == "file":
                    data['name'] = v['path']
                elif k == 'token':
                    try:
                        decoded = jwt.decode(v['token'], options={
                            "verify_signature": False})
                        data['user_id'] = decoded['user_id']
                    except Exception as e:
                        data['user_id'] = v['token']['user_id']
                elif k == 'url':
                    data['url'] = v

            serializer = LeadSerializer(data=data)

            if serializer.is_valid():
                serializer.save()

    return Response(serializer.data)


@ api_view(['DELETE'])
def leadDelete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()

    return Response('Deleted')
