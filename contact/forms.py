from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control", "id" : "inputSubject", "placeholder" :"Insérez le sujet"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class" : "form-control", "id" : "inputMessage", "placeholder" :"Écrivez votre message"}))
    sender  = forms.EmailField(widget=forms.EmailInput(attrs={"class" : "form-control", "id" : "inputEmail", "placeholder" : "Entrez ici votre adresse mail"}))
    send_back = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class" : "form-check-input", "id" : "gridCheck", "placeholder" : "Cochez si vous souhaitez obtenir une copie du mail envoyé."}), required=False)
