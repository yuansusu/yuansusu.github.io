var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : '',
  user     : 'wenba',
  password : '2njkRQ3sUqW2Q8w2qoHvgVURQyjsK5hK',
  database : 'fudao_crm_clue_02'
});

connection.connect();

connection.query('select * from fudao_crm_clue where id=3716572', function (error, results, fields) {
  if (error) throw error;
  console.log('The solution is: ', results);
});

connection.end();