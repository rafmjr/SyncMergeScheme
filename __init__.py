import sublime
from .SyncMergeSchemeCommand import SyncMergeSchemeCommand

def plugin_loaded():
    settings = sublime.load_settings('Preferences.sublime-settings')
    settings.add_on_change('color_scheme', SyncMergeSchemeCommand().run)
