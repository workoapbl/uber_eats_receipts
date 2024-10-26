import argparse
import os
from utils import create_charges

def parse_args():
    parser = argparse.ArgumentParser(description="Process a list of names.")
    parser.add_argument('names', metavar='N', type=str, nargs='+', help='a list of names')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    names = set(args.names)
    receipt_dir = 'receipts'
    print(create_charges([os.path.join(receipt_dir, filename) for filename in os.listdir(receipt_dir) if filename.endswith('.pdf')], names))