from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
# custom authenticated models
class UserManager(BaseUserManager):
    def create_user(self, email, role,password=None, is_active=True, is_admin=False, is_staff=False):
        if not email:
            raise ValueError("must enter email")
        if not password:
            raise ValueError("must hve a password")
        if not role:
            raise ValueError("must enter role")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password) #change or set password
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.role

    def get_full_name(self):
        return self.first_name
    
    def get_short_name(self):
        return self.last_name

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    class Meta:
        db_table = "USER_DETAILS"

#skeleton
# class create_user(models.Model):
    # username = models.CharField(max_length=50)
    # email = models.EmailField(max_length=50)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # role = models.CharField(max_length=10)
    # password = models.CharField(max_length=50)
    # class Meta:
    #     db_table = "user_det"