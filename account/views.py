from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm
from django.views.generic import CreateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

def password_reset_request(request):
	msg = None
	form = PasswordResetForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			data = form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'account',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'olayemipeter2005@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
			else:
				msg = 'Email does not exist'
	return render(request=request, template_name="password_reset.html", context={"form":form, 'msg':msg})

class register(CreateView):
    model = User  
    form_class = RegisterForm
    template_name= 'register.html'

    def form_valid(self, form):
        user = form.save()
        return redirect('login')
