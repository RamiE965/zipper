from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Django standard user functionality
    pass

class Post(models.Model):
    # Posts model
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    message = models.TextField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User, related_name="likes")

    class Meta:
        # Order by reverse chronological order
        ordering = ['-timestamp']

    def __str__(self):
        # String representation of model
        return '{author}: {message} ({timestamp})'.format(
            author=self.author,
            message=self.message,
            timestamp=self.timestamp,
        )

RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)

class Relationship(models.Model):
    # Relationships between users model
    from_user = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='relationships_from')
                                
    to_user = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='relationships_to')

    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)

    def __str__(self):
        return f'{self.from_user.username} likes {self.to_user.username}'