# Contributing

Contributions to the project are welcome! Just open an [issue] or send a pull
request. After review/acceptance, the change will be incorporated as soon as
possible.

## Submitting a pull request

When submitting changes, you can use whatever workflow you're more comfortable
with.

### Using Github's web interface

The easiest way to submit a change is to just edit the page directly on the
Github interface. Check out the step-by-step instructions (with screenshots) on
[Github Help].

### Using the command line

Alternatively, you can do most of the process from the command line:

- [Fork the repository](https://github.com/rafmjr/SyncMergeScheme) on the Github's web interface

- Clone your fork locally:
```bash
~ git clone git@github.com:rafmjr/SyncMergeScheme.git "SyncMergeScheme"
```

- Create a feature branch, e.g. named after the command you plan to edit:
```bash
~ git checkout -b {branch_name}
```

- Make your changes (edit existing files or create a new one)

- Commit the changes:
```bash
~ git commit --all -m "{commit_message}"
```

- Push to your fork:
```bash
~ git push origin {branch_name}
```

- Go to the Github's page for your fork, and click the green pull request button.

> **NOTE:** Please send only related changes in the same pull request. Typically
> a pull request will include changes in a single file.

### Commit message

For the commit message, please follow the *[The seven rules of a great Git commit message]*.

[The seven rules of a great Git commit message]: https://chris.beams.io/posts/git-commit/#seven-rules
[Github Help]: https://help.github.com/articles/editing-files-in-another-user-s-repository/
[Repository]: https://github.com/rafmjr/SyncMergeScheme
[Issues]: https://github.com/rafmjr/SyncMergeScheme/issues
