from django.core.validators import URLValidator as validator


class RedirectToPreviousMixin:

    default_redirect = '/list_view/'

    def get(self, request, *args, **kwargs):
        request.session['previous_page'] = request.META.get('HTTP_REFERER', self.default_redirect)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        try: 
            validator(self.request.session['previous_page'])
            print(self.request.session['previous_page'])
            return self.request.session['previous_page']
        except:
            print(default_redirect)
            return default_redirect
