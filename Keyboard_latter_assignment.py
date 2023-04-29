import random
import numpy as np

#Bigram probabilities
pro = np.array([[0.000573659, 0.001447538, 0.002242048, 0.002088958, 0.000083630, 0.000514490, 0.000990971, 0.001079245, 0.001926149, 0.000023576, 0.001351677, 0.005238945, 0.001669467, 0.010984435, 0.000070298, 0.001098178, 0.000004356, 0.005653817, 0.004434813, 0.008044121, 0.000342443, 0.002729539, 0.000487061, 0.000104215, 0.003521967, 0.000106177],
[0.001598044, 0.000118648, 0.000023576, 0.000021781, 0.003857421, 0.000013069, 0.000004356, 0.000008712, 0.000494241, 0.000032887, 0.000000000, 0.001004638, 0.000022978, 0.000009909, 0.001435403, 0.000024773, 0.000000000, 0.000539168, 0.000186815, 0.000098662, 0.001505869, 0.000019220, 0.000000000, 0.000000000, 0.000567699, 0.000000000],
[0.003875109, 0.000004356, 0.000222694, 0.000008712, 0.002265624, 0.000004955, 0.000009909, 0.002489659, 0.000733858, 0.000000000, 0.002315219, 0.000518416, 0.000014265, 0.000004955, 0.003319977, 0.000024175, 0.000014864, 0.000490052, 0.000093109, 0.001143798, 0.000712077, 0.000004955, 0.000000000, 0.000000000, 0.000083798, 0.000000000],
[0.002501388, 0.000028531, 0.000019220, 0.000326047, 0.002625421, 0.000028531, 0.000106010, 0.000018023, 0.002259305, 0.000009909, 0.000008712, 0.000135307, 0.000032887, 0.000385072, 0.003365358, 0.000008712, 0.000000000, 0.000512001, 0.000624593, 0.000013069, 0.000502020, 0.000060221, 0.000029129, 0.000004356, 0.000562744, 0.000000000],
[0.005110413, 0.000229779, 0.001469080, 0.004485987, 0.004527036, 0.000749655, 0.000566430, 0.000134277, 0.000511929, 0.000004356, 0.000475284, 0.002631045, 0.001727558, 0.005933071, 0.000343736, 0.000784074, 0.000126426, 0.009417292, 0.005337679, 0.004787142, 0.000079441, 0.001300025, 0.000796975, 0.000798938, 0.001128312, 0.000031690],
[0.000453407, 0.000040403, 0.000018023, 0.000000000, 0.000954231, 0.001140113, 0.000004955, 0.000000000, 0.001615397, 0.000004356, 0.000000000, 0.000274969, 0.000013667, 0.000004356, 0.003193718, 0.000004356, 0.000000000, 0.001129437, 0.000036645, 0.000525931, 0.000481508, 0.000000000, 0.000009311, 0.000000000, 0.000107972, 0.000000000],
[0.000699343, 0.000004356, 0.000004356, 0.000009311, 0.002947351, 0.000004356, 0.000159050, 0.002047239, 0.000709420, 0.000017425, 0.000000000, 0.000158284, 0.000014864, 0.000276597, 0.002772193, 0.000038440, 0.000000000, 0.001001216, 0.000313409, 0.000172885, 0.000525501, 0.000004356, 0.000000000, 0.000004356, 0.000162641, 0.000000000],
[0.009215709, 0.000013069, 0.000004955, 0.000040403, 0.012985909, 0.000021781, 0.000013069, 0.000171090, 0.004396613, 0.000008712, 0.000000000, 0.000036645, 0.000070131, 0.000121472, 0.004448218, 0.000004356, 0.000000000, 0.000377819, 0.000042796, 0.001590241, 0.000343305, 0.000000000, 0.000018023, 0.000008712, 0.000247204, 0.000000000],
[0.000708917, 0.000239521, 0.002300546, 0.002033954, 0.001204858, 0.001548258, 0.002028282, 0.000008712, 0.000021781, 0.000000000, 0.000791494, 0.003694206, 0.001594621, 0.014429354, 0.001513599, 0.000367049, 0.000034084, 0.000955858, 0.005745034, 0.006256461, 0.000026736, 0.000837641, 0.000000000, 0.000100624, 0.000000000, 0.000252590],
[0.000221067, 0.000004356, 0.000004356, 0.000000000, 0.000219535, 0.000000000, 0.000004356, 0.000013069, 0.000112329, 0.000013069, 0.000008712, 0.000000000, 0.000000000, 0.000000000, 0.000423943, 0.000009311, 0.000000000, 0.000000000, 0.000000000, 0.000004955, 0.001201244, 0.000000000, 0.000009909, 0.000000000, 0.000000000, 0.000000000],
[0.000335191, 0.000088585, 0.000000000, 0.000000000, 0.002802973, 0.000013069, 0.000004955, 0.000014864, 0.001257635, 0.000000000, 0.000013069, 0.000048948, 0.000024773, 0.000986256, 0.000014864, 0.000000000, 0.000000000, 0.000009909, 0.001097220, 0.000000000, 0.000018023, 0.000004955, 0.000004356, 0.000000000, 0.000155460, 0.000000000],
[0.002755078, 0.000042796, 0.000081237, 0.001902070, 0.004647910, 0.000148543, 0.000059025, 0.000004356, 0.002704671, 0.000000000, 0.000435049, 0.006791081, 0.000170324, 0.000018622, 0.002797229, 0.000232005, 0.000000000, 0.000239258, 0.000752551, 0.000293328, 0.000423177, 0.000065774, 0.000099427, 0.000000000, 0.002147216, 0.000008712],
[0.002690070, 0.000526961, 0.000052107, 0.000004356, 0.006593160, 0.000028531, 0.000030494, 0.000009311, 0.001653310, 0.000000000, 0.000000000, 0.000031690, 0.000462718, 0.000040403, 0.002097838, 0.000564204, 0.000000000, 0.000044161, 0.000320925, 0.000000000, 0.000505251, 0.000004955, 0.000070298, 0.000000000, 0.001499191, 0.000000000],
[0.001184608, 0.000055865, 0.001243561, 0.005932161, 0.004617943, 0.000347757, 0.007902184, 0.000013667, 0.001866168, 0.000093276, 0.001819278, 0.000362692, 0.000060820, 0.000943891, 0.004477706, 0.000022978, 0.000000000, 0.000162306, 0.001328986, 0.004165900, 0.000551901, 0.000172981, 0.000036047, 0.000009311, 0.000930319, 0.000004356],
[0.000301107, 0.000709587, 0.000519277, 0.001407806, 0.000360730, 0.002300738, 0.000234136, 0.000616120, 0.001115675, 0.000071327, 0.001376355, 0.001921075, 0.003961013, 0.008657416, 0.003278186, 0.001312232, 0.000008712, 0.007035676, 0.001190592, 0.002998669, 0.012564480, 0.001084583, 0.004102184, 0.000070131, 0.000224059, 0.000022978],
[0.001330351, 0.000004955, 0.000013069, 0.000072524, 0.001878231, 0.000004356, 0.000014864, 0.000365253, 0.000825411, 0.000000000, 0.000000000, 0.001922056, 0.000158284, 0.000004955, 0.001207179, 0.000952268, 0.000000000, 0.001902501, 0.000267621, 0.000222264, 0.000373631, 0.000000000, 0.000004955, 0.000000000, 0.000218506, 0.000000000],
[0.000000000, 0.000004356, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000550202, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000],
[0.002166293, 0.000082003, 0.000333659, 0.001006864, 0.010886587, 0.000114291, 0.000414034, 0.000027933, 0.002941870, 0.000000000, 0.000816794, 0.000444862, 0.000517315, 0.000719161, 0.003569574, 0.000174776, 0.000000000, 0.001359719, 0.001435235, 0.001035563, 0.000495605, 0.000144617, 0.000172981, 0.000000000, 0.001716954, 0.000004356],
[0.001443948, 0.000050312, 0.000701306, 0.000225686, 0.004369446, 0.000098829, 0.000036645, 0.002296765, 0.001814012, 0.000004955, 0.000533280, 0.000446825, 0.000136671, 0.000344071, 0.003785615, 0.000524998, 0.000008712, 0.000021781, 0.002242383, 0.005444598, 0.001518267, 0.000000000, 0.000315540, 0.000000000, 0.000165369, 0.000004356],
[0.002525203, 0.000022978, 0.000362525, 0.000018023, 0.004908542, 0.000069700, 0.000009909, 0.016670181, 0.004619666, 0.000000000, 0.000014864, 0.000462551, 0.000193565, 0.000047751, 0.009152160, 0.000019220, 0.000000000, 0.001568340, 0.001512786, 0.001314530, 0.000911865, 0.000013667, 0.000257975, 0.000032289, 0.000703867, 0.000004356],
[0.000397638, 0.000237726, 0.000766721, 0.000335526, 0.000893339, 0.000160247, 0.000763657, 0.000056631, 0.000427366, 0.000017425, 0.000029129, 0.001999966, 0.000609394, 0.001897619, 0.000000000, 0.001560705, 0.000000000, 0.003343170, 0.002965518, 0.002995940, 0.000069700, 0.000021781, 0.000004356, 0.000017425, 0.000377293, 0.000059623],
[0.000465040, 0.000004955, 0.000008712, 0.000013069, 0.005563533, 0.000000000, 0.000000000, 0.000004356, 0.001148921, 0.000000000, 0.000000000, 0.000000000, 0.000004356, 0.000004356, 0.000177505, 0.000004955, 0.000000000, 0.000004356, 0.000009311, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000018023, 0.000000000],
[0.003023609, 0.000009311, 0.000009311, 0.000014265, 0.004504250, 0.000004356, 0.000000000, 0.003163847, 0.003231320, 0.000000000, 0.000004356, 0.000073888, 0.000023576, 0.000386101, 0.001832873, 0.000000000, 0.000000000, 0.000101223, 0.000171952, 0.000039206, 0.000004356, 0.000000000, 0.000069700, 0.000000000, 0.000050910, 0.000000000],
[0.000067737, 0.000004356, 0.000111299, 0.000000000, 0.000070729, 0.000000000, 0.000000000, 0.000004356, 0.000076282, 0.000000000, 0.000000000, 0.000014864, 0.000008712, 0.000000000, 0.000004955, 0.000168625, 0.000000000, 0.000000000, 0.000004356, 0.000308622, 0.000014864, 0.000000000, 0.000000000, 0.000008712, 0.000008712, 0.000000000],
[0.000151702, 0.000140429, 0.000037243, 0.000045357, 0.001554793, 0.000004356, 0.000004356, 0.000004356, 0.000472627, 0.000000000, 0.000004356, 0.000112496, 0.000145982, 0.000169223, 0.007658930, 0.000092510, 0.000000000, 0.000031092, 0.000652693, 0.000263097, 0.000053472, 0.000000000, 0.000044759, 0.000000000, 0.000039206, 0.000000000],
[0.000120443, 0.000000000, 0.000000000, 0.000000000, 0.000213384, 0.000000000, 0.000000000, 0.000000000, 0.000054070, 0.000000000, 0.000000000, 0.000009311, 0.000000000, 0.000000000, 0.000009311, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000004356, 0.000000000, 0.000000000, 0.000000000, 0.000052873, 0.000098829]])

