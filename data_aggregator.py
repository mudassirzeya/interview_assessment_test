from typing import List, Dict, Callable

def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    grouped_data = {}
    for item in data:
        group_key = item[key]
        if group_key not in grouped_data:
            grouped_data[group_key] = []
        grouped_data[group_key].append(item)

    return {k: aggregator(v) for k, v in grouped_data.items()}

# Example usage:
if __name__ == "__main__":
    data = [{'category': 'A', 'value': 10}, {'category': 'A', 'value': 20}, {'category': 'B', 'value': 5}]
    result = aggregate_data(data, 'category', lambda x: sum(item['value'] for item in x))
    print(result)
