from typing import Tuple, List
from math import log

rates = [[1, 0.23, 0.25, 16.43, 18.21, 4.94,],
        [4.34, 1, 1.11, 71.40, 79.09, 21.44],
        [3.93, 0.90, 1, 64.52, 71.48, 19.37],
        [0.061, 0.014, 0.015, 1, 1.11, 0.30],
        [0.055, 0.013, 0.014, 0.90, 1, 0.27],
        [0.20, 0.047, 0.052, 3.33, 3.69,1]]

currencies = ("PLN", "EUR", "USD", "RUB", "INR", "MXN")

def negate_log_convertor(graph: Tuple[Tuple[float]]) -> List[List[float]]:
    result = [[-log(edge) for edge in row] for row in graph]
    return result

def arbitrage(currency_tuple: tuple, rates_matrix: Tuple[Tuple[float, ...]]):
    trans_graph = negate_log_convertor(rates_matrix)
    source = 0
    n = len(trans_graph)
    min_dist = [float('inf')] * n

    pre = [-1] * n
    min_dist[source] = source

    #Relaxation |V-1| times
    for _ in range(n):
        for source_cur in range(n):
            for dest_cur in range(n):
                if min_dist[dest_cur] > min_dist[source_cur]+trans_graph[source_cur][dest_cur]:
                    min_dist[dest_cur] = min_dist[source_cur]+trans_graph[source_cur][dest_cur]
                    pre[dest_cur] = source_cur

    #If we can still relax the edges then we have a negative cycle
    for source_cur in range(n):
        for dest_cur in range(n):
            if min_dist[dest_cur] > min_dist[source_cur]+trans_graph[source_cur][dest_cur]:
                print_cycle = [dest_cur, source_cur]
                while pre[source_cur] not in print_cycle:
                    print_cycle.append(pre[source_cur])
                    source_cur = pre[source_cur]
                print_cycle.append(pre[source_cur])
                print("Arbitrage opportunity: \n")
                print("-->".join([currencies[p] for p in print_cycle[::-1]]))

if __name__ == "__main__":
    arbitrage(currencies, rates)
            