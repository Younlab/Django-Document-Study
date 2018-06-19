from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f'[{self.pk}] Place({self.name})'

    class Meta:
        ordering = ['name']


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'[{self.pk}] Restaurant'

class Supplier(Place):

    # 특정 Place 인 p1 있을 때
    # Supplier.objects.filter(customers_in=p1)
    # Supplier.objects.filter(place_ptr=p1)
    customers = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='supplier_by_customer',
    )

    # p1 이 역방향 Manager 를 사용할때
    # related_name 안겹침
    # p1.supplier_set <- MTO
    # p1.supplier     <- OTO (역방향 매니저가 존재하지 않음)
    # p1이 역방향 Query를 사용할때
    # related_name 및 related_query_name에 아무것도 지정하지 않았을대
    # related_query_name 기본값
    # 클래스명의 lowercase -> supplier 겹칩
