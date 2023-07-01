from utils.token import check_token
from django.http import JsonResponse

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object


API_WHITELIST = ["/api/administrator/login/", ]
ADMIN = ["/api/administrator/addProduct/", "/api/administrator/addModule/", "/api/administrator/addChoiceImage/", ]


class AuthorizeMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        if request.path not in API_WHITELIST:
            token = request.META.get('HTTP_TOKEN')
            if token is None or token == "":
                return JsonResponse({'errno': 1001, 'msg': "未查询到登录信息"})
            else:
                identify = "user"
                if request.path in ADMIN:
                    identify = "admin"
                status = check_token(identify, token)
                if status == 0:
                    pass
                elif status == 1:
                    return JsonResponse({'errno': 1002, 'msg': "登录已过期"})
                else:
                    return JsonResponse({'errno': 1003, 'msg': "权限不足"})
