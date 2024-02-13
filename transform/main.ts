import { source } from "./source";
import * as fs from "fs";

const main = () => {
  const transformed = transform(source);
  save(transformed);
};

const save = (obj: any) => {
  const json = JSON.stringify(obj, null, 2);
  console.log(json);
  fs.writeFileSync("transformed.json", json);
};

const transform = (obj: any) => {
  const mappings: any = {};

  for (let key in obj) {
    if (typeof obj[key] === "object") {
      if (Array.isArray(obj[key])) {
        const arrayMappings: any = {};
        if (obj[key].length === 0) {
          continue;
        }
        if (typeof obj[key][0] === "object") {
          arrayMappings["type"] = "array[object]";
          arrayMappings["path"] = key;
          arrayMappings["mapping"] = transform(obj[key][0]);
          mappings[key] = arrayMappings;
          continue;
        }
        if (typeof obj[key][0] === "string") {
          arrayMappings["type"] = "array[string]";
          arrayMappings["path"] = key;
          mappings[key] = arrayMappings;
          continue;
        }
      } else {
        const objectMappings: any = {};
        objectMappings["type"] = "object";
        objectMappings["path"] = key;
        objectMappings["mapping"] = transform(obj[key]);
        mappings[key] = objectMappings;
      }
    }
    if (typeof obj[key] === "string") {
      const stringMappings: any = {};
      stringMappings["type"] = "string";
      stringMappings["path"] = key;
      mappings[key] = stringMappings;
    }
  }
  return mappings;
};

main();
