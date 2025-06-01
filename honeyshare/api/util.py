def ensureAttr(attr, exc):
    def _ensureAttr(func):
        def decorator(self, *args, **kwargs):
            if not hasattr(self, attr) or getattr(self, attr) is None:
                raise exc
            return func(self, *args, **kwargs)

        return decorator

    return _ensureAttr
