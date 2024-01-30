import heapq


def min_cost_to_connect_cables(cables):
    cables = cables[:]
    heapq.heapify(cables)

    while len(cables) > 1:
        cable_1 = heapq.heappop(cables)
        cable_2 = heapq.heappop(cables)

        heapq.heappush(cables, cable_1 + cable_2)

    return heapq.heappop(cables)


if __name__ == "__main__":
    cable_lengths = [4, 3, 2, 6, 1, 7]
    min_total_cost = min_cost_to_connect_cables(cable_lengths)
    print("Мінімальні витрати для об'єднання кабелів:", min_total_cost)
