import numpy as np
import pylab as plt
import draw_qsurf

def get_deff(fname_list = None, draw = False, pad_num = None):
	if fname_list == None:
		return 'woot'
		
	com_matrix = np.zeros([3,2])

	j = 0
	for fname in fname_list:
		with open(fname) as f:
			check = f.readline()
		if check[0] == 'S':
			with open(fname, 'r') as fin:
				data = fin.read().splitlines(True)
			with open(fname, 'w') as fout:
				fout.writelines(data[2:])
				
			
		data = np.loadtxt(fname)
		
		com_x = 0
		com_y = 0
		com_z = 0
		
		i = 0
		for x in data[:,0]:
			com_x += x * data[i,3] 
			i += 1

		i = 0
		for y in data[:,1]:
			com_y += y * data[i,3] 
			i += 1

		i = 0
		for z in data[:,2]:
			com_z += z * data[i,3] 
			i += 1

		q_tot = np.sum(data[:,3])
		com_x = com_x / (q_tot * 1E-6)
		com_y = com_y / (q_tot * 1E-6)
		com_z = com_z / (q_tot * 1E-6)
		
		com_matrix[:,j] = np.array([com_x, com_y, com_z]) 
		
		
		if draw:
			if j == 0:
				draw_px = min(data[:,1]) * 1E6
				draw_py = min(data[:,0]) * 1E6
			if j == 1:
				draw_nx = min(data[:,1]) * 1E6
				draw_ny = min(data[:,0]) * 1E6
		j += 1
				
	d_eff = 0	
	for i in range(0,2):
		d_eff +=(com_matrix[i,0] - com_matrix[i,1])**2

	d_eff = np.sqrt(d_eff)
	# if draw:
		# draw_qsurf.draw(draw_px, draw_py, draw_nx, draw_ny, com_matrix, pad_num)
	
	# print d_eff
	if draw:
		return d_eff, np.array([draw_px, draw_py, draw_nx, draw_ny]), com_matrix[:2,:]
	else:
		return d_eff
		
def get_deff_global_old(fname_list = None, draw = False, pad_num = None):
	if fname_list == None:
		return 'woot'
	

	com_matrix = np.zeros([3,2])
	draw_ny = []
	draw_py = []
	draw_px = []
	draw_nx = []
	

	j = 0
	for fname in fname_list:
		with open(fname) as f:
			check = f.readline()
		if check[0] == 'S':
			with open(fname, 'r') as fin:
				data = fin.read().splitlines(True)
			with open(fname, 'w') as fout:
				fout.writelines(data[2:])
				
	fname_sorted = [fname_list[1::2], fname_list[::2]]
		
	for fname_pol in fname_sorted:
		data = []
		q_tot = 0	
		for fname in fname_pol:
			data.append(np.loadtxt(fname))
			
		com_x = 0
		com_y = 0
		com_z = 0
		
		for alpha in xrange(len(data)):
			i = 0
			for x in data[alpha][:,0]:
				com_x += x * data[alpha][i,3] 
				i += 1

			i = 0
			for y in data[alpha][:,1]:
				com_y += y * data[alpha][i,3] 
				i += 1

			i = 0
			for z in data[alpha][:,2]:
				com_z += z * data[alpha][i,3] 
				i += 1

			q_tot += np.sum(data[alpha][:,3])
			if draw:
				if j == 0:
					draw_px.append(min(data[alpha][:,1]) * 1E6)
					draw_py.append(min(data[alpha][:,0]) * 1E6)
				if j == 1:
					draw_nx.append(min(data[alpha][:,1]) * 1E6)
					draw_ny.append(min(data[alpha][:,0]) * 1E6)
		
		com_x = com_x / (q_tot * 1E-6)
		com_y = com_y / (q_tot * 1E-6)
		com_z = com_z / (q_tot * 1E-6)
		
		com_matrix[:,j] = np.array([com_x, com_y, com_z]) 
		j += 1		
	d_eff = 0	
	for i in range(0,2):
		d_eff +=(com_matrix[i,0] - com_matrix[i,1])**2

	d_eff = np.sqrt(d_eff)
	# if draw:
		# draw_qsurf.draw(draw_px, draw_py, draw_nx, draw_ny, com_matrix, pad_num)

	# print d_eff
	if draw:
		print np.array([draw_px, draw_py, draw_nx, draw_ny])
		return d_eff, np.array([draw_px, draw_py, draw_nx, draw_ny]), com_matrix[:2,:]
	else:
		return d_eff

