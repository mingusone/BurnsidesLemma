def BurnsidesLemma(h,w,s):
  longer_edge = max([h,w])
  if (h%2): #if h is odd, add 1. 
    h+=1
  if (w%2):
    w+=1  

  fix_i = s**(h*w)
 
  fix_ac = (s**((h//2)*(w//2)))
  
  fix_bpq = (s**((h)*(w//2)))

  fix_rs = s**((((h*w))/2)+(longer_edge/2)) #unfinished. This should be disabled if w!=h because it will never be identical?

  how_many_i = 1
  how_many_ac = 2
  how_many_bpq = 3
  how_many_rs = 2

  sum_of_all_fix = (how_many_i * fix_i) + (how_many_ac * fix_ac) + (how_many_bpq * fix_bpq) + (how_many_rs * fix_rs)

  number_of_group_elements = how_many_i + how_many_ac + how_many_bpq + how_many_rs

  the_orbits = sum_of_all_fix / number_of_group_elements

  return the_orbits
