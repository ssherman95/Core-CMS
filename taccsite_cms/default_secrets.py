# TACC CMS SITE TEMPLATE SETTINGS.
# DEFAULT VALUES.
# CHANGE BEFOR DEV/PREPROD/PRODUCTION DEPLOYMENT.

########################
# DJANGO SETTINGS
########################

_SECRET_KEY = 'replacethiswithareallysecureandcomplexsecretkeystring'
_DEBUG = True       # False for Prod.
_CONSOLE_LOG_ENABLED = False    # Boolean check to turn on/off console logging statements.

# Specify allowed hosts or use an asterisk to allow any host and simplify the config.
# _ALLOWED_HOSTS = ['hostname.tacc.utexas.edu', 'host.ip.v4.address', '0.0.0.0', 'localhost', '127.0.0.1']   # In production.
_ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', '*']   # In development.

# Boolean check to see if ldap is being used by the site.
# Requires django-auth-ldap ≥ 2.0.0
_LDAP_ENABLED = False

# Boolean check to determine the appropriate database settings when using containers.
_USING_CONTAINERS = True

########################
# DATABASE SETTINGS
########################

if _USING_CONTAINERS:
    # used in container deployments.
    _DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'PORT': '5432',
            'NAME': 'taccsite',
            'USER': 'postgresadmin',
            'PASSWORD': 'taccforever', # Change before live deployment.
            'HOST': 'core_cms_postgres'
        }
    }
else:
    # used in local dev, venv or manual deployments.
    _DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'PORT': '5432',
            'NAME': 'taccsite',
            'USER': 'postgresadmin',
            'PASSWORD': 'taccforever', # Change before live deployment.
            'HOST': 'localhost'
        }
    }

########################
# DJANGO CMS SETTINGS
########################

# CMS Site (allows for multiple sites on a single CMS)
_SITE_ID = 1
_CMS_TEMPLATES = (
    # Customize this list in per-project `secrets.py`
    # FAQ: First template is default template
    # REF: http://docs.django-cms.org/en/latest/how_to/install.html#templates

    # For standard pages (has Container and Breadcrumbs)
    ('standard.html', 'Standard'),
    # For content that spans full window width (no Container nor Breadcrumbs)
    ('fullwidth.html', 'Full Width'),

    # Any project that needs per-project styles must have a custom template
    # FAQ: This is a tedious solution until a cleaner solution is devised
    # TODO: Automate per-project asset load and update exisitng sites as needed
    # ('name-of-project/templates/fullwidth.html', 'Fullwidth (Custom)'),
    # NOTE: If project later uses custom template, then for that project:
    #       1. Rename standard default template to "DEPRECATED […]".
    #       2. Update all pages to use the custom default template.
    #       3. Disable standard default template (remove from `_CMS_TEMPLATES`).
    # ('fullwidth.html', 'DEPRECATED Fullwidth'),

    # Any portal whose homepage has NO design must enable and use this template
    # ('home_portal.html', 'Standard Portal Homepage'),

    # All portals should enable all of these templates
    # FAQ: If this becomes mandatory, then in `settings.py`:
    #      `if _PORTAL: [ manually add these entries ]`
    # ('guide.html', 'Guide'),
    # ('guides/getting_started.html', 'Guide: Getting Started'),
    # ('guides/data_transfer.html', 'Guide: Data Transfer'),
    # ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    # ('guides/portal_technology.html', 'Guide: Portal Technology Stack'),

    # For now, only Core portal should enable this template
    # FAQ: We know not yet how to auto-replicate pages and plugins across sites
    # ('style_guide.html', 'Style Guide'),
)

########################
# GOOGLE ANALYTICS
########################

# To use during dev, Tracking Protection in browser needs to be turned OFF.
_GOOGLE_ANALYTICS_PROPERTY_ID = "UA-123ABC@%$&-#"
_GOOGLE_ANALYTICS_PRELOAD = True

########################
# CMS FORMS
########################

# Create CMS Forms
# SEE: https://pypi.org/project/djangocms-forms/
# SEE: https://www.google.com/recaptcha/admin/create
_DJANGOCMS_FORMS_RECAPTCHA_PUBLIC_KEY = ""
_DJANGOCMS_FORMS_RECAPTCHA_SECRET_KEY = ""

########################
# ELASTICSEARCH
########################

_ES_AUTH = 'username:password'
_ES_HOSTS = 'http://elasticsearch:9200'
_ES_INDEX_PREFIX = 'cms-dev-{}'
_ES_DOMAIN = 'http://localhost:8000'

########################
# FEATURES
########################

