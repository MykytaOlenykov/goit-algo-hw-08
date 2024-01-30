import heapq


def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        cable_1 = heapq.heappop(cables)
        cable_2 = heapq.heappop(cables)

        total_cost += cable_1 + cable_2

        heapq.heappush(cables, cable_1 + cable_2)

    return total_cost


if __name__ == "__main__":
    cable_lengths = [4, 3, 2, 6, 7, 1]
    min_total_cost = min_cost_to_connect_cables(cable_lengths)
    print("Мінімальні витрати для об'єднання кабелів:", min_total_cost)
