#!/usr/bin/env python3

# This script is used to embed the OSW OS docs into the OSW docs.
# It (sadly) also uses command-line programs, as they are just easier to use :P

import os, yaml, shutil, subprocess, tempfile

targetYaml = 'mkdocs.yml'
sourceBranch = os.environ.get('OSW_OS_DOCS_BRANCH', 'master')
sourceFolder = tempfile.mkdtemp()

# First clone the OSW OS docs
subprocess.check_call(['git', 'clone', '--depth', '1', '--branch', sourceBranch, '--recursive', 'https://github.com/Open-Smartwatch/open-smartwatch-os.git', sourceFolder])

# Merge docs folder from OSW-OS into ours
subprocess.check_call(['rsync', '-avh', sourceFolder + '/docs/', 'docs'])

# Merge mkdocs.yml with the OSW-OS one
with open(targetYaml, 'r') as f:
    target = yaml.safe_load(f)
assert('nav' in target)

with open(os.path.join(sourceFolder, 'docs', 'config.yml'), 'r') as f:
    source = yaml.safe_load(f)

found = False
for menuEntry in target['nav']:
    if 'Firmware' in menuEntry.keys():
        found = True
        menuEntry['Firmware'] = source
assert(found)

with open(targetYaml, 'w') as f:
    yaml.safe_dump(target, f)

# Cleanup
shutil.rmtree(sourceFolder)