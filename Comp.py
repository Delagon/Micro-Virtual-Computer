import sys
import getch

Name_To_Hex = {
  "IOX" : 0,
  "ADD" : 1,
  "MUL" : 2,
  "DIV" : 3,
  "STR" : 4,
  "LOD" : 5,
  "SET" : 6,
  "JMT" : 7
  }

class command:
  def __init__(self, code, r1, r2, r3):
    self.code = code
    self.r1 = r1
    self.r2 = r2
    self.r3 = r3
  def toString(self):
    return self.code, self.r1, self.r2, self.r3

def main(fn, regcount):
  reg = [0] * regcount
  lines = []
  f = file(fn)
  mem = []
  line = f.readline()
  inMem = False
  while line != "":
    if line == "MEM\n":
      inMem = True
    else:
      if inMem:
        mem += [int(line)]
      else:
        r = [0,0,0]
        p = 0
        for i in line.split()[1:]:
          r[p] = int(i)
          p += 1
        lines += [command(Name_To_Hex[line.split()[0]], r[0], r[1], r[2])]
    line = f.readline()
  for i in lines:
    print i.toString()
  pointer = 0
  while pointer < len(lines):
    comm = lines[pointer]
    code = comm.code
    if code == 0:
      r1 = reg[comm.r1]
      if   r1 == 0:
        print reg[comm.r2]
      elif r1 == 1:
        print chr(reg[comm.r2])
      elif r1 == 2:
        reg[comm.r2] = ord(getch.getch())
      elif r1 == 3:
        reg[comm.r2] = int(getch.getch())
    elif code == 1:
      reg[comm.r1] = reg[comm.r2] + reg[comm.r3]
    elif code == 2:
      reg[comm.r1] = reg[comm.r2] * reg[comm.r3]
    elif code == 3:
      reg[comm.r1] = reg[comm.r2] / reg[comm.r3]
    elif code == 4:
      mem[comm.r1] = reg[comm.r2]
    elif code == 5:
      reg[comm.r1] = mem[comm.r2]
    elif code == 6:
      reg[comm.r1] = comm.r2
    elif code == 7:
      if reg[comm.r1] >= 0:
        pointer += reg[comm.r2] - 1
    pointer += 1

if __name__ == "__main__":
  args = sys.argv[1:]
  if len(args) == 1:
    args += [8]
  main(args[0], int(args[1]))
