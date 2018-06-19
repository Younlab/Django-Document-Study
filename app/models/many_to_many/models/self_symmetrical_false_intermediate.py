from django.db import models
__all__ = (
    'TwitterUser',
    'Relation',
)

# class TwitterUser(models.Model):
#     """
#     User 간의 관계는 2종류로 나뉨
#         follow
#         block
#
#     관계를 나타내는 Relation 클래스를 사용(중개모델)
#     """
#     name = models.CharField(max_length=50)
#     relations = models.ManyToManyField(
#         'self',
#         symmetrical=False,
#         through='Relation',
#     )
#
#     def __str__(self):
#         return self.name

class TwitterUser(models.Model):
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
    )

    def __str__(self):
        return self.name

    @property
    def following_relations(self):
        # 내가 follow 하고 있는 relation 들을 리턴
        # TwitterUser.objects.get(name=self.name).filter(Relation.objects.get())
        # Relation.objects.filter(from_user=self)
        # Relation.objects.filter(from_user=self, relation_type='f')
        return self.relations_by_from_user.filter(relation_type='f')

    @property
    def follower_relations(self):
        # 나를 follow 하고 있는 Relation 들을 리턴
        # (내가 Relation의 to_user이며, relation_type 이 'f' 인 경우)
        return self.relations_by_to_user.filter(relation_type='f')

    @property
    def block_relations(self):
        # 내가 block 하고 있는 relation 들을 리턴
        # Relation.objects.filter(from_user=self, relation_type='f')
        return self.relations_by_from_user.filter(relation_type='b')


class Relation(models.Model):
    CHOICES_RELATION_TYPE = (
        ('f', 'Follow'),
        ('b', 'Block'),
    )

    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_from_user',
    )

    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_to_user',
    )

    relation_type = models.CharField(
        max_length=1,
        choices=CHOICES_RELATION_TYPE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'from({}), to({}), {}'.format(
            self.from_user.name,
            self.to_user.name,
            self.get_relation_type_display(),
        )