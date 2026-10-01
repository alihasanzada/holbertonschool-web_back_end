export default function createIteratorObject(report) {
  const departments = Object.values(report.allEmployees);

  return (function* iterate() {
    for (const employees of departments) {
      yield* employees;
    }
  }());
}
