from django.db import models


# Create your models here.


# 用户
# 普通用户
class User(models.Model):
    gender_choices = (('男', '男'), ('女', '女'))
    id = models.IntegerField(db_column="id", primary_key=True, null=False)
    username = models.CharField(db_column="username", max_length=100, null=False)
    password = models.CharField(db_column="password", max_length=100, null=False)
    real_name = models.CharField(db_column="real_name", max_length=100, null=False)
    gender = models.CharField(db_column="gender", max_length=100, choices=gender_choices)
    mobile = models.CharField(db_column="mobile", max_length=100)
    email = models.CharField(db_column="email", max_length=100)
    address = models.CharField(db_column="address", max_length=200)
    image = models.CharField(db_column="image", max_length=200, null=True)

    class Meta:
        managed = True
        db_table = "user"

        def __str__(self):
            return "编号：%s\t姓名：%s\t性别：%s" % (self.id, self.name, self.gender)


# 管理员
class Manager(models.Model):
    gender_choices = (('男', '男'), ('女', '女'))
    id = models.IntegerField(db_column="id", primary_key=True, null=False)
    username = models.CharField(db_column="username", max_length=100, null=False)
    password = models.CharField(db_column="password", max_length=100, null=False)
    real_name = models.CharField(db_column="real_name", max_length=100, null=False)
    gender = models.CharField(db_column="gender", max_length=100, choices=gender_choices)
    mobile = models.CharField(db_column="mobile", max_length=100)
    email = models.CharField(db_column="email", max_length=100)
    address = models.CharField(db_column="address", max_length=200)
    image = models.CharField(db_column="image", max_length=200, null=True)

    class Meta:
        managed = True
        db_table = "manager"

        def __str__(self):
            return "编号：%s\t姓名：%s\t性别：%s" % (self.id, self.name, self.gender)


# 失物
class Lost(models.Model):
    id = models.IntegerField(db_column="id", primary_key=True, null=False)
    lost_name = models.CharField(db_column="lost_name", max_length=100, null=False)
    place = models.CharField(db_column="address", max_length=200)
    lost_date = models.DateField(db_column="lost_date", null=False)
    username = models.CharField(db_column="username", max_length=100, null=False)
    mobile = models.CharField(db_column="mobile", max_length=100)
    is_return = models.CharField(db_column="is_return", max_length=100, null=False)
    image = models.CharField(db_column="image", max_length=200, null=True)

    class Meta:
        managed = True
        db_table = "Lost"

        def __str__(self):
            return "编号：%s\t名字：%s\t地点：%s" % (self.id, self.lost_name, self.place)


# 招领
class Found(models.Model):
    id = models.IntegerField(db_column="id", primary_key=True, null=False)
    found_name = models.CharField(db_column="found_name", max_length=100, null=False)
    place = models.CharField(db_column="address", max_length=200)
    found_date = models.DateField(db_column="found_date", null=False)
    username = models.CharField(db_column="username", max_length=100, null=False)
    mobile = models.CharField(db_column="mobile", max_length=100)
    is_return = models.CharField(db_column="is_return", max_length=100, null=False)
    image = models.CharField(db_column="image", max_length=200, null=True)

    class Meta:
        managed = True
        db_table = "Found"

        def __str__(self):
            return "编号：%s\t名字：%s\t地点：%s" % (self.id, self.found_name, self.place)
