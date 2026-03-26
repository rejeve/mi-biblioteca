class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_paths = [
            '/accounts/',
            '/admin/',
        ]

        if not request.user.is_authenticated:
            if not any(request.path.startswith(p) for p in allowed_paths):
                from django.shortcuts import redirect
                return redirect('account_login')

        return self.get_response(request)