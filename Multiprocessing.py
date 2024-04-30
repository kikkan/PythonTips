import concurrent.futures
import numpy as np
import multiprocessing
from time import perf_counter as pf


def doSomething(a=1, s=1, method=0):
    # print(f"started {a}")
    b = 0.123
    for i in range(10000):
        for j in range(i):
            b = j*i
    # print(f"done sleep {a}")
    ret = f'task {a}, slept for {s} sek'
    if method != 0:
        method.put(ret)
    else:
        return ret


# %% First try


# %% pool
if __name__ == "__main__":
    tasks = 8
    start = pf()
    if True:
        q = multiprocessing.Queue()

        ps = []
        for i in range(tasks):
            p = multiprocessing.Process(target=doSomething, args=[i, i-1, q])
            p.start()
            ps.append(p)
        rets = []
        for p in ps:
            rets.append(q.get())
            p.join()

        # for val in rets:
        #     print(f'{val}')

    print('Done 1')
    endMult1 = pf()
    if True:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            secs = [3, 1, 1, 3, 2, 1, 2, 1, 2, 3, 1, 1]
            pl = [executor.submit(doSomething, i, secs[i]) for i in range(tasks)]

            # for f in concurrent.futures.as_completed(pl):
            #     print(f.result())
            # print()

            # for f in pl:
            #     print(f.result())
    print('Done 2')
    endMult2 = pf()

    for i in range(tasks):
        temp = doSomething(i, secs[i])
    print('Done 3')
    endsing = pf()

    print(f'Single: {round(endsing - endMult2,2)}\n'
          f'Multi2: {round(endMult2 - endMult1,2)}\n'
          f'Multi1: {round(endMult1 - start,2)}')
