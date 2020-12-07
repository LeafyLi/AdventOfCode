with open('input.txt') as f:
    lines = [x.replace('.', '').strip() for x in f.readlines()]

graph = {}
all_colors = set()
for line in lines:
    outer_bag, held_items = line.split(' contain ')
    outer_bag_color = ' '.join(outer_bag.split(' ')[:2])
    all_colors.add(outer_bag_color)
    if held_items == 'no other bags':
        graph[outer_bag_color] = set()
        continue
    for item in held_items.split(', '):
        bag_color = ' '.join(item.split(' ')[1:3])
        if outer_bag_color not in graph:
            graph[outer_bag_color] = set()
        if bag_color not in graph:
            graph[bag_color] = set()
        graph[outer_bag_color].add(bag_color)
        all_colors.add(bag_color)


def bfs(start_vertex, end_vertex, graph):
    visited = set([start_vertex])
    paths = [[start_vertex]]
    while paths:
        cur_path = paths.pop()
        cur_node = cur_path[-1]
        # Add memo if slow
        if cur_node == end_vertex:
            return True
        for neighbor in graph[cur_node]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            new_path = list(cur_path)
            new_path.append(neighbor)
            paths.append(new_path)
    return False


# Assume dag
total_start_vertices = 0
memo_table = set()  # Vertices that can already see it
for color in all_colors:
    total_start_vertices += bfs(color, 'shiny gold', graph)
print(total_start_vertices - 1)




# pt 2
graph = {}
all_colors = set()
for line in lines:
    outer_bag, held_items = line.split(' contain ')
    outer_bag_color = ' '.join(outer_bag.split(' ')[:2])
    all_colors.add(outer_bag_color)
    if held_items == 'no other bags':
        graph[outer_bag_color] = {}
        continue
    for item in held_items.split(', '):
        bag_color = ' '.join(item.split(' ')[1:3])
        if outer_bag_color not in graph:
            graph[outer_bag_color] = {}
        if bag_color not in graph:
            graph[bag_color] = {}
        graph[outer_bag_color][bag_color] = int(str(item.split(' ')[0]))
        all_colors.add(bag_color)


def bfs(start_vertex, graph):
    if graph[start_vertex] == dict():
        return 1
    return sum([graph[start_vertex][neighbor] * bfs(neighbor, graph) for neighbor in graph[start_vertex]]) + 1


print(bfs('shiny gold', graph) - 1)
