from django.shortcuts import render
from gestion.models import Infosociete
from gestion.models import CountSociete


# Create your views here.
def Choose(request):
    return render(request, 'choose.html')

def Create_form(request):
    return render(request, 'form.html')

def index(request):
    return render(request, 'index.html')

# def log(request):
#     return render(request, 'login.html')

# insert information societe
def insert_company(request):
    if request.method=='POST':
        nom=request.POST.get('nom-societe')
        objet=request.POST.get('objet')
        siege=request.POST.get('siege')
        adresse_exploitation=request.POST.get('adresse-exploitation')
        dirigeant=request.POST.get('nom-dirigeant')
        date_creation=request.POST.get('date-creation')
        identite_fiscale=request.POST.get('num-identite-fiscale')
        numero_statistique=request.POST.get('num-statistique')
        numero_registre_commerce=request.POST.get('num-registre-commerce')
        status=request.POST.get('status')
        devise_compte=request.POST.get('devise-tenue-compte')
    
        info=Infosociete(nom=nom,objet=objet,siege=siege,adresse_exploitation=adresse_exploitation,dirigeant=dirigeant,date_creation=date_creation,identite_fiscale=identite_fiscale,numero_statistique=numero_statistique,numero_registre_commerce=numero_registre_commerce,status=status,devise_compte=devise_compte)
        info.save()
        return render(request,'choose.html')
    else:
        return render(request,'form.html')

def list_company(request):
    societes=Infosociete.objects.all()
    return render(request,'list_company.html',{'societes':societes})


def get_id_name(request, idsociete, nom):
    # Use the id and nom to fetch the data for the selected row from your database
    # Pass the data to the 'show.html' template for rendering
    return render(request, 'create_count.html', {'idsociete': idsociete, 'nom': nom})

def log(request):
    return render(request,'login.html')

def insert_count(request):
    if request.method=='POST':
        idsociete=request.POST.get('idsociete')
        password=request.POST.get('password')
    
        count=CountSociete(idsociete=idsociete,mot_de_passe=password)
        count.save()
        return render(request,'welcome.html')
    else:
        return render(request,'create_count.html')

    

