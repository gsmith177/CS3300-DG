from django.contrib.auth.backends import ModelBackend
from .models import User

# This code is becasue django's authentication expects a username and not an email.

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

