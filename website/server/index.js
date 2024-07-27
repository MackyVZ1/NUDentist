const express = require('express')
const app = express()
const port = 8000
app.get("/", (req, res) => {
    res.json({message : 'Hello World!'})
})

app.listen(port,console.log("server is running on the port"));