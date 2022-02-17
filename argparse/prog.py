import argparse


parser = argparse.ArgumentParser(
    prog="This is a test argparse python program.",
    usage="%(prog)s [options]",
    description="Calculate the square of the given number."
)
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", type=int, help="increase output verbosity", choices=[0, 1, 2])
group.add_argument("-q", "--quiet", action="store_true", help="show the simple result")
parser.add_argument("square", type=int, help="Display the square of a given number")
parser.print_help()
args = parser.parse_args()
area = args.square ** 2
if args.verbose == 1:
    print(f"The square of the {args.square} is {area}")
elif args.verbose == 2:
    print(f"{args.square} ^ 2 = {area}")
elif args.quiet:
    print(area)
else:
    print("You need to use the parameter!")
