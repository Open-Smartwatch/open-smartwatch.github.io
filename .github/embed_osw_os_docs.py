#!/usr/bin/env python3

# This script is used to embed the OSW OS docs into the OSW docs.
# It (sadly) also uses command-line programs, as they are just easier to use :P

import os, yaml, shutil, subprocess, tempfile

targetYaml = 'mkdocs.yml'
sourceLocalCopy = os.environ.get('OSW_OS_LOCAL_COPY', None)
sourceBranch = os.environ.get('OSW_OS_DOCS_BRANCH', 'master')
dryRun = os.environ.get('DRY_RUN', 'false') == 'true'

sourceFolder = tempfile.mkdtemp()
# First clone the OSW OS docs
if sourceLocalCopy is None:
    subprocess.check_call(['git', 'clone', '--depth', '1', '--branch', sourceBranch, '--recursive', 'https://github.com/Open-Smartwatch/open-smartwatch-os.git', sourceFolder])
else:
    subprocess.check_call(['rsync', '-avh', '--delete', sourceLocalCopy + '/', sourceFolder + '/'])
    subprocess.check_call(['git', 'checkout', sourceBranch], cwd=sourceFolder)

# Merge docs folder from OSW-OS into ours
subprocess.check_call(['rsync', '-avh', sourceFolder + '/docs/', 'docs'])

# Merge mkdocs.yml with the OSW-OS one
with open(targetYaml, 'r') as f:
    target = yaml.safe_load(f)
assert('nav' in target)

with open(os.path.join(sourceFolder, 'docs', 'config.yml'), 'r') as f:
    source = yaml.safe_load(f)

# Now merge the firmware docs into the OSW docs (on the highest navigation level)
insertPosition = 0
for item in target['nav']:
    # Try to find the "Firmware" entry
    if 'Firmware' in item.keys():
        break
    insertPosition += 1
else:
    raise Exception('Could not find "Firmware" navigation entry in mkdocs.yml!')
insertPositionForFirmware = insertPosition

defaultFirmwareEntry = list()
for srcEntries in source:
    for srcLabel, srcEntry in srcEntries.items():
        if isinstance(srcEntry, list):
            # Ensure that the moutned list is flat
            for subEntries in srcEntry:
                for subEntry in subEntries.values():
                    assert isinstance(subEntry, str), 'No additional nesting allowed in OSW OS docs (the readthedocs-theme is broken)!'
            # Insert the new entry
            insertPosition += 1
            target['nav'].insert(insertPosition, {'Firmware - ' + srcLabel: srcEntry})
        elif isinstance(srcEntry, str):
            # A non-list entry is just a link to a single page -> add it to the default firmware entry
            defaultFirmwareEntry.append({srcLabel: srcEntry})
        else:
            # Whoops!
            raise Exception('Unknown type of entry in OSW OS docs!')
if len(defaultFirmwareEntry) > 0:
    target['nav'][insertPositionForFirmware] = {'Firmware': defaultFirmwareEntry}

# Write the new mkdocs.yml
if dryRun:
    print(yaml.safe_dump(target))
else:
    with open(targetYaml, 'w') as f:
        yaml.safe_dump(target, f)

# Cleanup
shutil.rmtree(sourceFolder)