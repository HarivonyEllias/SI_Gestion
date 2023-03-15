from django.shortcuts import render
from gestion.models import Infosociete

# Create your views here.
def Choose(request):
    return render(request, 'choose.html')

def Create_form(request):
    return render(request, 'form.html')

def index(request):
    return render(request, 'index.html')

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

