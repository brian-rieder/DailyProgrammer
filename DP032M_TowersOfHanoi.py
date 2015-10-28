#! /bin/env python3

# Author: Brian Rieder
# Purpose: Basic Towers of Hanoi solver with a pretty print

move_count = 0 # hack...

def move_a_disk(source, dest):
  disk = hanoi_set[source].pop()
  hanoi_set[dest].append(disk)
  print_hanoi(hanoi_set)
  global move_count
  move_count += 1

def hanoi(source, dest, temp, n):
  if n > 0:
    hanoi(source, temp, dest, n-1)
    move_a_disk(source, dest)
    hanoi(temp, dest, source, n-1)

def create_hanoi(n):
  return [list(range(n, 0, -1)),[],[]]

def print_hanoi(hanoi_set):
  p_list = []
  for height in range(hanoi_n):
    row_str = ""
    for tower in hanoi_set:
      try:
        row_str += " " + str(tower[height])
      except IndexError:
        #row_str += " |"
        row_str += "  "
    p_list.append(row_str)
  [print(row) for row in reversed(p_list)]
  # the ground
  print("@" * 7)

if __name__ == "__main__":
  hanoi_n = 3
  hanoi_set = create_hanoi(hanoi_n)
  print_hanoi(hanoi_set)
  hanoi(0, 2, 1, hanoi_n)
  print("There were %d moves required for completion." % move_count)
