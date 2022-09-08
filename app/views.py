from asyncio.windows_events import NULL
from audioop import reverse
from email import message
from logging import exception
from multiprocessing import context
from venv import create
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.views.generic import View
from django.urls import reverse
from django.db.models import Q
# Create your views here.

def Indexpage(request):
    all_category = AssetsCategory.objects.all()
    totalcat = len(all_category)
    all_subcategorg = AssetssubCategory.objects.all()
    totalsubcat = len(all_subcategorg)
    all_roomsde = Rooms.objects.all()
    totalRoom = len(all_roomsde)
    all_assets = Assets.objects.all()
    totalAss = len(all_assets)
    return render(request,"app/index.html",{'catcount':totalcat,'subcatcount':totalsubcat,'roomcount':totalRoom,'Assetcount':totalAss})


def category(request):
    return render(request,"app/category.html")

def base(request):
    return render(request,"app/base.html")

def Addcategory(request):

    Title = request.POST['cat_Title']
    category = AssetsCategory.objects.create(cat_Title=Title)
    return HttpResponseRedirect(reverse('showcatad'))

def showcategoryasd(request):
    all_cat = AssetsCategory.objects.all()
    return render(request,"app/showcatad.html",{'key19':all_cat})



def Roomspage(request):
    return render(request,"app/AddRooms.html")

def AddRoomsp(request):

    RoomNo = request.POST['Room_No']
    Floorname = request.POST['Floor']
    AddRoom = Rooms.objects.create(Room_No=RoomNo,Floor=Floorname)
    return HttpResponseRedirect(reverse('showrooms'))

def showRooms(request):
    all_rooms = Rooms.objects.all()
    return render(request,"app/showrooms.html",{'key22':all_rooms})


def Subcategorypage(request):
    all_categ = AssetsCategory.objects.all()
    return render(request,"app/subcategory.html",{'key30':all_categ})

def Addsubcat(request):
    if request.method == 'POST':
    
        assetsCategory = AssetsCategory.objects.get(id = request.POST['Assets_Categories'])
        Subcat_Title = request.POST['subcat_Title']
        #subcim = request.FILES['subimage']
        Addsubcate = AssetssubCategory.objects.create(Assets_Category=assetsCategory,subcat_Title=Subcat_Title)
        return HttpResponseRedirect(reverse('showsubcatgory'))


def showsubcatgory(request):
    all_subcatg = AssetssubCategory.objects.all()
    return render(request,"app/showsubcate.html",{'key23':all_subcatg})

def Deletesubcate(request,id):
    deldata = AssetssubCategory.objects.get(id=id)
    deldata.delete()
    return HttpResponseRedirect(reverse('showsubcatgory'))


def SubSubcategorypage(request):
    all_subcatge = AssetssubCategory.objects.all()
    return render(request,"app/subsubcategory.html",{'key47':all_subcatge})

def Addsubsubcat(request):
    if request.method == 'POST':
    
        assetssubCategory = AssetssubCategory.objects.get(id = request.POST['Assets_Categories'])
        Subsubcat_Title = request.POST['subcat_Title']
        #subsubcim = request.FILES['subimage']
        Addsubsubcate = AssetsSubsubCategory.objects.create(AssetsSubCategoryid=assetssubCategory,Subsubcat_Title=Subsubcat_Title)
        return HttpResponseRedirect(reverse('showsubsubcatgory'))

def showsubsubcatgory(request):
    all_subsubcatg = AssetsSubsubCategory.objects.all()
    return render(request,"app/showsubsubcat.html",{'key48':all_subsubcatg})

def Deletesubsubcate(request,id):
    deldata = AssetsSubsubCategory.objects.get(id=id)
    deldata.delete()
    return HttpResponseRedirect(reverse('showsubsubcatgory'))


def Addassetpage(request):
    all_cat = AssetssubCategory.objects.all()
    all_room = Rooms.objects.all()
    all_subsubcategory = AssetsSubsubCategory.objects.all()
    return render(request,"app/Addasset.html",{'key19':all_cat,'key15':all_room,'key49':all_subsubcategory})

