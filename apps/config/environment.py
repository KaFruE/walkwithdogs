ENVIRONMENT = 'dev'

if ENVIRONMENT == 'prod':
    SETTINGS_MODULE = 'config.settings.prod'
elif ENVIRONMENT == 'dev':
    SETTINGS_MODULE = 'config.settings.dev'
