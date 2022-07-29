export default function createIteratorObject(report) {
  return Object.values(report.allEmployees).reduce((acc, next) => acc.concat(next), []);
}
