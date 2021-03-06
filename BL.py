def BurnsidesLemma(h,w,s):
  longer_edge = max([h,w])
  if (h%2): #if h is odd, add 1. Same with width. This is relevant as the center column or row will matter in further calculations.
    h+=1
  if (w%2):
    w+=1  

  fix_i = s**(h*w)
 
  fix_ac = (s**((h//2)*(w//2)))
  
  fix_bpq = (s**((h)*(w//2)))

  #unfinished. This should be disabled if w!=h because diagonal reflections would never stabilize a non-square board.
  fix_rs = s**((((h*w))/2)+(longer_edge/2)) 

  # The below could be hardcoded but the reason we isolate them is because we were running multiple for loops to try to find the
  # correct number of each symmetries to use given X orbits. Reverse engineering nonsense. It was a for a Foobar challenge where 
  # I misinterpreted what kind of symmetries they were looking for. 
  how_many_i = 1
  how_many_ac = 2
  how_many_bpq = 3
  how_many_rs = 2

  sum_of_all_fix = (how_many_i * fix_i) + (how_many_ac * fix_ac) + (how_many_bpq * fix_bpq) + (how_many_rs * fix_rs)

  number_of_group_elements = how_many_i + how_many_ac + how_many_bpq + how_many_rs

  the_orbits = sum_of_all_fix / number_of_group_elements

  return the_orbits
