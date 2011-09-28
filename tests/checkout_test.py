from tests.patches_data import GIT, RAW
BAD_PATCH = ''.join(
    [l for l in GIT.PATCH.splitlines(True) if l.strip() != 'e'])
    fs['trunk/chrome/file.cc'] = (
        patch.FilePatchDiff(
            'chrome/file.cc', GIT.PATCH, []),
        patch.FilePatchDiff('new_dir/subdir/new_file', GIT.NEW_SUBDIR, []),
      content_lines = tree['chrome/file.cc'].splitlines(True)
      tree['chrome/file.cc'] = ''.join(
        ['bin_file', 'chrome/file.cc', 'new_dir/subdir/new_file', 'extra'],
        patches.filenames)
      co.apply_patch([patch.FilePatchDiff('chrome/file.cc', BAD_PATCH, [])])
      self.assertEquals(e.filename, 'chrome/file.cc')
        'patching file chrome/file.cc\n'
        'chrome/file.cc.rej\n')
          [patch.FilePatchDiff('chrome/file.cc', RAW.PATCH, svn_props)])
      self.assertEquals(e.filename, 'chrome/file.cc')
          'While running svn propset svn:ignore foo chrome/file.cc '
          'patching file chrome/file.cc\n'
          'svn: Cannot set \'svn:ignore\' on a file (\'chrome/file.cc\')\n')
        [patch.FilePatchDiff('chrome/file.cc', RAW.PATCH, svn_props)])
    filepath = os.path.join(self.root_dir, self.name, 'chrome/file.cc')
        ['bin_file', 'chrome/file.cc', 'new_dir/subdir/new_file', 'extra'],
        patches.filenames)
        ['svn', 'pget', 'svn:eol-style', 'chrome/file.cc'],
          [patch.FilePatchDiff('chrome/file.cc', RAW.PATCH, svn_props)])
      self.assertEquals(e.filename, 'chrome/file.cc')
          'Cannot apply svn property foo to file chrome/file.cc.')
        [patch.FilePatchDiff('chrome/file.cc', RAW.PATCH, svn_props)])
        ['bin_file', 'chrome/file.cc', 'new_dir/subdir/new_file', 'extra'],
        patches.filenames)
        'patching file chrome/file.cc\n'
        'chrome/file.cc.rej\n')