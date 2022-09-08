from django.db import models
from django.forms import ImageField
import datetime
# Create your models here.

class AssetsCategory(models.Model):
    id = models.AutoField(primary_key=True)
    cat_Title = models.CharField(max_length=50) 
    is_created = models.DateTimeField(auto_now_add=True)

class AssetssubCategory(models.Model):
    Assets_Category = models.ForeignKey(AssetsCategory, on_delete=models.CASCADE)
    subcat_Title = models.CharField(max_length=50)
    #subcat_image = models.FileField(default="", upload_to = 'images/')

class AssetsSubsubCategory(models.Model):
    AssetsSubCategoryid = models.ForeignKey(AssetssubCategory, on_delete=models.CASCADE)
    Subsubcat_Title = models.CharField(max_length=50)
    #subsubcat_image = models.FileField(blank=True,null=True,upload_to = 'images/')

class Rooms(models.Model):
    Room_No = models.CharField(max_length=50) 
    Floor = models.CharField(max_length=50)

class Assets(models.Model):
    id = models.AutoField(primary_key=True)
    Assetsname = models.CharField(max_length=50)
    Room_No_id = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    Assets_SubCategory_id = models.ForeignKey(AssetssubCategory, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    Details = models.CharField(max_length=50)
    AssetsSubsubCategory_id = models.ForeignKey(AssetsSubsubCategory, on_delete=models.CASCADE, default=None, blank=True, null=True)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)