from django.contrib.auth.hashers import make_password, check_password
from django.db import models

class OlineUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=100)
    password = models.CharField(max_length=1024)
    balance = models.FloatField()
    # 补充的信息
    user_email = models.CharField(max_length=25, null=True)
    mobile_phone = models.CharField(max_length=15)
    remark = models.TextField(null=True)

    class Meta:
        db_table = 'oline_user'

    def setPassword(self, new_password):
        self.password = make_password(password=new_password)

    def checkPassword(self, enter_password):
        return check_password(enter_password, self.password)

class StockInfoList(models.Model):
    stock_name = models.CharField(max_length=20)
    stock_code = models.CharField(max_length=10)
    stock_type = models.CharField(max_length=10)

    class Meta:
        db_table = 'stock_info_list'