class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}

        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1

        max_freq = 0
        for value in freq.values():
            if value > max_freq:
                max_freq = value

        max_count = 0
        for value in freq.values():
            if value == max_freq:
                max_count += 1

        part_count = max_freq - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - (max_freq * max_count)

        if empty_slots - available_tasks > 0:
            idles = empty_slots - available_tasks
        else:
            idles = 0

        return len(tasks) + idles
