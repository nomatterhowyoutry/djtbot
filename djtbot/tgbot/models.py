from django.db import models


class ParentCategoryClothes(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CategoryClothes(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    parent = models.ForeignKey(ParentCategoryClothes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CategoryPrice(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_user_in_telegram = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_bot = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.username


class Male(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Country(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ClothesMale(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ClothesCountry(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Clothes(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    article_id = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=200)
    img_top = models.ImageField(upload_to='product_top')
    img_left = models.ImageField(upload_to='product_left')
    img_right = models.ImageField(upload_to='product_right')
    img_bottom = models.ImageField(upload_to='product_bottom')
    created = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    price = models.PositiveSmallIntegerField()

    currency = models.ForeignKey(CategoryPrice, on_delete=models.CASCADE)
    parent_category = models.ForeignKey(ParentCategoryClothes, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryClothes, on_delete=models.CASCADE)
    male = models.ForeignKey(ClothesMale, on_delete=models.CASCADE)
    country = models.ForeignKey(ClothesCountry, on_delete=models.CASCADE)

    def __str__(self):
        return self.article_id


# class Buttons(models.Model):
#     id = models.AutoField(primary_key=True, editable=False)
#     name = models.CharField(max_length=30, unique=True)
#     callback_data = models.CharField(max_length=30, unique=True, blank=True, default='')
#     switch_inline_query_current_chat = models.CharField(max_length=30, unique=True, blank=True, default='')
#     url = models.URLField(blank=True, default='')
#
#     def __str__(self):
#         return self.name
#
#
# class Message(models.Model):
#     id = models.AutoField(primary_key=True, editable=False)
#     name = models.CharField(max_length=30)
#     text = models.TextField()


class Basket(models.Model):
    id = models.AutoField(primary_key=True, editable=False)

    product = models.ForeignKey(Clothes, on_delete=models.CASCADE, to_field='article_id')
    user = models.OneToOneField(User, on_delete=models.CASCADE, to_field='id_user_in_telegram')


class BasketHistory(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.IntegerField()
    product = models.IntegerField()
