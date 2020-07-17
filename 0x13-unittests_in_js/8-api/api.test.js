const mocha = require('mocha');
const { expect } = require('chai');

const request = require('request');

describe('API', () => {
  describe('GET index', () => {
    it('should return status code 200', (done) => {
      request('http://localhost:7865', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(200);
      });
      done();
    });

    it('should return correct message', (done) => {
      request('http://localhost:7865', (err, res, body) => {
        if (err) throw err;
        expect(body).to.equal('Welcome to the payment system');
      });
      done();
    });
  });
});
