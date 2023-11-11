from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id','title', 'subtitle', 'content', 'author', 'isbn', 'price',)

    def validate(self,data):
        title = data.get('title', None)
        author = data.get('author', None)

        # check title if it contains only alphabetical chars
        if not title.isalpha():
            raise ValidationError(
                {
                    'status' : False,
                    'message' : "Kitobni sarlavhasi harflardan tashkil topgan bo'lishi kerak!"
                }
            )

        if Books.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitob sarlavhasi va muallifi bir hil bo'lgan kitobni yuklay olmaysiz!"
                }
            )
        return  data

    def validate_price(self, price):
        if price < 0 or price > 99999999999:
            raise ValidationError(
                {
                    'status' : False,
                    'message' : "Narx noto'g'ri kiritlgan"
                }
            )


# class CashSerializer(serializers.Serializer):
#     input = serializers.CharField(max_length=150)
#     output = serializers.CharField(max_length=120)