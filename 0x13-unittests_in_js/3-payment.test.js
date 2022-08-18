let chai = require('chai');
let expect = chai.expect;
const sinon = require('sinon');

const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./3-payment.js');

describe('sendPaymentRequestToApi', () => {
  const spy = sinon.spy(Utils, 'calculateNumber');

  it('validate the usage of the Utils function', () => {
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledWith('SUM', 100, 20)).to.be.true;
    expect(spy.calledOnce).to.be.true;
    spy.restore();
  });
});
