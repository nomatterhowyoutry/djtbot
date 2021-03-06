from .models import *


class UserManager(object):
    @classmethod
    def is_user(cls, user_id):
        try:
            user = User.objects.get(id_user_in_telegram=user_id)
        except User.DoesNotExist:
            user = None

        return user

    @classmethod
    def add_user(cls, id_user_in_telegram, first_name, username, is_bot):
        user = User.objects.create(
            id_user_in_telegram=id_user_in_telegram,
            first_name=first_name,
            username=username,
            is_bot=is_bot
        )
        user.save()


class ManagerUserCity(object):
    @classmethod
    def get_user(cls, user_id):
        try:
            country = Country.objects.get(user_id=user_id)
        except Country.DoesNotExist:
            country = None

        return country

    @classmethod
    def create(cls, country, user_id):
        user = Country.objects.create(
            name='Украина' if country == 1 else 'Россия',
            user_id=user_id
        )
        user.save()

    @classmethod
    def update(cls, user_id, country):
        user = Country.objects.filter(user_id=user_id).update(name='Украина' if country == 1 else 'Россия')


class ManagerUserTypes(object):
    @classmethod
    def get_user(cls, user_id):
        try:
            male = Male.objects.get(user_id=user_id)
        except Male.DoesNotExist:
            male = None

        return male

    @classmethod
    def create(cls, male, user_id):
        user = Male.objects.create(name='Мужской' if male == 1 else 'Женский', user_id=user_id)
        user.save()

    @classmethod
    def update(cls, user_id, male):
        user = Male.objects.filter(user_id=user_id).update(name='Мужской' if male == 1 else 'Женский')


class ClothesManager(object):
    @classmethod
    def get_clothes_all(cls):
        clothes = Clothe.objects.all()

        return clothes if clothes else None

    @classmethod
    def get_clothes(cls, article_id):
        article = Clothe.objects.filter(article_id=article_id)

        return article if article else None

    @classmethod
    def get(cls, article_id):
        try:
            article = Clothe.objects.get(article_id=article_id)
        except Clothe.DoesNotExist:
            article = None

        return article

    @classmethod
    def filter_clothes_for_category(cls, category_id, country, male):
        return Clothe.objects.filter(
            category_id=category_id,
            country=country,
            male=male,
            is_active=True).order_by('-id')


class ClothesCategoryManager(object):
    @classmethod
    def get_category_id(cls, category):
        try:
            category = CategoryClothe.objects.get(name=category)
        except CategoryClothe.DoesNotExist:
            category = None

        return category


class BasketManager(object):
    @classmethod
    def add(cls, user_id, product_id):
        basket = Basket.objects.create(id_user_in_telegram=user_id, product_id=product_id)
        basket.save()

    @classmethod
    def get(cls, id_user_in_telegram, product_id):
        product = Basket.objects.filter(id_user_in_telegram=id_user_in_telegram, product_id=product_id)

        return product if product else None

    @classmethod
    def del_product(cls, id_user_in_telegram, product_id):
        try:
            product = Basket.objects.filter(id_user_in_telegram=id_user_in_telegram, product_id=product_id)
            product.delete()
        except Basket.DoesNotExist:
            product = None

        return product

    @classmethod
    def get_product_in_basket(cls, user_id):
        product = Basket.objects.filter(id_user_in_telegram=user_id)

        return product if product else None


class SystemPhotoManager(object):
    @classmethod
    def get_product_img(cls):
        try:
            result = SystemPhoto.objects.get(name='шмотки')
        except SystemPhoto.DoesNotExist:
            result = None

        return result

    @classmethod
    def get_basket_photo(cls):
        try:
            result = SystemPhoto.objects.get(name='корзина')
        except SystemPhoto.DoesNotExist:
            result = None

        return result

    @classmethod
    def to_reviews_photo(cls):
        try:
            result = SystemPhoto.objects.get(name='поделиться')
        except SystemPhoto.DoesNotExist:
            result = None

        return result

    @classmethod
    def not_product_photo(cls):
        try:
            result = SystemPhoto.objects.get(name='нет товара')
        except SystemPhoto.DoesNotExist:
            result = None

        return result

    @classmethod
    def order(cls):
        try:
            result = SystemPhoto.objects.get(name='заказ')
        except SystemPhoto.DoesNotExist:
            result = None

        return result

    @classmethod
    def to_share_photo(cls):
        try:
            result = SystemPhoto.objects.get(name='rosie')
        except SystemPhoto.DoesNotExist:
            result = None

        return result


class OrderManager(object):
    @classmethod
    def add(cls, user_id, article_id, first_name, price, markup):
        order = Order.objects.create(
            user=user_id,
            article=article_id,
            first_name=first_name,
            price=price,
            markup=markup)
        order.save()


class HistoryUpdateManager(object):
    @classmethod
    def add(cls, update_id):
        order = HistoryUpdateId.objects.create(update_id=update_id)
        order.save()

    @classmethod
    def get(cls, update_id):
        try:
            update_id = HistoryUpdateId.objects.get(update_id=update_id)
        except HistoryUpdateId.DoesNotExist:
            update_id = None
        return update_id
