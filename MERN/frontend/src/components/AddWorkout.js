import React, {useState} from "react";
import { TextField, FormControl, Button } from "@mui/material";
import { Link } from "react-router-dom"
import "../styles/AddWorkout.css"
const AddWorkout = () => {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [emailError, setEmailError] = useState(false)
    const [passwordError, setPasswordError] = useState(false)
 
    const handleSubmit = (event) => { 
        event.preventDefault()
 
        setEmailError(false)
        setPasswordError(false)
 
        if (email == '') {
            setEmailError(true)
        }
        if (password == '') {
            setPasswordError(true)
        }
 
        if (email && password) {
            console.log(email, password)
            const AddWorkout = async()=>{
                const response = await fetch("/api/workouts/", {
                    method: "POST",
                    body: JSON.stringify({title:email, time:password}),
                    headers: {
                        "Content-Type": "application/JSON"
                    }
                })
                if(!response.ok){
                    console.log("ERROR!")
                }

            }
            AddWorkout()
            setEmail("")
            setPassword("")
        }
        
    }
     
    return ( 
        <div className="container">
        <React.Fragment>
        <form autoComplete="off" onSubmit={handleSubmit}>
            <h2>Add Workout</h2>
                <TextField 
                    label="Workout"
                    onChange={e => setEmail(e.target.value)}
                    required
                    variant="outlined"
                    color="secondary"
                    type="text"
                    sx={{mb: 3}}
                    fullWidth
                    value={email}
                    error={emailError}
                 />
                 <TextField 
                    label="Time"
                    onChange={e => setPassword(e.target.value)}
                    required
                    variant="outlined"
                    color="secondary"
                    type="number"
                    value={password}
                    error={passwordError}
                    fullWidth
                    sx={{mb: 3}}
                 />
                 <Button variant="outlined" color="secondary" type="submit">Add workout</Button>
             
        </form>
        </React.Fragment>
        </div>
     );
}
 
export default AddWorkout;