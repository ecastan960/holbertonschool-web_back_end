const chai = require('chai');
let expect = chai.expect;
const request = require('request');

describe('integration testing', () => {
  describe('GET /', () => {
    it('endpoint GET /', (done) => {
      const endpoint = {
        url: 'http://localhost:7865',
        method: 'GET',
      };
      request(endpoint, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });
});

describe('regex integration testing', () => {
  describe('GET /cart/:id', () => {
    it('endpoint: GET /cart/:id', (done) => {
      const endpoint = {
        url: 'http://localhost:7865/cart/12',
        method: 'GET',
      };
      request(endpoint, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 12');
        done();
      });
    });
  });
  describe('GET /cart/:isNaN', () => {
    it('endpoint: GET /cart/:isNaN', (done) => {
      const endpoint = {
        url: 'http://localhost:7865/cart/anything',
        method: 'GET',
      };
      request(endpoint, (error, response, body) => {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });
});
