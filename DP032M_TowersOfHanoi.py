#! /bin/env python3

def move_a_disk(source, dest):
  disk = hanoi_set[source].pop()
  hanoi_set[dest].append(disk)
  print(hanoi_set)

def hanoi(source, dest, temp, n):
  if n > 0:
    hanoi(source, temp, dest, n-1)
    move_a_disk(source, dest)
    hanoi(temp, dest, source, n-1)

def create_hanoi(n):
  return [list(range(n, 0, -1)),[],[]]

def print_hanoi(hanoi_set):
  max_height = max(len(hanoi_set[0]), len(hanoi_set[1]), len(hanoi_set[2]))
  p_list = [[]] * max_height
  for tower in hanoi_set:
    for disk in tower:
      pass
  for line in p_list:
    print(line)
  # the ground
  print("@" * 7)

if __name__ == "__main__":
  hanoi_n = 3
  hanoi_set = create_hanoi(hanoi_n)
  hanoi(0, 2, 1, hanoi_n)
  #print_hanoi([[3],[2, 1],[4]])
