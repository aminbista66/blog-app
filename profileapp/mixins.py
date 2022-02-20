from django.contrib.auth.mixins import AccessMixin

class CustomLoginAndUserCheckMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        user_given_id = kwargs.get('pk')
        if not request.user.is_authenticated and user_given_id == request.user.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
