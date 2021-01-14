# django imports
from django.shortcuts import render, get_object_or_404

# django rest framework imports
from rest_framework.response import Response
from rest_framework.views import APIView

# app imports
from .models import Article
from .serializers import ArticleSerializer


class ArticleView(APIView):
    """
        docstring
    """

    def get(self, request):
        """
            docstring
        """
        
        objects = Article.objects.all()
        serializer = ArticleSerializer(objects, many=True)

        return Response({'articles': serializer.data})

    def post(self, request):
        """
            docstring
        """

        obj = request.data.get('article')

        # Cria um artigo com os dados acima.
        serializer = ArticleSerializer(data=obj)
        if serializer.is_valid(raise_exception=True):
            obj_saved = serializer.save()

        return Response({'success': f"Article '{obj_saved.title}' created successfully."})

    def put(self, request, id):
        """
            docstring
        """

        saved_obj = get_object_or_404(Article.objects.all(), id=id)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_obj, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            obj_saved = serializer.save()

        return Response({'success': f"Article '{obj_saved.title}' updated successfully."})

    def delete(self, request, id):
        """
            docstring
        """

        obj = get_object_or_404(Article.objects.all(), id=id)
        obj.delete()

        return Response({'message': f'Article with id {id} has been deleted.'}, status=204)



