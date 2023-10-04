const mongoose = require("mongoose")

const Schema = mongoose.Schema;

const workoutSchema = new Schema({
    title:{
        type: String,
        required: true
    },
    time: {
        type: Number,
        required: true
    },
    date: {
        type: Date, default: Date.now }

},{
    timestamps: {
        type: String
    }
})

module.exports = mongoose.model("Workout", workoutSchema);