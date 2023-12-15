data = {
    "id": "a91688f0-8ac0-4f9f-8448-5e9948511ce1",
    "type": "Public",
    "header": {
        "lastName": "Boukrouh",
        "firstName": "Aymane"
    },
    "subtype": "API",
    "line_items": [
        {
            "description": "Description of 0001",
            "number": "0001"
        },
        {
            "description": "Description of 0002",
            "number": "0002"
        },
        {
            "description": "Description of 0003",
            "number": "0003"
        }
    ],
    "clauses": [
        {
            "date": "Nov. 1st, 2023",
            "number": "1.1.1.1"
        },
        {
            "date": "Nov. 2nd, 2023",
            "number": "2.2.2.2"
        }
    ]
}

transformations = {
  "identifier": {
    "type": "string",
    "required": True,
    "path": "id"
  },
  "type": {
    "type": "string",
    "required": True,
    "path": "type"
  },
  "header": {
    "type": "object",
    "required": True,
    "mapping": {
      "lastName": {
        "type": "string",
        "required": True,
        "path": "header.lastName"
      },
      "firstName": {
        "type": "string",
        "required": True,
        "path": "header.firstName"
      }
    }
  },
  "subtype": {
    "type": "string",
    "required": False,
    "path": "subtype"
  },
  "line_items": {
    "type": "array[object]",
    "required": True,
    "path": "line_items",
    "mapping": {
      "number": {
        "type": "string",
        "required": True,
        "path": "number"
      }
    }
  },
  "clauses": {
    "type": "array[object]",
    "required": True,
    "path": "clauses",
    "mapping": {
      "date": {
        "type": "string",
        "required": True,
        "path": "date"
      },
      "number": {
        "type": "string",
        "required": True,
        "path": "number"
      }
    }
  }
}


def process_transformations(data, transformations):
    output = {}
    messages = []

    def get_from_data(path, data, required=False):
        parts = path.split(".", 1)
        if len(parts) == 1:
            value = data.get(parts[0])
            if value is None and required:
                messages.append({"type": "error", "message": f"Required path '{path}' not found in data."})
            elif value is None:
                messages.append({"type": "warning", "message": f"Path '{path}' not found in data."})
            return value
        else:
            new_data = data.get(parts[0])
            if new_data is None and required:
                messages.append({"type": "error", "message": f"Required path '{path}' not found in data."})
                return None
            return get_from_data(parts[1], new_data, required)

    def get_transformed_item(data, transformations):
        result, _ = process_transformations(data, transformations)
        return result

    #def check_unused_data_keys(data, transformations):
    #    for key in data:
    #        if key not in transformations:
    #            messages.append({"type": "warning", "message": f"Key '{key}' in data not mapped in transformations."})
    #        elif isinstance(data[key], dict):
    #            check_unused_data_keys(data[key], transformations[key].get('mapping', {}))

    for key, transform in transformations.items():
        if transform['type'] == 'string':
            output[key] = get_from_data(transform['path'], data, transform.get('required', False))
        elif transform['type'] == 'array[object]':
            array_data = get_from_data(transform['path'], data, transform.get('required', False)) or []
            output[key] = [get_transformed_item(item, transform['mapping']) for item in array_data]

    #check_unused_data_keys(data, transformations)
    
    return output, messages

# Test with the given data and transformations
import json

transformed_data, messages = process_transformations(data, transformations)
print(json.dumps(transformed_data, indent=4))
print(json.dumps(messages, indent=4))
