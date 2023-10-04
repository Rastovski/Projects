require('dotenv').config()
const mongoose = require("mongoose")
const express = require("express")
const app = express()
const routes = require("./routes/workoutRoutes")

app.use(express.json()) // for request body
app.use("/api/workouts/", routes)


mongoose.connect(process.env.mongoDB)
        .then(()=>{
            console.log("Successfully connected!")
            app.listen(process.env.PORT,()=>{
                console.log(`Listening on PORT: ${process.env.PORT}`)
            })
        })
        .catch((error)=>{
            console.log("Database not connected!")
        })