#travel time
tim =np.array([[127, 204, 323, 408, 474, 527, 573, 612, 647, 678, 221, 303, 384, 452, 508, 555, 596, 632, 664, 369, 422, 475, 524, 566, 605, 639],
[204, 127, 204, 323, 408, 474, 527, 573, 612, 647, 221, 221, 303, 384, 452, 508, 555, 596, 632, 329, 369, 422, 475, 524, 566, 605],
[323, 204, 127, 204, 323, 408, 474, 527, 573, 612, 303, 221, 221, 303, 384, 452, 508, 555, 596, 329, 329, 369, 422, 475, 524, 566],
[408, 323, 204, 127, 204, 323, 408, 474, 527, 573, 384, 303, 221, 221, 303, 384, 452, 508, 555, 369, 329, 329, 369, 422, 475, 524],
[474, 408, 323, 204, 127, 204, 323, 408, 474, 527, 452, 384, 303, 221, 221, 303, 384, 452, 508, 422, 369, 329, 329, 369, 422, 475],
[527, 474, 408, 323, 204, 127, 204, 323, 408, 474, 508, 452, 384, 303, 221, 221, 303, 384, 452, 475, 422, 369, 329, 329, 369, 422],
[573, 527, 474, 408, 323, 204, 127, 204, 323, 408, 555, 508, 452, 384, 303, 221, 221, 303, 384, 524, 475, 422, 369, 329, 329, 369],
[612, 573, 527, 474, 408, 323, 204, 127, 204, 323, 596, 555, 508, 452, 384, 303, 221, 221, 303, 566, 524, 475, 422, 369, 329, 329],
[647, 612, 573, 527, 474, 408, 323, 204, 127, 204, 632, 596, 555, 508, 452, 384, 303, 221, 221, 605, 566, 524, 475, 422, 369, 329],
[678, 647, 612, 573, 527, 474, 408, 323, 204, 127, 664, 632, 596, 555, 508, 452, 384, 303, 221, 639, 605, 566, 524, 475, 422, 369],
[221, 221, 303, 384, 452, 508, 555, 596, 632, 664, 127, 204, 323, 408, 474, 527, 573, 612, 647, 259, 346, 420, 481, 532, 576, 615],
[303, 221, 221, 303, 384, 452, 508, 555, 596, 632, 204, 127, 204, 323, 408, 474, 527, 573, 612, 204, 259, 346, 420, 481, 532, 576],
[384, 303, 221, 221, 303, 384, 452, 508, 555, 596, 323, 204, 127, 204, 323, 408, 474, 527, 573, 259, 204, 259, 346, 420, 481, 532],
[452, 384, 303, 221, 221, 303, 384, 452, 508, 555, 408, 323, 204, 127, 204, 323, 408, 474, 527, 346, 259, 204, 259, 346, 420, 481],
[508, 452, 384, 303, 221, 221, 303, 384, 452, 508, 474, 408, 323, 204, 127, 204, 323, 408, 474, 420, 346, 259, 204, 259, 346, 420],
[555, 508, 452, 384, 303, 221, 221, 303, 384, 452, 527, 474, 408, 323, 204, 127, 204, 323, 408, 481, 420, 346, 259, 204, 259, 346],
[596, 555, 508, 452, 384, 303, 221, 221, 303, 384, 573, 527, 474, 408, 323, 204, 127, 204, 323, 532, 481, 420, 346, 259, 204, 259],
[632, 596, 555, 508, 452, 384, 303, 221, 221, 303, 612, 573, 527, 474, 408, 323, 204, 127, 204, 576, 532, 481, 420, 346, 259, 204],
[664, 632, 596, 555, 508, 452, 384, 303, 221, 221, 647, 612, 573, 527, 474, 408, 323, 204, 127, 615, 576, 532, 481, 420, 346, 259],
[369, 329, 329, 369, 422, 475, 524, 566, 605, 639, 259, 204, 259, 346, 420, 481, 532, 576, 615, 127, 204, 323, 408, 474, 527, 573],
[422, 369, 329, 329, 369, 422, 475, 524, 566, 605, 346, 259, 204, 259, 346, 420, 481, 532, 576, 204, 127, 204, 323, 408, 474, 527],
[475, 422, 369, 329, 329, 369, 422, 475, 524, 566, 420, 346, 259, 204, 259, 346, 420, 481, 532, 323, 204, 127, 204, 323, 408, 474],
[524, 475, 422, 369, 329, 329, 369, 422, 475, 524, 481, 420, 346, 259, 204, 259, 346, 420, 481, 408, 323, 204, 127, 204, 323, 408],
[566, 524, 475, 422, 369, 329, 329, 369, 422, 475, 532, 481, 420, 346, 259, 204, 259, 346, 420, 474, 408, 323, 204, 127, 204, 323,],
[605, 566, 524, 475, 422, 369, 329, 329, 369, 422, 576, 532, 481, 420, 346, 259, 204, 259, 346, 527, 474, 408, 323, 204, 127, 204,],
[639, 605, 566, 524, 475, 422, 369, 329, 329, 369, 615, 576, 532, 481, 420, 346, 259, 204, 259, 573, 527, 474, 408, 323, 204, 127,]])


