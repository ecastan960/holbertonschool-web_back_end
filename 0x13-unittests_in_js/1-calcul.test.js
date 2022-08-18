const assert = require('assert');
const calculateNumber = require("./1-calcul");

describe('calculateNumber', function () {
  it('SUM', function () {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
  });
  it('SUBTRACT', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3.7), -3);
  });
  it('DIVIDE', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5,), 0.2);
    assert.strictEqual(calculateNumber('DIVIDE', 1, 0), 'Error');
  });
});
