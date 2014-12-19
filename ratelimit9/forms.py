from captcha.fields import ReCaptchaField

class Ratelimit9Form(object):
    
    def __init__(self, *args, **kwargs):
        
        captcha = kwargs.pop('captcha', None)
        super(Ratelimit9Form, self).__init__(*args, **kwargs)
        
        if captcha:
            self.fields['captcha'] = ReCaptchaField(
                # @todo enable developer to adjust this field
                attrs={'theme':'white'},
                error_messages={
                    'required': 'Enter the CAPTCHA code.',
                    'captcha_invalid': 'The CAPTCHA code you entered is invalid. Try again.',
                }
            )
