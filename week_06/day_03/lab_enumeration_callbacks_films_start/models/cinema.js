const Cinema = function(films) {
    this.films = films;
};

module.exports = Cinema;

Cinema.prototype.findTitles = function(films) {
    const titles = this.films.map((film) => {
        return film.title
    });
    return titles
};

Cinema.prototype.findByTitle = function(title) {
    const found = this.films.find(film => film.title === title);
    return found;
};

Cinema.prototype.findAllGenre = function(genre) {
    const result = this.films.filter(film => film.genre === genre);
    return result;
};

Cinema.prototype.findByYear = function(year) {
    const result = this.films.filter(film => film.year === year);
    return result
};

Cinema.prototype.yearCheck = function(year) {
    const result = this.films.includes(year);
    return result;
};

Cinema.prototype.runningTime = function(runtime) {
    const result = this.films.every((film => film.length > runtime));
    return result
};

Cinema.prototype.totalRuntime = function(films) {
    const result = this.films.reduce((runningTotal, film) => {
        return runningTotal + film.length
    }, 0);
    return result
};