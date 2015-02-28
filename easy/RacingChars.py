import sys
tracks = open(sys.argv[1], 'r').readlines()
index = 0
index_i = 0
for i in range(0, len(tracks)):	
    cur = tracks[i].strip()
    gate = cur.find('_')
    checkpoint = cur.find('C')
    if checkpoint != -1:
        index = checkpoint
    else:
	index = gate
    if i != 0:
        prev_i = tracks[i-1].strip()
        checkpoint_i = prev_i.find('C')
	gate_i = prev_i.find('_')
	if checkpoint_i != -1:
            index_i = checkpoint_i
	else:
	    index_i = gate_i
	if index < index_i:
	    print tracks[i][0:index] + "/" + tracks[i][index+1:]
	elif index > index_i:
	    print tracks[i][0:index] + "\\" + tracks[i][index+1:]
	else:
	    print tracks[i][0:index] + "|" + tracks[i][index+1:]
    else:
	print tracks[i][0:index] + "|" + tracks[i][index+1:]
