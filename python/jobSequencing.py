def take_input():
    n = int(input('Enter number of jobs: '))
    for i in range(n):
        temp_list = []
        temp_list.append(i+1)
        temp = int(input(f'Enter deadline slot of job {i+1}: '))
        temp_list.append(temp)
        temp = int(input(f'Enter profit of job {i+1}: '))
        temp_list.append(temp)
        Arr.append(temp_list)
    no_of_slots = max(Arr, key=lambda x: x[1])[1]
    return no_of_slots

def job_sequencing():
    k, i = no_of_slots, 0
    while k > 0:
        if i < len(Arr):
            deadline = Arr[i][1] - 1
        else:
            break
        while deadline >= 0:
            if Slot[deadline] == '-':
                Slot[deadline] = Arr[i][0]
                k -= 1
                break
            else:
                deadline -= 1
        i += 1

Arr = []
Slot = []
no_of_slots = take_input()
for i in range(no_of_slots):
    Slot.append('-')

Arr.sort(key=lambda x: x[2], reverse=True)
job_sequencing()

print(f'Solution Set: {Slot}\nOptimal Schedule: ', end='')
for i in range(no_of_slots):
    print(f'J{Slot[i]}', end=' ')
