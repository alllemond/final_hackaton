from rest_framework import generics, viewsets
from .models import Comment, Like
from rest_framework.response import Response
from rest_framework.decorators import action 
from .serializers import CommentSerializer
from .permissions import IsCommentAuthor


# class CreateCommentView(generics.CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class= CommentSerializer
#     permission_classes = [IsCommentAuthor]
    
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)



# class RetrieveEditDestroyCommentView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class= CommentSerializer
#     permission_classes = [IsCommentAuthor]
    
#     def perform_update(self, serializer):
#         serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset= Comment.objects.all()
    serializer_class = CommentSerializer
    permission_class = IsCommentAuthor

    def get_permission(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'like':
            permissions = [permissions.IsAuthenticated, ]
        else:
            permissions = [permissions.IsReviewAuthor, ]

        return [permission() for permission in permissions]

    @action(detail=True, methods=['POST'])
    def like(self, request, *args, **kwargs):
        review = self.get_object()
        like_obj, _ = Like.objects.get_or_create(review=review, user=request.user)
        like_obj.like = not like_obj.like 
        like_obj.save()
        status= 'like'
        if not like_obj.like:
            status = 'unlike'
        return Response({'status': status})


