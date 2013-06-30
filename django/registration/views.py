from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict
from django.template.response import TemplateResponse
from django.utils.http import base36_to_int, is_safe_url, urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.translation import ugettext as _
from django.shortcuts import resolve_url
from django.utils.encoding import force_bytes, force_text

from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.sites.models import get_current_site

from registration.forms import UserCreateForm

from django.shortcuts import render

# Create your views here.

@sensitive_post_parameters()
@csrf_protect
@never_cache
def signup(request, template_name='registration/signup.html', user_creation_form=UserCreateForm):
    """
    Displays the signup form and handles the signup action.
    """
    redirect_to = '' # request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = user_creation_form(data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            user = form.save(commit=True)

            # Okay, registration complete. Log the user in.
            auth_login(request, user)

            return HttpResponseRedirect(redirect_to)
    else:
        form = user_creation_form(None)

    current_site = get_current_site(request)
    context = {
        'form': form,
        'next': redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }

    return TemplateResponse(request, template_name, context,)
