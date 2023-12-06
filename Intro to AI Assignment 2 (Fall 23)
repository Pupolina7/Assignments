import os
import random

GRID_SIZE = 20
GENERATIONS = 5000


def scan_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words


def in_grid(x, y):
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE


def print_crossword(solution, words):
    answer = [['-' for _ in range(20)] for _ in range(20)]
    for index, sol in enumerate(solution):
        x = int(sol[0])
        y = int(sol[1])
        if sol[2] == 1:
            for i in range(x, min(x + len(words[index]), 20)):
                answer[i][y] = words[index][i - x]
        if sol[2] == 0:
            for i in range(y, min(y + len(words[index]), 20)):
                answer[x][i] = words[index][i - y]
    for i in answer:
        for j in i:
            print(j, end=' ')
        print()
    print()


def count_intersections(words, places):
    grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    word_positions = {}

    # Check for invalid placement and populate word_positions dictionary
    for i in range(len(words)):
        word = words[i]
        x, y, orientation = places[i]
        word_positions[i] = set()
        if x + len(word) >= GRID_SIZE:
            return -1, -1
        for j in range(len(word)):
            if orientation == 1:
                if not in_grid(x + j, y):
                    return -1, -1  # Invalid placement
                if grid[x + j][y] != ' ' and grid[x + j][y] != word[j]:
                    return -1, -1  # Different letters in the same grid cell
                word_positions[i].add((x + j, y))
            elif orientation == 0:
                if not in_grid(x, y + j):
                    return -1, -1  # Invalid placement
                if grid[x][y + j] != ' ' and grid[x][y + j] != word[j]:
                    return -1, -1  # Different letters in the same grid cell
                word_positions[i].add((x, y + j))

    # Count intersections and check connectivity
    intersections = 0
    disconnected = set(range(len(words)))

    for i in range(len(words)):
        word = words[i]
        x, y, orientation = places[i]

        for j in range(len(word)):
            if orientation == 1:
                adjacent_positions = [(x + j, y - 1), (x + j, y + 1)]
            elif orientation == 0:
                adjacent_positions = [(x - 1, y + j), (x + 1, y + j)]

            for pos in adjacent_positions:
                if pos in word_positions[i]:
                    word_positions[i].remove(pos)
                    disconnected.discard(i)
                    intersections += 1

    return intersections // 2, len(disconnected)


def check_neighbours(words, places):
    grid = [[' ' for _ in range(20)] for _ in range(20)]
    invalid_placement = 0
    # Place words on the grid
    for i in range(len(words)):
        word = words[i]
        x, y, orientation = places[i]
        for j in range(len(word)):
            if orientation == 1:
                if grid[x + j][y] == word[j] or grid[x + j][y] == ' ':
                    grid[x + j][y] = word[j]
                else:
                    invalid_placement = -1
                break
            elif orientation == 0:
                if grid[x][y + j] == word[j] or grid[x][y + j] == ' ':
                    grid[x + j][y] = word[j]
                else:
                    invalid_placement = -1
                break
        if invalid_placement == -1:
            return -1, -1
    # Count perpendicular intersections
    neighbours = 0
    stacked = 0
    for i in range(len(words)):
        word = words[i]
        x, y, orientation = places[i]
        if orientation == 1:
            if 0 <= y - 1 < GRID_SIZE:
                neighbour = grid[x:x + len(word) - 1][y - 1:]
                letters_together = 0
                for k, _ in enumerate(neighbour):
                    if neighbour[k] != ' ':
                        letters_together += 1
                        if letters_together > 1:
                            neighbours += 1
                    else:
                        letters_together = 0
            if 0 <= y + 1 < GRID_SIZE:
                neighbour = grid[x:x + len(word) - 1][y + 1:]
                letters_together = 0
                for k, _ in enumerate(neighbour):
                    if neighbour[k] != ' ':
                        letters_together += 1
                        if letters_together > 1:
                            neighbours += 1
                    else:
                        letters_together = 0
            if 0 <= x - 1 < GRID_SIZE:
                if grid[x - 1][y] != ' ':
                    stacked += 1
            if 0 <= x + len(word) < GRID_SIZE:
                if grid[x + len(word)][y] != ' ':
                    stacked += 1
        if orientation == 0:
            if 0 <= x - 1 < GRID_SIZE:
                neighbour = grid[x - 1][y:y + len(word) - 1]
                letters_together = 0
                for k, _ in enumerate(neighbour):
                    if neighbour[k] != ' ':
                        letters_together += 1
                        if letters_together != 1:
                            neighbours += 1
                    else:
                        letters_together = 0
            if 0 <= x + 1 < GRID_SIZE:
                neighbour = grid[x + 1][y:y + len(word) - 1]
                letters_together = 0
                for k, _ in enumerate(neighbour):
                    if neighbour[k] != ' ':
                        letters_together += 1
                        if letters_together != 1:
                            neighbours += 1
                    else:
                        letters_together = 0
            if 0 <= y - 1 < GRID_SIZE:
                if grid[x][y - 1] != ' ':
                    stacked += 1
            if 0 <= y + len(word) < GRID_SIZE:
                if grid[x][y + len(word)] != ' ':
                    stacked += 1

    return neighbours, stacked


def place_randomly(words):
    places = []
    for i, word in enumerate(words):
        orientation = random.randint(0, 1)
        if orientation == 0:
            places.append([random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - len(word)), 0])
        if orientation == 1:
            places.append([random.randint(0, GRID_SIZE - len(word)), random.randint(0, GRID_SIZE - 1), 1])
    return places


