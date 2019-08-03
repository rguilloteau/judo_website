from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    
    form = ContactForm(request.POST or None)
    
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['sender']
        renvoi = form.cleaned_data['send_back']

        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'contact/contact.html', locals())