"""
Features for the CMS that can be turned either ON or OFF

Usage:

- For baked-in features, like BRANDING or PORTAL, see relevant section instead.
- For optional features, look below, and enable feature(s) via _FEATURES list.

Baked-In Feature Setting Example.

# Desctipion of feature X
# SEE: [link to user/div guide about feature]
_FEATURE_A = "someValue"

Optional Feature Toggle Example.

_FEATURES = {
    # Desctipion of feature X
    # SEE: [link to user/dev guide about feature]
    "X": True,

    # Desctipion of feature Y
    # SEE: [link to user/dev guide about feature]
    "Y": False,

    # Desctipion of feature Z
    # SEE: [link to user/dev guide about feature]
    "Z": True,
}

"""

_FEATURES = {
    # Blog/News & Social Media Metadata
    # GL-42: Split this into two features
    # SEE: https://confluence.tacc.utexas.edu/x/EwDeCg
    # SEE: https://confluence.tacc.utexas.edu/x/FAA9Cw
    "blog": False,
}

########################
# BRANDING & LOGOS & FAVICON
########################
# TODO: GH-59: Use Dict Not Array for Branding Settings

# Branding settings for portal and navigation.

"""
Additional Branding and Portal Logos for Partner & Affiliate Organizations

Usage:

- For each beand used in the templating, add corresponding new settings values to this file  (see example below).
- New branding settings must be added to the _BRANDING list to render in the template.
- The order of the _BRANDING list determines the rendering order of the elements in the template.
- The portal logo setting must be assigned to the _LOGO variable to render in the template.
- The following VALUES for new elements set in the configuration object must exist in the portal css as well:
    - Any new selectors or css styles (add to /taccsite_cms/static/site_cms/css/src/_imports/branding_logos.css)
    - Image files being references (add to /taccsite_cms/static/site_cms/img/org_logos)

Values to populate (for an array):

_SETTING_NAME = [                # The name of the branding or logo config setting object.
    "org_name",                    # The name of the organization the branding belongs too.
    "img_file_src",                # Path and filename relative to the static files folder.
    "img_element_classes",         # The list of selectors to apply to the rendered element, these need to exist in the css/scss.
    "a_target_url",                # The href link to follow when clicked, use "/" for portal logos.
    "a_target_type",               # The target to open the new link in, use _blank for external links, _self for internal links.
    "alt_text",                    # The text to read or render for web assistance standards.
    "cors_setting",                # The CORS setting for the image, set to anonymous by default.
    "visibility"                   # Toggles wether or not to display the element in the template, use True to render, False to hide.
]

Values to populate (for a dict):

_SETTING_NAME = {                  # The name of the favicon config setting object.
    "img_file_src": "…",             # Path and filename relative to the static files folder.
}

Branding Configuration Example.

_ANORG_BRANDING = [
   "anorg",
   "site_cms/img/org_logos/anorg-logo.png"
   "branding-anorg",
   "https://www.anorg.com/"
   "_blank",
   "ANORG Logo",
   "anonymous",
   "True"
]

Logo Configuration Example.

_ANORG_LOGO = [
   "anorg",
   "site_cms/img/org_logos/anorg-logo.png"
   "branding-anorg",
   "/"
   "_self",
   "ANORG Logo",
   "anonymous",
   "True"
]

Favicon Configuration Example.

_ANORG_FAVICON = {
    "img_file_src": "site_cms/img/favicons/favicon.ico"
}
"""

########################
# BRANDING

_TACC_BRANDING = [
    "tacc",
    "site_cms/img/org_logos/tacc-white.png",
    "branding-tacc",
    "https://www.tacc.utexas.edu/",
    "_blank",
    "TACC Logo",
    "anonymous",
    "True"
]

_UTEXAS_BRANDING = [
    "utexas",
    "site_cms/img/org_logos/utaustin-white.png",
    "branding-utaustin",
    "https://www.utexas.edu/",
    "_blank",
    "University of Texas at Austin Logo",
    "anonymous",
    "True"
]

_NSF_BRANDING = [
    "nsf",
    "site_cms/img/org_logos/nsf-white.png",
    "branding-nsf",
    "https://www.nsf.gov/",
    "_blank",
    "NSF Logo",
    "anonymous",
    "True"
]

_BRANDING = [ _TACC_BRANDING, _UTEXAS_BRANDING ]        # Default TACC Portal.
# _BRANDING = [ _NSF_BRANDING, _TACC_BRANDING, _UTEXAS_BRANDING ]       # NSF Funded TACC Portal.

########################
# LOGOS

_PORTAL_LOGO = [
    "portal",
    "site_cms/img/org_logos/portal.png",
    "",
    "/",
    "_self",
    "Portal Logo",
    "anonymous",
    "True"
]

_LOGO = _PORTAL_LOGO                # Default Portal Logo.

########################
# FAVICON

_FAVICON = {
    "img_file_src": "site_cms/img/favicons/favicon.ico"
}

########################
# PORTAL
########################

_PORTAL = False     # True for any CMS that is part of a Portal.
