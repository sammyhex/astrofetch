import argparse

errorMsg = 'astrofetch: invalid combination of arguments\nsee astrofetch -h for usage'

parser = argparse.ArgumentParser(
    prog='astrofetch',
    description='Fetch program to display the current zodiac season and system information.',
    epilog=f"Hiiii I'm at the bottom!! Wowee", formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument(
    '-s', '--small', 
    action='store_true', 
    help='show information as a single line')
parser.add_argument(
    '-m', '--mini', 
    action='store_true', 
    help='show as little information as possible')
parser.add_argument(
    '-u', '--unicode', 
    action='store_true', 
    default=False, 
    help='use unicode characters with small or medium mode')
parser.add_argument(
    '-i', '--info', 
    nargs='+', 
    metavar='', 
    help='search for sign or date information. (eg: leo) (jan 1)')

args = parser.parse_args()

if args.small:
    if args.mini or args.info:
        exit(errorMsg)
if args.mini:
    if args.info:
        exit(errorMsg)
