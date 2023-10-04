const express = require('express')
const router = express.Router()
const {getAllWorkouts, addWorkout, getByID, updateByID, deleteByID} = require("../controller/workoutController")

router.get("/", getAllWorkouts)
router.post("/", addWorkout)
router.get("/:id", getByID)
router.patch("/:id", updateByID)
router.delete("/:id", deleteByID)

module.exports = router