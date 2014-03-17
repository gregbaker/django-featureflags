# django-featureflags

A feature flags/toggle module for Django that allows you to quickly and temporarily disable some features on a site.

## Installing and Configuring


* `FEATUREFLAGS_LOADER`: The module responsible for loading the list of currently-disabled features. See [Disabling Features](#disabling) below.  Default: `'featureflags.loaders.settings_loader'`
* `FEATUREFLAGS_DISABLED_VIEW`: The view function to be called when a view is disabled with the `uses_feature` decorator. Default: `'featureflags.views.service_unavailable'`
* `DEFAULT_TEMPLATE`: If using the `'featureflags.views.service_unavailable'` view, the template that should be rendered. Default is `503.html` if present, or a very simple internal message if not.


## Disabling Features <a name="disabling"></a>

### Loading from `settings.py`

The default `FEATUREFLAGS_LOADER` is `'featureflags.loaders.settings_loader'`. It looks at the setting `DISABLED_FEATURES` for the currently-disabled features. It can be set like this:

> `DISABLED_FEATURES = set() # nothing disabled: normal operation`

> `DISABLED_FEATURES = set(['big_reports', 'search'])`

Putting disabled features in `settings.py` requires a code-restart if you want to disable features: this might not be desirable.

### Loading from other places

TODO


## About Feature Flags

Some things to read about what feature flags are:

 * [Wikipedia: Feature Toggle](http://en.wikipedia.org/wiki/Feature_toggle)
 * [Martin Fowler: Feature Toggle](http://martinfowler.com/bliki/FeatureToggle.html)
 * [What is a feature flag?](http://stackoverflow.com/questions/7707383/what-is-a-feature-flag)

