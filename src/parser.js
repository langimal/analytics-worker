const { Console } = require('console');
const { Transform } = require('stream');
const { createHash } = require('crypto');

class Parser extends Transform {
  constructor(options) {
    super(options);
    this.settings = options.settings;
    this.hash = createHash('md5');
  }

  _transform(chunk, encoding, callback) {
    this.hash.update(chunk);
    callback(null, chunk);
  }

  _flush(callback) {
    const digest = this.hash.digest('hex');
    this.push(digest);
    callback();
  }
}

module.exports = Parser;