def Addasset(request):

    if request.method == 'POST':
        subsubcate = request.POST['Assets_subsubCategories']
        if len(subsubcate) == 0:
            assetssubCategory = AssetssubCategory.objects.get(id = request.POST['Assets_subCategories'])
            roomid = Rooms.objects.get(id = request.POST['Assets_roomno'])
            asset_name = request.POST['asset_name']
            asset_Status = request.POST['asset_Status']
            asset_Detail = request.POST['asset_details']
            Addassetst = Assets.objects.create(Assets_SubCategory_id=assetssubCategory,AssetsSubsubCategory_id=None,Room_No_id=roomid,Assetsname=asset_name,status=asset_Status,Details=asset_Detail)
            return HttpResponseRedirect(reverse('showasset'))    
        elif len(subsubcate)>0:
            assetssubCategory = AssetssubCategory.objects.get(id = request.POST['Assets_subCategories'])
            assetssubsubCategory = AssetsSubsubCategory.objects.get(id=subsubcate)
            roomid = Rooms.objects.get(id = request.POST['Assets_roomno'])
            asset_name = request.POST['asset_name']
            asset_Status = request.POST['asset_Status']
            asset_Detail = request.POST['asset_details']
            Addassets = Assets.objects.create(Assets_SubCategory_id=assetssubCategory,AssetsSubsubCategory_id=assetssubsubCategory,Room_No_id=roomid,Assetsname=asset_name,status=asset_Status,Details=asset_Detail)
            return HttpResponseRedirect(reverse('showasset'))

def showasset(request):
    all_cat = Assets.objects.all()
    return render(request,"app/assetlist.html",{'key22':all_cat})


def UpdateAssetpage(request,id):
    Assetup = Assets.objects.get(id = id)
    roomsda = Rooms.objects.all()
    all_subcateg = AssetssubCategory.objects.all()

    return render(request,"app/updateasset.html",{'key33':Assetup,'key30':roomsda,'key29':all_subcateg})

def UpdateAssets(request,id):
    adata = Assets.objects.get(id=id)
    #adata.Assets_SubCategory_id = AssetssubCategory.objects.get(id = request.POST['Assets_subCategories'])
    adata.Room_No_id = Rooms.objects.get(id = request.POST['Assets_roomno'])
    adata.Assetsname = request.POST['asset_name']
    adata.status = request.POST['asset_Status']
    adata.Details = request.POST['asset_details']
    adata.save()
    return HttpResponseRedirect(reverse('showasset'))

def DeleteAsset(request,id):
    deldata = Assets.objects.get(id=id)
    deldata.delete()
    return HttpResponseRedirect(reverse('showasset'))

def Searchpage(request):
    all_subcatg = AssetssubCategory.objects.all()
    all_rooms = Rooms.objects.all()
    all_subsubcat = AssetsSubsubCategory.objects.all()
    return render(request,"app/search.html",{'key39':all_subcatg,'key40':all_rooms,'key81':all_subsubcat})


def Search(request):
    categ = request.GET.getlist('Assets_subCategories')
    subsubcateg = request.GET.getlist('Assets_subsubCategories')
    roomsf = request.GET.getlist('Assets_roomno')
    statusAct = request.GET.get('StatusActive')
    statusNotact = request.GET.get('StatusNotActive')
   
    allassets = {}
    if len(categ)>0:
        allassets["Assets_SubCategory_id__id__in"] = categ
        
    if len(subsubcateg)>0:
        allassets["AssetsSubsubCategory_id__id__in"] = subsubcateg
    if len(roomsf)>0:
        allassets["Room_No_id__id__in"] = roomsf
    if statusAct:
        allassets["status"] = statusAct 
    if statusNotact:
        allassets["status"] = statusNotact

    search = Assets.objects.filter(**allassets)
    if len(search) == 0:
        message = "No Assets Found !! "
        return render(request,"app/showsearch.html",{'msg':message})
    
    return render(request,"app/showsearch.html",{'key44':search})

###############################################################################






# def SubcatSearchpage(request):
#     all_subcatge = AssetssubCategory.objects.all()
#     return render(request,"app/subcatsearch.html",{'key55':all_subcatge})

# def SubcatSearch(request):
#     searchcata = Assets.objects.filter(Q(Assets_SubCategory_id=request.GET.get('Assets_subCategories')),Q(status=request.GET.get('asset_Status')))
#     return render(request,"app/showsubcsearch.html",{'key57':searchcata})

# def RoomSearchpage(request):
#     all_roomser = Rooms.objects.all()
#     return render(request,"app/roomsearch.html",{'key58':all_roomser})

# def RoomSearch(request):
#     searchroom = Assets.objects.filter(Q(Room_No_id=request.GET.get('Assets_roomno')),Q(status=request.GET.get('asset_Status')))
#     return render(request,"app/showroomsearch.html",{'key59':searchroom})


  


