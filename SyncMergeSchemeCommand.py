import re, sublime, sublime_plugin
from os import path
from .packages.debounce import debounce

class SyncMergeSchemeCommand(sublime_plugin.ApplicationCommand):
    def __init__(self):
        self.sm_path = sublime.load_settings('SyncMergeScheme.sublime-settings').get('sublime_merge_path')
        self.sm_package_dir = self.resolve_sm_package_dir()
        self.sm_settings_files = [
            'Commit Message - Merge.sublime-settings',
            'Commit Message - Merge Dark.sublime-settings',
            'Diff - Merge.sublime-settings',
            'Diff - Merge Dark.sublime-settings',
            'File Mode - Merge.sublime-settings',
            'File Mode - Merge Dark.sublime-settings',
        ]

    @debounce(1)
    def run(self):
        st_color_scheme = sublime.load_settings('Preferences.sublime-settings').get('color_scheme')
        self.sync_color_scheme(st_color_scheme)
        self.update_sm_preferences(st_color_scheme)

    def sync_color_scheme(self, color_scheme):
        for file_name in self.sm_settings_files:
            file_path = path.join(self.sm_package_dir, file_name)

            try:
                with open(file_path, 'r') as file:
                    sm_current_settings = sublime.decode_value(file.read())
            except:
                sm_current_settings = {}
            finally:
                sm_current_settings['color_scheme'] = color_scheme

            with open(file_path, 'w') as file:
                file.write(sublime.encode_value(sm_current_settings, pretty = True))

    def update_sm_preferences(self, color_scheme):
        sm_preferences_path = path.join(self.sm_package_dir, 'Preferences.sublime-settings')

        with open(sm_preferences_path, 'r') as file:
            sm_preferences = sublime.decode_value(file.read())

            if re.search('light', color_scheme):
                sm_preferences['theme'] = 'Merge.sublime-theme'
            elif re.search('dark', color_scheme):
                sm_preferences['theme'] = 'Merge Dark.sublime-theme'

        with open(sm_preferences_path, 'w') as file:
            file.write(sublime.encode_value(sm_preferences, pretty = True))

    def resolve_sm_package_dir(self):
        # if user has specified the installation path, resolve package directory based on that
        if self.sm_path:
            return path.join(self.sm_path, 'Packages', 'User')

        # else, figure out based on the Sublime Text installation path
        st_path = path.realpath(path.join(sublime.cache_path().replace('Cache', ''), '..'))
        return path.join(st_path, 'Sublime Merge', 'Packages', 'User')