def get_deff_global(fname_list = None, draw = False, pad_num = None):
	if fname_list == None:
		return 'woot'
	
	j = 0
	com_matrix = np.zeros([3,2])
	draw_ny = []
	draw_py = []
	draw_px = []
	draw_nx = []
	
	for fname in fname_list:
		with open(fname) as f:
			check = f.readline()
		if check[0] == 'S':
			with open(fname, 'r') as fin:
				data = fin.read().splitlines(True)
			with open(fname, 'w') as fout:
				fout.writelines(data[2:])
				
	data = []
	q_tot_pos = 0	
	q_tot_neg = 0	
	for fname in fname_list:
		data.append(np.loadtxt(fname))
		
	for alpha in xrange(len(data)):
		q_pos_in_current_pad = np.sum(np.multiply(data[alpha][:,3] > 0, data[alpha][:,3]))
		q_neg_in_current_pad = np.sum(np.multiply(data[alpha][:,3] < 0, data[alpha][:,3]))
		# print q_pos_in_current_pad + q_neg_in_current_pad

		i = 0
		for x in data[alpha][:,0]:
			if (data[alpha][i,3] > 0):
				com_matrix[0,0] += x * data[alpha][i,3] 
			else:
				com_matrix[0,1] += x * data[alpha][i,3] 
			i += 1

		i = 0
		for y in data[alpha][:,1]:
			if (data[alpha][i,3] > 0):
				com_matrix[1,0] += y * data[alpha][i,3] 
			else:
				com_matrix[1,1] += y * data[alpha][i,3] 
			i += 1

		i = 0
		for z in data[alpha][:,2]:
			if (data[alpha][i,3] > 0):
				com_matrix[2,0] += z * data[alpha][i,3] 
			else:
				com_matrix[2,1] += z * data[alpha][i,3] 
			i += 1

		q_tot_pos += q_pos_in_current_pad
		q_tot_neg += q_neg_in_current_pad
		
		
		# this is not working now
		if draw:
			if j == 0:
				draw_px.append(min(data[alpha][:,1]) * 1E6)
				draw_py.append(min(data[alpha][:,0]) * 1E6)
			if j == 1:
				draw_nx.append(min(data[alpha][:,1]) * 1E6)
				draw_ny.append(min(data[alpha][:,0]) * 1E6)
		
	com_matrix[:,0] = com_matrix[:,0]  / (q_tot_pos * 1E-6)
	com_matrix[:,1] = com_matrix[:,1]  / (q_tot_neg * 1E-6)
	d_eff = 0	
	for i in range(0,2):
		d_eff +=(com_matrix[i,0] - com_matrix[i,1])**2

	d_eff = np.sqrt(d_eff)
	# print d_eff
	# print d_eff
	# if draw:
		# draw_qsurf.draw(draw_px, draw_py, draw_nx, draw_ny, com_matrix, pad_num)

	# print d_eff
	if draw:
		# print com_matrix
		# print q_tot_neg
		# print q_tot_pos
		# print draw_ny
		# print draw_nx
		# print draw_py
		# print draw_px
		return d_eff, np.array([draw_px, draw_py, draw_nx, draw_ny]), com_matrix[:2,:]
	else:
		return d_eff
		

def get_deff_global_fixed(fname_list = None, draw = False, pad_num = None):
	if fname_list == None:
		return 'woot'
	
	j = 0
	com_matrix = np.zeros([3,2])
	
	for fname in fname_list:
		with open(fname) as f:
			check = f.readline()
		if check[0] == 'S':
			with open(fname, 'r') as fin:
				data = fin.read().splitlines(True)
			with open(fname, 'w') as fout:
				fout.writelines(data[2:])
				
	data = []
	data = np.zeros([4])
	for fname in fname_list:
		data = np.vstack((data, np.loadtxt(fname)))
	data = np.delete(data, (0), axis=0)
		
	i = 0
	for x in data[:,0]:
		if data[i,3] > 0:
			com_matrix[0,0] += x * data[i,3] 
		elif data[i,3] < 0:
			com_matrix[0,1] += x * data[i,3] 
		i += 1

	i = 0
	for y in data[:,1]:
		if (data[i,3] > 0):
			com_matrix[1,0] += y * data[i,3] 
		elif data[i,3] < 0:
			com_matrix[1,1] += y * data[i,3] 
		i += 1

	i = 0
	for z in data[:,2]:
		if (data[i,3] > 0):
			com_matrix[2,0] += z * data[i,3] 
		elif data[i,3] < 0:
			com_matrix[2,1] += z * data[i,3] 
		i += 1

	q_tot_pos = np.sum(np.multiply(data[:,3] > 0, data[:,3]))
	q_tot_neg = np.sum(np.multiply(data[:,3] < 0, data[:,3]))
	

	
	com_matrix[:,0] /=  (q_tot_pos * 1E-6)
	com_matrix[:,1] /=  (q_tot_neg * 1E-6)
	d_eff = 0	
	for i in range(0,2):
		d_eff +=(com_matrix[i,0] - com_matrix[i,1])**2

	d_eff = np.sqrt(d_eff)
	print d_eff
	return d_eff


	
if __name__ == "__main__":
	print get_deff()