from .models import Post
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings


def postPublishedCallback(sender, instance, **kwargs):
    if isinstance(instance, Post):

        host = settings.SITE_URL
        print(f"you could read it <a href='{host}/user/post/{instance.id}'>here</a>.")
        ###############################################################################
        # auth_users = CustomUser.objects.all()
        # for auth_user in auth_users:
        #     send_mail(
        #         "Mini Social: A new post was published",
        #         "",
        #         settings.SITE_MAIL,
        #         [auth_user.email],
        #         fail_silently=False,
        #         # fail_silently=False, in the production chane the true
        #         html_message = f"you could read it <a href='{host}/user/post/{instance.id}'>here</a>.",
        #     )
        ##################################################################################################
        # print('!!! Post published..')
        # print(instance)
        # # print(sender, instance)

   # HW: 1 notify by email the post author when a new comment was added to its post
   # hint: post_save (comment) ---> post ---> author  ---> email  
   # 
        try:
            auth_user = CustomUser.objects.get(pk=id)  # Replace with the actual email
        except CustomUser.DoesNotExist:
            auth_user = None
        
        if auth_user:
            # Sending the email to the user
            send_mail(
                "Mini Social: A new post was published",
                f"You could read it here: {host}/user/post/{instance.id}",
                settings.SITE_MAIL,
                [auth_user.email],  # Sending email to the user's email address
                fail_silently=False,  # Change to True in production
                html_message=f"You could read it <a href='{host}/user/post/{instance.id}'>here</a>.",
            )   