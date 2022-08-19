let chai = require('chai');
let expect = chai.expect;
const sinon = require('sinon');

const sendPaymentRequestToApi = require('./5-payment.js');

describe('sendPaymentRequestToApi', () => {
  let spy;
  beforeEach(() => spy = sinon.spy(console, 'log'));
  afterEach(() => spy.restore());

  it('sendPaymentRequestToAPI(100, 20)', () => {
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledWith('The total is: 120')).to.be.true;
    expect(spy.calledOnce).to.be.true;
  });
  it('sendPaymentRequestToAPI(10, 10)', () => {
    sendPaymentRequestToApi(10, 10);
    expect(spy.calledWith('The total is: 20')).to.be.true;
    expect(spy.calledOnce).to.be.true;
  });
});
