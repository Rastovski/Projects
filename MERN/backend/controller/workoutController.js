const Workout = require("../model/workoutSchema")
const mongoose = require("mongoose")

const getAllWorkouts = async (req, res)=>{
    const workouts = await Workout.find({})
    
    if(!workouts){
        return res.status(400).json({message: "Workouts not found! Error."})
    }
    res.status(200).json(workouts)
}

const getByID = async(req, res)=>{
    const {id} = req.params
    if(!mongoose.isValidObjectId(id)){
        console.log("Id is not valid!")
        return res.status(400).json({message: "Id not valid!"})
    }
    const workout = await Workout.findById(id)
    
    if(!workout){
        return res.status(400).json({message: "Workouts not found! Error."})
    }
    res.status(200).json(workout)

}

const addWorkout = async (req, res)=>{
    const {title, time, date} = req.body
    const workout = await Workout.create({title, time, date})
    if(!workout){
        return res.status(400).json({message: "Workouts not found! Error."})
    }
    res.status(200).json(workout)
}

const deleteByID = async (req, res)=>{
    const {id} = req.params
    if(!mongoose.isValidObjectId(id)){
        console.log("Id is not valid!")
        return res.status(400).json({message: "Id not valid!"})
    }
    const workouts = await Workout.findByIdAndDelete(id)
    
    if(!workouts){
        return res.status(400).json({message: "Workouts not found! Error."})
    }
    res.status(200).json(workouts)

}

const updateByID = async (req, res)=>{
    const {id} = req.params
    if(!mongoose.isValidObjectId(id)){
        console.log("Id is not valid!")
        return res.status(400).json({message: "Id not valid!"})
    }
    const workouts = await Workout.findByIdAndUpdate(id, req.body)
    
    if(!workouts){
        return res.status(400).json({message: "Workouts not found! Error."})
    }
    res.status(200).json(workouts)
}

module.exports = {
    getAllWorkouts,
    addWorkout,
    getByID,
    deleteByID,
    updateByID
}