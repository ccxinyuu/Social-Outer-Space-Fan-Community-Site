from django.db import models
from django.conf import settings
import misaka

from group.models import Group
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()

# Create your models here.
class Post(models.Model):
    
