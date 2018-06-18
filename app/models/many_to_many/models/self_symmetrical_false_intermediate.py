from django.db import models
__all__ = (
    'TwitterUser',
    'Relation',
)

class TwitterUser(models.Model):
    """
    User 간의 관계는 2종류로 나뉨
        follow
        block

    관계를 나타내는 Relation 클래스를 사용(중개모델)
    """
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
    )

    def __str__(self):
        return self.name

class Relation(models.Model):
    """
    TwitterUser 간의 MTM 관계를 정의
        from_user
        to_user
        follow인지, block 인지를 판단.
    """
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
    # 입력값을 제한하는 choices옵션 추가
    relation_type = models.CharField(
        max_length=1,
        choices=CHOICES_RELATION_TYPE,
    )
    # 관계의 생성일 기록
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'from({}), to({}), {}'.format(
            self.from_user.name,
            self.to_user.name,
            self.get_relation_type_display(),
        )