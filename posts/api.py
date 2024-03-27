from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializers


@api_view(['GET'])
def post_list_api (request):
    posts = Post.objects.all()
    data = PostSerializers(posts, many=True).data

    return Response({'data':data})