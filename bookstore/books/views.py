from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# View lấy danh sách sách và tạo mới một cuốn sách
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        """
        Trả về danh sách tất cả các cuốn sách
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Thêm một cuốn sách mới
        """
        return self.create(request, *args, **kwargs)

# View lấy thông tin, cập nhật hoặc xóa sách theo ID
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        """
        Lấy thông tin chi tiết của một cuốn sách theo ID
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Cập nhật thông tin của một cuốn sách
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Xóa một cuốn sách theo ID
        """
        return self.destroy(request, *args, **kwargs)

