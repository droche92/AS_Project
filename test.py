import psutil
import pandas

def cpu():
    #using psutil to read the cpu usage
    count = psutil.cpu_count()
    freq = psutil.cpu_freq()
    percent = psutil.cpu_percent()

    #putting the values of count, freq and percent into a list called cpu_things
    cpu_things = [count, freq, percent]


    #iterating the list
    for x in cpu_things:
        print(x)

    cpu_data = {'data': [count, freq, percent]}
    df = pandas.DataFrame(cpu_data, columns=['data'])

    df.to_csv('example.csv')

    return count, freq, percent


def memory():
    vm = psutil.virtual_memory()

    return vm

cpu()
memory()

