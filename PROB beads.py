# -*- coding: utf-8 -*-
"""
ID: ion11
LANG: PYTHON3
PROB: beads
"""
f = open('beads.in','r')
fout = open('beads.out','w')

fin = f.readlines()

N = int(fin[0])

data = fin[1]
datalist = [bead for bead in data if bead == "w" or bead == "r" or bead == "b"]

best = 0

for i in range(N):
    
    before_break = datalist.copy()
    before_break.extend(datalist[:i])
    
    after_break = datalist[i:]
    after_break.extend(datalist)
    after_break.reverse()
    
    still_have_before = True
    still_have_after = True
    first_run = True
    temp_best = 0
    
    while still_have_before or still_have_after:
        
        if first_run:
            before_runner = before_break.pop()
            after_runner = after_break.pop()
            
            temp_best += 2
            
            first_run = False
            
        else:
            
            if still_have_before:
                before_next_one = before_break.pop()
                
            if still_have_after:
                after_next_one = after_break.pop()
            
            if before_runner == "w" or after_runner == "w":
                
                if before_runner == "w":
                    before_runner = before_next_one
                    temp_best += 1
                else:
                    if (before_next_one == before_runner or before_next_one == "w") and still_have_before:
                        temp_best += 1
                        assert(still_have_before == True)
                    else:
                        still_have_before = False
                        assert(still_have_before == False)
                
                if after_runner == "w":
                    after_runner = after_next_one
                    temp_best += 1
                else:
                    if (after_next_one == after_runner or after_next_one == "w") and still_have_after:
                        temp_best += 1
                        assert(still_have_after == True)
                    else:
                        still_have_after = False
                        assert(still_have_after == False)
                        
            else:
                
                if (before_next_one == before_runner or before_next_one == "w") and still_have_before:
                    temp_best += 1
                    assert(still_have_before == True)
                else:
                    still_have_before = False
                    assert(still_have_before == False)
                
                if (after_next_one == after_runner or after_next_one == "w") and still_have_after:
                    temp_best += 1
                    assert(still_have_after == True)
                else:
                    still_have_after = False
                    assert(still_have_after == False)
        
        
        if len(before_break) == 0:
            still_have_before = False
            assert(still_have_before == False)
            
        if len(after_break) == 0:
            still_have_after = False
            assert(still_have_after == False)
            
    if temp_best > best:
        best = temp_best

if best > N:
    best = N

fout.write(str(best)+"\n")