# Numpy Look Up Array for Alphabets
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Possible Intial Solutions


init_sol = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def obj(r):
    cost=0
    for i in range(0,len(r)):
        for j in range(0,len(r)):
            cost = cost + pro[i][j]*tim[r.index(alpha[i])][r.index(alpha[j])] 
    return cost


# ti is intial temp
# tf is final temp
# n is total no of iteration for 1 temp 
# factor is by which temp decarese after one iteration.
# p is thresold probability by which we accept the inferior solutions 
# k is boltzmen const parameter in heat eq
# r is intial solution array passed

def simulated_annealing(ti,tf,n,factor,p,k,r):
    ni = 0
    while(ti>tf):
        while(ni<n):
            # Cost till that point
            obj1=obj(r)
            # randomly genrating a points that can be swapped 
            i = random.randint(0,len(r)-1) 
            j = random.randint(0,len(r)-1)
            # new sol
            r_new = []
            # new solution 
            for k in range(0,len(r)):
                r_new.append(r[k])
            temp = r_new[i]
            r_new[i] = r_new[j]
            r_new[j] = temp
            # New Cost of the Keyboard Obtained
            obj2 = obj(r_new)
            # Direct Acceptance
            if(obj2<obj1):
                for i in range(0,len(r_new)):
                    r[i] = r_new[i]
            # Calculating the Acceptance Probability 
            prob = np.exp((-(obj2-obj1))/(k*ti))
            # Checking with the threshold Probability
            if(prob > p):
                for i in range(0,len(r_new)):
                    r[i] = r_new[i]
            ni = ni + 1
        ti = ti*factor
        ni = 0
    return r

