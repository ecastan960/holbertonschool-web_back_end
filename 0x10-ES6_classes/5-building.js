export default class Building {
  constructor(sqft) {
    const test = typeof this.evacuationWarningMessage !== 'function';
    if (this.constructor !== Building && test) {
      throw Error(
        'Class extending Building must override evacuationWarningMessage',
      );
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
