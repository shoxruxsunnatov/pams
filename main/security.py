from django.contrib.auth.mixins import AccessMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class CSRFExempt(AccessMixin):
    
    @method_decorator(csrf_exempt, name='dispatch')
    def dispatch(self, request, *args, **kwargs):
        
        return super().dispatch(request, *args, **kwargs)
