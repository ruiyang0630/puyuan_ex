class ConvertCoolkiesToAuthorization:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.META.get('HTTP_COOKIE')
        if token:
            request.META['HTTP_AUTHORIZATION'] = token
        response = self.get_response(request)
        return response
