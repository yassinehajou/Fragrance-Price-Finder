const express = require('express');
const app = express();
// const mysql = require('mysql');

// const db = mysql.createConnection({
//     user: "root",
//     host: "localhost",
//     password: "",
//     database: "fragrances",
// });

app.listen(3001, () => {
    console.log("Listening on port 3001");
});
