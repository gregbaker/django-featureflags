# django-featureflags

A feature flags/toggle module for Django that allows you to quickly and temporarily disable some features on a site.

## Installing and Configuring


* `FEATUREFLAGS_LOADER`: The module responsible for loading the list of currently-disabled features. See [Disabling Features](#disabling) below.  Default: `'featureflags.loaders.settings_loader'`
* `FEATUREFLAGS_DISABLED_VIEW`: The view function to be called when a view is disabled with the `uses_feature` decorator. Default: `'featureflags.views.service_unavailable'`
* `DEFAULT_TEMPLATE`: If using the `'featureflags.views.service_unavailable'` view, the template that should be rendered. Default is `503.html` if present, or a very simple internal message if not.
* `FEATUREFLAGS_CACHE_TIMEOUT`: The number of seconds that the currently-disabled features should be cached using Django's default cache. If set to zero, caching flags will be disabled and the loader will be called for every request. The default is 10 seconds.
* Additional settings may be used depending on the loader used. These are described below.


## Disabling Features <a name="disabling"></a>

### Loading from `settings.py`

The default `FEATUREFLAGS_LOADER` is `'featureflags.loaders.settings_loader'`. It looks at the setting `DISABLED_FEATURES` for the currently-disabled features. It can be set like one of these:

    DISABLED_FEATURES = set() # nothing disabled: normal operation
    DISABLED_FEATURES = set(['big_reports', 'post_comment'])

Putting disabled features in `settings.py` requires a code-restart if you want to disable features: this might not be desirable.

### Loading from a JSON file

The loader `featureflags.loaders.file_loader` will read a JSON file with a list of the disabled features. You can set the location of the JSON file with the settings `FEATUREFLAGS_FILENAME`. So in your `settings.py`, you will have code like this:

    FEATUREFLAGS_LOADER = 'featureflags.loaders.file_loader'
    FEATUREFLAGS_FILENAME = `/home/deployment/disabled_features.json

Then in the `disabled_features.json` file, have content like one of these:

    []
    ["big_reports", "post_comment"]



### Loading from other places

TODO


## About Feature Flags

Some things to read about what feature flags are:

 * [Wikipedia: Feature Toggle](http://en.wikipedia.org/wiki/Feature_toggle)
 * [Martin Fowler: Feature Toggle](http://martinfowler.com/bliki/FeatureToggle.html)
 * [What is a feature flag?](http://stackoverflow.com/questions/7707383/what-is-a-feature-flag)

