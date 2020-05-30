# Sync Merge Scheme
Plugin to sync **Sublime Merge** UI Scheme with the one selected on **Sublime Text**.

![How To Use](https://raw.githubusercontent.com/rafmjr/SyncMergeScheme/master/screenshots/demo.gif?raw=true)

## Installation

### Install via Package Control

The easiest and recommended way to install this plugin is using [Package Control](https://packagecontrol.io).

From the **application menu**, navigate to:

- `Tools` -> `Command Palette...` -> `Package Control: Install Package`, type
  the words **Sync Merge Scheme**, then select it to complete the installation.

### Install Manually

Download and extract this plugin as a zip file or clone the repository using git,
then move it to your Sublime Text packages directory.

```bash
~ git clone git@github.com:rafmjr/SyncMergeScheme.git "SyncMergeScheme"
```

> **TIP:** You can locate your Sublime Text packages directory by using the
> application menu `Preferences` -> `Browse Packages...`.

## Usage

Just open Sublime Text's `Command Palette`, then select `UI: Select Color Scheme` and
pick your favorite scheme, Sublime Merge should update accordingly.

## Configuration

This plugin will try to locate Sublime Merge settings on the same directory where Sublime Text
settings were placed in your machine. However, if you have a different setup, you can indicate
where your Sublime Merge setting files should be found by selecting in the main menu:

- `Preferences` -> `Package Settings` -> `Sync Merge Scheme` -> `Settings – User`

A configuration file for this plugin will be created. You can now indicate the Sublime Merge
path:

```
{
    // Absolute path where Sublime Merge settings should live in your machien
    "sublime_merge_path": "C:\\Users\\<USER>\\AppData\\Roaming\\Sublime Merge",
}
```

Save the file and restart Sublime Text for the configuration to take effect.

## License Notice

The option to customize your theme in Sublime Merge is only available with a valid license key.
