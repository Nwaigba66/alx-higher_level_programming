$.get('https://swapi-api.alx-tools.com/api/people/5/?', function (character, textStatus) {
  $('DIV#character').text(character.name);
});
