class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


# Single input simulation
commands = ["TimeMap", "set", "get", "get", "set", "get", "get"]
args = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

obj = None
result = []

for cmd, arg in zip(commands, args):
    if cmd == "TimeMap":
        obj = TimeMap()
        result.append(None)
    elif cmd == "set":
        obj.set(*arg)
        result.append(None)
    elif cmd == "get":
        res = obj.get(*arg)
        result.append(res)

print(result)
