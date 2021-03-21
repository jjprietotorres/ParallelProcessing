#Kudus @vacarezzad !!
from tqdm import tqdm
import psutil
import multiprocessing
from joblib import Parallel, delayed

inputs = tqdm(your_list)

print('Physical Cores',psutil.cpu_count(logical = False))
print('Locgical Cores',psutil.cpu_count(logical = True))

#logical cores available
num_cores = multiprocessing.cpu_count()

processed_list = Parallel(n_jobs=num_cores)(delayed(your_function)(i,parameters) for i in inputs)
