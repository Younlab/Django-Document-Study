from django.db import models
__all__ = (
    'Person',
    'Group',
    'Membership',
)

class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )

class Membership(models.Model):
    # p1 이라는 Person인스턴스가 있을떼
    # Membership.objects.filter(person=p1)
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='memberships',
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    recommender = models.ForeignKey(
                                    Person,
                                    on_delete=models.SET_NULL,
                                    blank=True,
                                    null=True,
                                    related_name='memberships_by_recommender',
                                    )

    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)