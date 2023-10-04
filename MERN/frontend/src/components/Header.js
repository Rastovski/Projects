import "../styles/Header.css"
import {Link} from "react-router-dom"

const Header = ()=>{
    return(
        <ul>
            <Link className="link" to="/">All Workouts</Link>
            <Link className="link" to="/addworkout">Add Workout</Link>
        </ul>
    )
}

export default Header; 