def print_keyboard_layout(r):
  print('Key Board Layout: ')
  for i in range(0,10):
      print(r[i], end =' ')
  print()
  for i in range(10,19):
      print(r[i], end =' ')
  print()
  for i in range(19,26):
      print(r[i], end =' ')
  print()


print("intial solution:    ")
print_keyboard_layout(alpha)
print("Objective value is: ",obj(alpha))

print("__________________________________________________________________")
r = simulated_annealing(2000,1,50,0.99,0.9,1,init_sol)
print_keyboard_layout(r)
print("Objective value is: ", obj(r))

# by increasing temp by 1000
print("__________________________________________________________________")
r = simulated_annealing(3000,1,50,0.99,0.9,1,init_sol)
print_keyboard_layout(r)
print("Objective value is: ", obj(r))

# by increasing k by 1 
print("__________________________________________________________________")
r = simulated_annealing(2000,1,50,0.99,0.9,2,init_sol)
print_keyboard_layout(r)
print("Objective value is: ", obj(r))

# by decreasing a factor of chaning a temp by 0.1

print("__________________________________________________________________")
r = simulated_annealing(2000,1,50,0.89,0.9,1,init_sol)
print_keyboard_layout(r)
print("Objective value is: ", obj(r))

# by increasing a no of loops in 1 temp by 10 
print("__________________________________________________________________")
r = simulated_annealing(2000,1,60,0.99,0.9,1,init_sol)
print_keyboard_layout(r)
print("Objective value is: ", obj(r))




