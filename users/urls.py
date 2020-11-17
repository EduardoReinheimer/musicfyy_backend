from django.conf.urls import url
from django.urls import include
from allauth.account.views import confirm_email

urlpatterns = [
    url('rest-auth/', include('rest_auth.urls')),
    url('rest-auth/registration/', include('rest_auth.registration.urls')),
    url('account/', include('allauth.urls')),
    url('accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email,
    name='account_confirm_email'),
]