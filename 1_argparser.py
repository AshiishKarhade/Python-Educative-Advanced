import argparse


def get_args():
  parser = argparse.ArgumentParser(
      description="Simple Argument Parser",
      epilog="Example: python 1_argparser.py -n John -a 25")

  # Required Arguments
  parser.add_argument('-n',
                      '--name',
                      action='store',
                      required=True,
                      help='Enter name')
  # Optional Arguments
  parser.add_argument('-a', '--age', default=25, type=int, help='Enter Age')
  parser.add_argument('-s',
                      '--sex',
                      default='O',
                      choices=['M', 'F', 'O'],
                      help='Enter sex from M, F or O')
  print(parser.parse_args())


if __name__ == "__main__":
  get_args()
