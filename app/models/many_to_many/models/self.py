from django.db import models
__all__ = (
    'FacebookUser',
)
#
# class FacebookUser(models.Model):
#     name = models.CharField(max_length=50)
#     # 관계가 대칭적으로 형성됨
#     # A가 B를 frends에 추가 -> B의 frends에도 A가 추가되어있다.
#     frends = models.ManyToManyField(
#         'self',
#     )
#
#     def __str__(self):
#         return self.name
#
#     def show_frends(self):
#         print('-',self.name ,'의 친구 목록')
#         result = self.frends.all()
#         for i in result:
#             print('-', i)

class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    frends = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        return self.name
    def show_frends(self):
        print('-', self.name, '의 친구목록')
        result = self.frends.all()
        for i in result:
            print('-', i)