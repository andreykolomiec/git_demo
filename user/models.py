from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(...)

    def __str__(self) -> str:
        return self.name

    def say_hi(self) -> str:
        # age < 18 Hi, self.name
        # age > 18 Hi, self.name self.last_name
        if self.age < 18:
            return f"Hi, {self.name}"
        return f"Hello, {self.name}"
