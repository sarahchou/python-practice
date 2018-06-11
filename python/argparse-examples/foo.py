import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help: this program does nothing')
args = parser.parse_args()