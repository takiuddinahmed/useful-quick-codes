import re

data = {
    "455f0e29-b104-485a-b55a-9e14e119c200": {
        "contractor_name": "Lockheed Martin",
        "payment_term_display_value": "N30 - Net 30 Days",
        "payment_term_value": "N30",
        "line_items": [
            {
                "value": "100.00",
                "description": "CLIN 0001"
            },
            {
                "value": "200.00",
                "description": "CLIN 0002"
            },
            {
                "value": "100.00",
                "description": "CLIN 0001"
            },
            {
                "value": "200.00",
                "description": "CLIN 0002"
            },
                        {
                "value": "100.00",
                "description": "CLIN 0001"
            },
            {
                "value": "200.00",
                "description": "CLIN 0002"
            }
        ]
    }
}

substitutions = {
    "contractor": {
        "type": "string",
        "value": "{{outputs(455f0e29-b104-485a-b55a-9e14e119c200)[contractor_name]}}",
    },
    "line_items": {
        "type": "array",
        "value": "{{outputs(455f0e29-b104-485a-b55a-9e14e119c200)[line_items]}}",
        "items": {
            "value": {
                "type": "string",
                "value": "LAX - {{item().value}} {{item().description}}}}",
            },
            "description": {
                "type": "string",
                "value": "{{item().description}}",
            }
        }
    }
}


def substitute_string(source, data, item=None):
    """
    Replace placeholders in the source string.
    """
    pattern = r"{{outputs\(([^)]+)\)\[([^]]+)\]}}"

    def pattern_to_output_value(match):
        node_key, output_key = match.groups()
        if 'item()' in output_key:
            attribute = output_key.replace('item().', '')
            return item.get(attribute, "")
        return data.get(node_key, {}).get(output_key, "")

    source = re.sub(pattern, /Users/takiuddinahmed/Downloads/redis_test.py, source)

    if item:
        # Replace item placeholders with the actual values from the item dict.
        item_placeholders = re.findall(r"{{item\(\)\.([^}]+)}}", source)
        for ph in item_placeholders:
            source = source.replace("{{item().%s}}" % ph, item.get(ph, ""))
    
    return source

def process_substitution(sub, data):
    if 'type' in sub:
        if sub['type'] == 'string':
            return substitute_string(sub['value'], data)
        elif sub['type'] == 'array':
            pattern = r"{{outputs\(([^)]+)\)\[([^]]+)\]}}"
            match = re.search(pattern, sub['value'])
            if match:
                node_key, output_key = match.groups()
                array_items = data[node_key][output_key]
                # Process each item in the array to a dict dynamically
                return [
                    {
                        key: substitute_string(sub['items'][key]['value'], data, item)
                        for key in sub['items']
                    } for item in array_items
                ]

def apply_substitutions(substitutions, data):
    results = {}
    for key, sub in substitutions.items():
        results[key] = process_substitution(sub, data)
    return results

# Use the function:
result = apply_substitutions(substitutions, data)
print(result)