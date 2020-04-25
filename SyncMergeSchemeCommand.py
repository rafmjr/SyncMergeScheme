import sublime, sublime_plugin
import os, json
from .packages.appdirs import user_data_dir

class SyncMergeSchemeCommand(sublime_plugin.ApplicationCommand):
    def __init__(self):
        package_dir = os.path.join(user_data_dir('Sublime Merge'), 'Packages/User')

        self.settings_files = [
            os.path.join(package_dir, 'Commit Message - Merge.sublime-settings'),
            os.path.join(package_dir, 'Commit Message - Merge Dark.sublime-settings'),
            os.path.join(package_dir, 'Diff - Merge.sublime-settings'),
            os.path.join(package_dir, 'Diff - Merge Dark.sublime-settings'),
            os.path.join(package_dir, 'File Mode - Merge.sublime-settings'),
            os.path.join(package_dir, 'File Mode - Merge Dark.sublime-settings'),
        ]

    def run(self):
        color_scheme = sublime.active_window().active_view().settings().get('color_scheme')

        for settings_file in self.settings_files:
            with open(settings_file, 'r') as f:
                current_settings = json.load(f)

            with open(settings_file, 'w') as f:
                current_settings['color_scheme'] = color_scheme
                json.dump(current_settings, f, indent = 4, sort_keys = True)
