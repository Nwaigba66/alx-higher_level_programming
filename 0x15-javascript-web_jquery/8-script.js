$.ajax({
  method: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function(movies) {
    movies.output.forEach(function (movie) {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
});
}
});
