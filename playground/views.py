from email import message
from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    # Prevent attackers
    try:
        # # send_mail('subject', 'message', 'info@moshbuy.com',
        # #           ['alimi@moshbuy.com'])
        # mail_admins('subject', 'message', html_message='<em>message</em>')
        # message = EmailMessage('subject', 'message',
        #                        'from@moshbuy.com', ['johnsmith@moshbuy.com'])
        # message.attach_file('playground/static/images/a2.jpg')
        # message.send()
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Alimi'}
        )
        message.send(['john@moshbuy.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
