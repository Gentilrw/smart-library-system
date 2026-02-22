from datetime import datetime

# logging decorator
def track_access(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG {datetime.now()}] Accessing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# closure permission system
def permission_check(required_role):
    def decorator(func):
        def wrapper(self, user_role, *args, **kwargs):
            if user_role != required_role:
                return "Access denied: Admins only."
            return func(self, user_role, *args, **kwargs)
        return wrapper
    return decorator