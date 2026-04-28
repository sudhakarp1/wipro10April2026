def jobSequencing(jobs):
    jobs.sort(key=lambda x: x[1], reverse=True )
    maxDeadLine = max(j[2] for j in jobs)
    slots = [None] * (maxDeadLine + 1)

    profit = 0
    for job, p, d in jobs:
        for i in range(d, 0, -1):
            if slots[i] is None:
                slots[i], profit = job, profit + p
                break

    print(f'Jobs scheduled: {maxDeadLine} --> ', [j for j in slots if j])
    print(f'Total Profit: ', profit)


if __name__ == '__main__':
    jobs = [('j1',100, 2), ('j2',19,1), ('j3',40, 2), ('j4',30,1), ('j5',55, 3) ]

    jobSequencing(jobs)