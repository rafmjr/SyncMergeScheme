import os, sublime, sublime_plugin
from .packages.appdirs import user_data_dir

class SyncMergeSchemeCommand(sublime_plugin.ApplicationCommand):
    def __init__(self):
        self.sm_package_dir = os.path.join(user_data_dir('Sublime Merge'), 'Packages/User')
        self.sm_settings_files = [
            'Commit Message - Merge.sublime-settings',
            'Commit Message - Merge Dark.sublime-settings',
            'Diff - Merge.sublime-settings',
            'Diff - Merge Dark.sublime-settings',
            'File Mode - Merge.sublime-settings',
            'File Mode - Merge Dark.sublime-settings',
        ]

    def run(self):
        st_color_scheme = sublime.load_settings('Preferences.sublime-settings').get('color_scheme')

        for file_name in self.sm_settings_files:
            file_path = os.path.join(self.sm_package_dir, file_name)

            try:
                with open(file_path, 'r') as file:
                    sm_current_settings = sublime.decode_value(file.read())
            except:
                sm_current_settings = {}
            finally:
                sm_current_settings['color_scheme'] = st_color_scheme

            with open(file_path, 'w') as file:
                file.write(sublime.encode_value(sm_current_settings, pretty = True))
