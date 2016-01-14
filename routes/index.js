var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express',
  						name: 'Winston Hurst',
  						ami_name: 'wdh_esc_node'
   });					
});

module.exports = router;
