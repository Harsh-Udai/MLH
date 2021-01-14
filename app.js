const express = require('express');
const path = require('path');
const hbs = require('hbs');

const app = express();

app.set('view engine','hbs');
app.set('views',path.join(__dirname,'/views'));
app.use(express.static(path.join(__dirname,'/public')));

//Data Part
let data = [];

app.get('/',(req,res)=>{
    res.render('index');
})

app.get('/data',(req,res)=>{
    res.send({
        data: data
    })
})

app.get('/data_main',(req,res)=>{
    data.push(req.query.todo);
    res.send({
        data:data
    })
})

app.get('/delete',(req,res)=>{
    const value = req.query.todo;
    data.splice(value,1);
    res.send({
        data:data
    })
})

app.listen(3000,()=>{
    console.log("Server Started")
});