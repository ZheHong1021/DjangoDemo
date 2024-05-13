from config.django.base import DEBUG, MIDDLEWARE, INSTALLED_APPS

# settings.py
print(f"DEBUG={DEBUG}")
if DEBUG:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INSTALLED_APPS += [
        'debug_toolbar', # debug_toolbar
    ]

    
    INTERNAL_IPS = ['127.0.0.1', ]

    # this is the main reason for not showing up the toolbar
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

    DEBUG_TOOLBAR_PANELS = [ # 看要打開哪個 Panel
        'debug_toolbar.panels.history.HistoryPanel',
        # 'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        # 'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        # 'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
    ]