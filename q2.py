import matplotlib.pyplot as plt

def graphSnowfall(t):
    # initialize counts
    boundaries = [0, 10, 20, 30, 40, 50]
    counts = [0] * (len(boundaries) - 1)

    # Read data from the file and aggregate snowfall values into ranges
    with open(t, 'r') as file:
        for line in file:
            snowfall = int(line.strip())
            if 0 < snowfall <= 10:
                counts[0] += 1
            elif 11 <= snowfall <= 20:
                counts[1] += 1
            elif 21 <= snowfall <= 30:
                counts[2] += 1
            elif 31 <= snowfall <= 40:
                counts[3] += 1
            elif 41 <= snowfall <= 50:
                counts[4] += 1

    # plotting the bar chart
    plt.bar([f"{boundaries[i]}-{boundaries[i+1]}cms" for i in range(len(boundaries) - 1)], counts)
    plt.xlabel('Snowfall Range (cms)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Distribution')
    plt.show()

# file path
file_path = 'q2.txt'
graphSnowfall(file_path)
