var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : '',
  user     : 'yuansusu',
  password : '111111111111111111111',
  database : 'mydatabase'
});

connection.connect();

connection.query('select * from mytable where id=1, function (error, results, fields) {
  if (error) throw error;
  console.log('The solution is: ', results);
});

connection.end();
