from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label="Sujet")
    message = forms.CharField(widget=forms.Textarea,  label = "Message")
    sender  = forms.EmailField(label = "Votre adresse e-mail")
    send_back = forms.BooleanField(label='Recevoir une copie', help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
