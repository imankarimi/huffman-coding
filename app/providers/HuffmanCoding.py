import heapq


class HuffmanCoding:

    @staticmethod
    def encode(info):
        heap = [[weight, [code, '']] for code, weight in info.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            low = heapq.heappop(heap)
            high = heapq.heappop(heap)
            for pair in low[1:]:
                pair[1] = '0' + pair[1]
            for pair in high[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

        result = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
        return result

