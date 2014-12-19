from ratelimit.mixins import RatelimitMixin

class Ratelimit9Mixin(RatelimitMixin):

    def get_form_kwargs(self, *args, **kwargs):
        result = super(Ratelimit9Mixin, self).get_form_kwargs(*args, **kwargs)
         
        try:
            # check if captcha field already exists
            result['data']['recaptcha_response_field']
            result['captcha'] = True
        except KeyError:
            # check if user should complete the captcha
            if getattr(self.request, 'limited', False):
                result['captcha'] = True
        
        return result
