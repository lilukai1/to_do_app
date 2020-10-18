from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have a valid email.")
        if not username:
            raise ValueError("Users must have a valid username.")

        user = self.model(
            username=username,
            email= self.normalize_email(email),

            # first_name=first_name
            # last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None):

        user = self.create_user(
            email= self.normalize_email(email),
            username=username,
            password=password,
            # first_name=first_name
            # last_name=last_name
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email= models.EmailField(max_length=60, unique=True, verbose_name= "email")
    username= models.CharField(unique=True, max_length=20)
    date_joined= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ ] # add 'first_name', 'last_name', change username field to email and add username to required field if wanted

    objects = MyAccountManager()

    # def full_name(self):
    #     return (str(self.first_name) + " " + str(self.last_name))

    def __str__(self):
        return(self.username)

    def has_perm(self, parm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    # def get_absolute_url(self):
    #     return reverse('detail_view', kwargs={'name': full_name(self.first_name, self.last_name)})