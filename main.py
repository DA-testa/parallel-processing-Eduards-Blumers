# python3


def parallel_processing(n, m, data):
    output = []
    current = [0] * n  

    for job in range(m):
        index = 0
        min_time = current[0]

        
        for i in range(n):
            if current[i] < min_time:
                min_time = current[i]
                index = i

        
        output.append((index, current[index]))

        
        current[index] += data[job]

    return output


def main():
    input_str = input()
    n, m = map(int, input_str.split())
    data_str = input()
    data = list(map(int, data_str.split()))
    result = parallel_processing(n, m, data)

    for thread, start_time in result:
        print(thread, start_time)



if __name__ == "__main__":
    main()

