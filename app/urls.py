from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.Indexpage,name="index"),

    path("category/",views.category,name="category"),
    path("Category/",views.Addcategory,name="Category"),
    path("showcatad/",views.showcategoryasd,name="showcatad"),

    path("Rooms/",views.Roomspage,name="Rooms"),
    path("AddRooms/",views.AddRoomsp,name="AddRooms"),
    path("showrooms/",views.showRooms,name="showrooms"),

    path("Subcategorypage/",views.Subcategorypage,name="Subcategorypage"),
    path("Addsubcat/",views.Addsubcat,name="Addsubcat"),
    path("showsubcatgory/",views.showsubcatgory,name="showsubcatgory"),
    path("Deletesubcate/<id>",views.Deletesubcate,name="Deletesubcate"),

    path("SubSubcategorypage/",views.SubSubcategorypage,name="SubSubcategorypage"),
    path("Addsubsubcat/",views.Addsubsubcat,name="Addsubsubcat"),
    path("showsubsubcatgory/",views.showsubsubcatgory,name="showsubsubcatgory"),
    path("Deletesubsubcate/<id>",views.Deletesubsubcate,name="Deletesubsubcate"),

    path("addasset",views.Addassetpage,name="addasset"),
    path("Addasset",views.Addasset,name="Addasset"),
    path("showasset/",views.showasset,name="showasset"),

    path("updateassetpage/<id>",views.UpdateAssetpage,name="updateassetpage"),
    path("updateassets/<id>",views.UpdateAssets,name="updateassets"),
    path("deleteasset/<id>",views.DeleteAsset,name="deleteasset"),

    path("Searchpage",views.Searchpage,name="Searchpage"),
    path("Search",views.Search,name="Search"),

    # path("SubcatSearchpage",views.SubcatSearchpage,name="SubcatSearchpage"),
    # path("SubcatSearch",views.SubcatSearch,name="SubcatSearch"),

    # path("RoomSearchpage",views.RoomSearchpage,name="RoomSearchpage"),
    # path("RoomSearch",views.RoomSearch,name="RoomSearch"),
   
    path("base/",views.base,name="base"),

  ]