from django.http import JsonResponse
from django.views import View
from django.utils import timezone

from main.security import CSRFExempt

from main.models import AccessKey


class HomeViewAPI(CSRFExempt, View):

    def get(self, req, *args, **kwargs):

        data = {
            "message": "You're accessing Passwords and Access keys Management System."
        }
    
        return JsonResponse(data, safe=False)
    

    def post(self, req, *args, **kwargs):

        token = req.POST.get('token', '').strip()

        data = {
            "message": "failed",
            "errors": []
        }
        print('token', token)

        if token:
            access_key = AccessKey.objects.filter(token=token, date_expiration__gt=timezone.now()).first()
            print('access_key', access_key)
            if access_key:
                access_key.times_used += 1
                access_key.save()

                data["message"] = "success"
            
            else:
                data["errors"].append("token")

        else:
            data["errors"].append("token")


        return JsonResponse(data, safe=False)
