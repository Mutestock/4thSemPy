import cli_ex

if __name__ == "__main__":
    cli_ex.manager()

'''
A couple of disclaimers:

1.
    The exercise claims that the output path must be specified, yet the functions doesn't take an output path variable
    As such it is placed in the the program's root.
    Note that I know how to place it somewhere else.
    See exercise01

2.
    I am using click instead of argparse or docopt
    02-1a CLI Programs stated that there were multiple CLI libraries. 
    I personally felt like both argparse and doctopt were messy so I found an alternative.
    Contact me if this is going to be an issue.


Manual Testing: python utils_test.py

CLI usage:

1. 
python utils.py first --path insertYourPathHere

2. 
python utils.py second --path insertYourPathHere

3.
python utils.py third --list yourfile01.txt yourfile02.txt ...etc 

4.
python utils.py fourth --list yourfile01.txt yourfile02.txt ...etc 

5.
python utils.py fifth --list yourfile01.md yourfile02.md ...etc 

'''
