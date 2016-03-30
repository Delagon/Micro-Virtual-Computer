A very simple virtual computer in python with a miniscule instruction set.
(getch files taken form http://code.activestate.com/recipes/134892/)
How to run:
  $ python Comp.py [filename] [registers (optional)]
  will run it from the command line, going over the filename given with up to that many registers (default 8), NOTE, this is a very dumb machine, if you give it a program refering to, say, register 15, and leave the registers at default IT WILL BREAK.

Instruction set
CODE, NAME, REGISTERS USED, DEC.
0     'IOX' r1, r2          Preforms IO (See bellow)
1     'ADD' r1, r2, r3      r1 = r2 + r3
2     'MUL' r1, r2, r3      r1 = r2 * r3
3     'DIV' r1, r2, r3      r1 = r2 / r3
4     'STR' r1, r2          mem[r1] = r2
5     'LOD' r1, r2          r1 = mem[r2]
6     'SET' r1, V           r1 = V (specified value)
7     'JMT' r1, r2          if r1 >= 0, jump r2 lines

IOX
r1  desc
0   print number in r2
1   print char represented by r2
2   read a char from the stdin and store in r2
3   read a char from stdin and store as raw int ('1' = 1) in r2

Comming soon:
    - Allow printing to other outputs
    - Allow input from other input
