from django.db import models


class Person(models.Model):

    # 名前
    name = models.CharField(max_length=128)
    # 誕生日
    birthday = models.DateTimeField()
    # 性別
    sex = models.IntegerField(editable=False)
    # 出身地
    address_from = models.IntegerField()
    # 現住所
    current_address = models.IntegerField()
    # メールアドレス
    email = models.EmailField()


class Transaction(models.Model):
    trading_partner = models.CharField(max_length=128)
    amount = models.IntegerField()
    transaction_category = models.CharField(max_length=128)
    subject_kari = models.CharField(max_length=128)
    subject_kasi = models.CharField(max_length=128)
    update_timestamp = models.DateTimeField()

class Accounting_subject(models.Model):
    #ex.現金
    subject = models.CharField(max_length=128)
    #ex.資産
    parent_subject = models.CharField(max_length=128)
    color_in_bar = models.CharField(max_length=128)
    color_in_bar_border = models.CharField(max_length=128)
    amount = models.IntegerField()
    term = models.DateTimeField()
