#!/bin/bash

# Author: Brian Rieder

# Title: Contiguous Chains

# Difficulty: Intermediate

# Link: https://www.reddit.com/r/dailyprogrammer/comments/3gpjn3/20150812_challenge_227_intermediate_contiguous/

# Description:
# If something is contiguous, it means it is connected or unbroken. For a chain, this would mean that all parts 
# of the chain are reachable without leaving the chain. So, in this little piece of ASCII-art:

# xxxxxxxx  
# x      x

# there is only 1 contiguous chain, while in this

# xxxx xxxx 
#
# x

# there are 3 contiguous chains. Note that a single x, unconnected to any other, counts as one chain.

# For the purposes of this problems, chains can only be contiguous if they connect horizontally of vertically, not diagonally. So this image
# xx
#   xx
#     xx    
# contains three chains.

# Your challenge today is to write a program that calculates the number of contiguous chains in a given input.

# Input:
# The first line in the input will consist of two numbers separated by a space, giving the dimensions of the ASCII-field you're supposed to read. 
# The first number gives the number of lines to read, the second the number of columns (all lines have the same number of columns).
# After that follows the field itself, consisting of only x's and spaces.

# Output:
# Output a single number giving the number of contiguous chains.


# Sample inputs & outputs
# Input 1
# 2 8
# xxxxxxxx
# x      x

# Output 1
# 1

# Input 2
# 3 9
# xxxx xxxx
#     x    
#    xx    

# Output 2
# 3


# figure out what file to process
input_num=$1
if [ "$input_num" == "" ] ; then 
  echo "no input num specified" ; exit 1 
fi

# process the input file and shove it in an array of strings
chain_strs=()
while IFS= read -r line || [[ -n "$line" ]] ; do
  chain_strs+=("$line")
done < "input$input_num.txt"
chain_strs=("${chain_strs[@]:1}") # remove the dimensions

# execute a BFS
num_chains=0
function toggle_chain {
  str_num=$1
  str_index=$2
  wholestring="${chain_strs[$str_num]}"
  # base case
  if [ "${wholestring:$str_index:1}" != "x" ] ; then
    return
  fi
  local num_changes=0
  chain_strs[$str_num]="${wholestring:0:$str_index}o${wholestring:$str_index+1}"
  if (( $str_num > 0 )) ; then
    str_num=$((str_num-1))
    toggle_chain $str_num $str_index
    str_num=$((str_num+1))
  else
    (( num_changes++ ))
  fi
  if (( $str_num < ${#chain_strs} )) ; then
    str_num=$((str_num+1))
    toggle_chain $str_num $str_index
    str_num=$((str_num-1))
  else
    (( num_changes++ ))
  fi
  if (( $str_index > 0 )) ; then
    str_index=$((str_index-1))
    toggle_chain $str_num $str_index
    str_index=$((str_index+1))
  else
    (( num_changes++ ))
  fi
  if (( $str_index < ${#wholestring} )) ; then
    str_index=$((str_index+1))
    toggle_chain $str_num $str_index
    str_index=$((str_index-1))
  else
    (( num_changes++ ))
  fi
  # check for end of chain
  if (( num_changes == 0 )) ; then
    (( num_chains += 1 ))
  fi
}

for (( str_ind=0 ; str_ind<${#chain_strs}; str_ind++ )); do
  str=${chain_strs[$str_ind]}
  for (( i=0 ; i<${#str}; i++ )); do
    toggle_chain $str_ind $i
  done
done

echo "Number of chains: $num_chains"
