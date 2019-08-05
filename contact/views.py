from django.shortcuts import render
from .forms import ContactForm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(dest, mail_sender, sender_passwd, subject, message):

    msg = MIMEMultipart()
    msg['From'] = mail_sender
    msg['To'] = dest
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(mail_sender, sender_passwd)
    mailserver.sendmail(mail_sender, dest, msg.as_string())
    mailserver.quit()

def contact(request):
    
    form = ContactForm(request.POST or None)
    
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        send_back = form.cleaned_data['send_back']

        if send_back:
            send_mail(sender, "normandie.judo@gmail.com", '=S/]/Q"6HHt6', subject, message)
        
        send_mail("romain.guilloteau@outlook.com", "normandie.judo@gmail.com", '=S/]/Q"6HHt6', subject, message)
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'contact/contact.html', locals())