def create_population(words):
    return [place_randomly(words) for _ in range(len(words))]


def fitness(places, words):
    start_in_grid = sum(1 for index, _ in enumerate(words) if in_grid(places[index][0], places[index][1]))
    end_in_grid = sum(1 for index, word in enumerate(words) if
                      places[index][2] == 1 and in_grid(places[index][0] + len(word) - 1, places[index][1]) or
                      places[index][2] == 0 and in_grid(places[index][0], places[index][1] + len(word) - 1))

    if start_in_grid == end_in_grid == len(words):
        intersections, disconnected = count_intersections(words, places)
        invalid_grid = 0
        neighbours, stacked = check_neighbours(words, places)

        if intersections == -1 or neighbours == -1:
            invalid_grid = -1 * 1000 ** (2 * len(words))
            intersections = 0
            disconnected = 0
            neighbours = 0
            stacked = 0

        fit_value = 10000 ** (start_in_grid + end_in_grid)

        fit_value += 300 * intersections
        fit_value -= 100 ** disconnected
        fit_value -= 100 * neighbours
        fit_value -= 200 * stacked
        fit_value += invalid_grid
    else:
        fit_value = -1 * 1000 ** (2 * len(words) - (start_in_grid + end_in_grid))

    return fit_value


def crossover(words, places):
    index1 = random.randint(0, len(words) - 1)
    index2 = random.randint(0, len(words) - 1)
    parent1 = words[index1]
    parent2 = words[index2]
    while not any(i in parent1 for i in parent2):
        index2 = random.randint(0, len(words) - 1)
        parent2 = words[index2]
    cross1 = cross2 = 0
    for i, let1 in enumerate(parent1):
        for j, let2 in enumerate(parent2):
            if let1 == let2:
                cross1 = i
                cross2 = j
                break
    if places[index1][2] == places[index2][2]:
        old_orientation = places[index2][2]
        places[index2][2] = 1 - old_orientation
    else:
        places[index1][2] = places[index2][2]
        places[index2][2] = 1 - places[index1][2]
    x, y = 0, 0
    if places[index1][2] == 0:
        x = random.randint(0, GRID_SIZE - len(words[index2]) + cross2)
        y = random.randint(0, GRID_SIZE - len(words[index1]) + cross1)
    if places[index1][2] == 1:
        x = random.randint(0, GRID_SIZE - len(words[index1]) + cross1)
        y = random.randint(0, GRID_SIZE - len(words[index2]) + cross2)
    if places[index1][2] == 0:
        places[index1][0] = x
        places[index1][1] = y - cross1
    if places[index2][2] == 0:
        places[index2][0] = x
        places[index2][1] = y - cross2
    if places[index1][2] == 1:
        places[index1][1] = y
        places[index1][0] = x - cross1
    if places[index2][2] == 1:
        places[index2][1] = y
        places[index2][0] = x - cross2
    return places


def mutate(words, places):
    index = random.randint(0, len(places) - 1)
    grid = [['-' for _ in range(20)] for _ in range(20)]
    for ind, place in enumerate(places):
        if ind != index:
            x = int(place[0])
            y = int(place[1])
            if place[2] == 1:
                for i in range(x, min(x + len(words[ind]), 20)):
                    grid[i][y] = words[ind][i - x]
            if place[2] == 0:
                for i in range(y, min(y + len(words[ind]), 20)):
                    grid[x][i] = words[ind][i - y]
    change = random.randint(0, 2)
    if change == 2:
        old_orientation = places[index][2]
        places[index][2] = 1 - old_orientation
        if places[index][2] == 0:
            if places[index][1] + len(words[index]) - 1 >= GRID_SIZE:
                change = random.randint(0, 1)
        if places[index][2] == 1:
            if places[index][0] + len(words[index]) - 1 >= GRID_SIZE:
                change = random.randint(0, 1)
    if change == 0 or change == 1:
        places[index][change] = random.randint(0, GRID_SIZE - len(words[index]))
    return places


def evolve(words):
    population = create_population(words)
    print_crossword(population[0], words)
    for i in range(GENERATIONS):
        population = sorted(population, key=lambda ind: fitness(ind, words), reverse=True)
        next_generation = population[:40]
        while len(next_generation) < 100:
            places = population[random.randint(0, len(population) - 1)]  # Select parents from the top 50 individuals
            child1 = mutate(words, places)
            next_generation.append(child1)
            child2 = crossover(words, child1)
            child1 = crossover(words, places)
            next_generation.append(child1)
            next_generation.append(child2)

        population = next_generation
        population = sorted(population, key=lambda ind: fitness(ind, words), reverse=True)
        if i % 100 == 0:
            print_crossword(population[0], words)
    population = sorted(population, key=lambda ind: fitness(ind, words), reverse=True)
    print(fitness(population[0], words))
    return population[0]


def save_output(output_dir, filename, solution):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, filename)
    with open(output_path, 'w') as file:
        for line in solution:
            file.write(f"{line[0]} {line[1]} {line[2]}\n")


def main(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            number_txt = filename[5:]
            words = scan_words(os.path.join(input_dir, filename))
            solution = evolve(words)
            print_crossword(solution, words)
            save_output(output_dir, 'output'+number_txt, solution)


if __name__ == "__main__":
    input_directory = "inputs"
    output_directory = "outputs"
    main(input_directory, output_directory)
