from django.shortcuts import redirect

class DoctorAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path starts with "/doctor/" and if doctor_id is not set in the session
        if request.path.startswith("/doctor/") and not request.session.get("doctor_id"):
            return redirect("doctor_login")  # Redirect to doctor login page if not authenticated
        response = self.get_response(request)  # Proceed to the next middleware/view
        return response
