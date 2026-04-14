from django.db import models


class Donor(models.Model):
    """
    XXXXXXXXX
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        XXXXXXXXXX

        Returns:
            str: XXXXXXXXxx
        """
        def __str__(self) -> str:
            return self.name
