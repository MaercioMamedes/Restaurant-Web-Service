import factory

from core.models import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda obj: f'user_test{id}')
    email = factory.LazyAttribute(lambda obj: f'{obj.name}@teste.com')

    def __str__(self):
        return self.name
