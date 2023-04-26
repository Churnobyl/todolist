from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, name, gender, age, introduction=None, password=None):
        if not email:
            raise ValueError("이메일은 필수 입력 필드입니다.")
        
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            gender = gender,
            age = age,
            introduction = introduction,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, gender, age, introduction=None, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            name = name,
            gender = gender,
            age = age,
            introduction = introduction,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Meta:
        db_table = 'user'
        
    gender_list = (
        ('M', '남성'),
        ('F', '여성'),
    )
    
    email = models.EmailField(max_length=255, unique=True, verbose_name='이메일 주소')
    name = models.CharField(max_length=30, verbose_name='이름')
    gender = models.CharField(max_length=1, choices=gender_list, verbose_name='성별')
    age = models.SmallIntegerField(verbose_name='나이')
    introduction = models.TextField(verbose_name='자기소개', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'gender', 'age', ]
    
    def __str__(self):
        return str(self.name)
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    
    