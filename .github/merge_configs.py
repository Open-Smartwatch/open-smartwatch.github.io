import argparse, yaml

parser = argparse.ArgumentParser()
parser.add_argument('target', type=str)
parser.add_argument('source', type=str)
args = parser.parse_args()

with open(args.target, 'r') as f:
    target = yaml.safe_load(f)
assert('nav' in target)

with open(args.source, 'r') as f:
    source = yaml.safe_load(f)

found = False
for menuEntry in target['nav']:
    if 'Firmware' in menuEntry.keys():
        found = True
        menuEntry['Firmware'] = source
assert(found)

with open(args.target, 'w') as f:
    yaml.safe_dump(target, f)