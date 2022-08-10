export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  if (weakMap.has(endpoint)) {
    const consult = weakMap.get(endpoint);
    if (consult >= 4) throw Error('Endpoint load is high');
    weakMap.set(endpoint, weakMap.get(endpoint) + 1);
  } else { weakMap.set(endpoint, 1); }
}
